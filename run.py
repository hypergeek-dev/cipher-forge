import sys
import random
import string
import humanize
import math
from colorama import Fore, Style
import re


class ComparePasswords:
    def __init__(self):
        self.common_passwords = self.load_common_passwords()

    def load_common_passwords(self):
        with open("assets/wordlists/common_passwords.txt", "r") as file:
            return [line.strip() for line in file]

    def validate_common_password(self, password):
        try:
            if password == "":
                return "The password is empty"
            if password in self.common_passwords:
                return Fore.RED + """\nYour password is among the 200
most used passwords.
We suggest you change it!
""" + Style.RESET_ALL

            if not re.match(r"^[^\x00-\x1F\x7F]+$", password):
                return "\nThe password contains invalid characters"

            return Fore.GREEN + """\nYour password is not a commonly
known password.
We still recommend changing it periodically.""" + Style.RESET_ALL

        except EOFError:
            return "Seems like your input was empty.\
                   Please enter something."
        except KeyboardInterrupt:
            return "You have pressed the Ctrl-C button."


class Diceware:
    def __init__(self):
        self.diceware_word_list = self.load_wordlists()

    def load_wordlist_from_file(self, filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file]

    def load_wordlists(self):
        word_list = []
        word_list.extend(self.load_wordlist_from_file(
            "assets/wordlists/3_letter_wordlist.txt"))
        word_list.extend(self.load_wordlist_from_file(
            "assets/wordlists/4_letter_wordlist.txt"))
        return word_list

    def generate_diceware_passphrase(self, passphrase_length):
        min_length = 6
        max_length = 16

        if passphrase_length < min_length or passphrase_length > max_length:
            error_message = (
                f"Password length must be between {min_length} "
                f"and {max_length}."
            )
            raise ValueError(error_message)

        num_special_symbols = passphrase_length // 3

        # Generate the passphrase
        passphrase = ""
        for _ in range(num_special_symbols):
            passphrase += random.choice(self.diceware_word_list)
            passphrase += random.choice(string.punctuation)

        passphrase += random.choice(self.diceware_word_list).capitalize()

        remaining_length = max_length - len(passphrase)
        remaining_length = min(remaining_length, passphrase_length)
        for _ in range(remaining_length):
            if random.random() < 0.5:
                passphrase += random.choice(self.diceware_word_list)
            else:
                passphrase += random.choice(string.punctuation)

        return passphrase[:passphrase_length]


def prompt_user(message, valid_responses):
    response = None
    try:
        while response not in valid_responses:
            response = input(message).strip().lower()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(0)  # Terminate the program gracefully

    return response


def prompt_user_integer(message, min_value, max_value):
    while True:
        try:
            response = int(input(message))
            if min_value <= response <= max_value:
                return response
            else:
                print(f"Please enter a number between "
                      f"{min_value} and {max_value}.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_entropy(pool_size, password_length):
    entropy = int(password_length * math.log2(pool_size))
    return entropy


def get_entropy_strength(entropy):
    if entropy < 28:
        return """Very Weak; as secure as writing
          your password on a sticky note."""
    elif entropy <= 35:
        return """Weak; it might keep out your
          technologically-challenged grandma."""
    elif entropy <= 59:
        return """Reasonable; enough to fend off
          your annoying co-worker."""
    elif entropy <= 127:
        return """Strong; your financial information
          is safer than hiding it under your
          mattress."""
    else:
        return "Very Strong; hackers will weep when they see this password!"


def generate_password_suggestion():
    try:
        password_length = prompt_user_integer("Enter the desired\
 password length(6-16): ", 6, 16)
        diceware = Diceware()
        passphrase = diceware.generate_diceware_passphrase(password_length)

        print(f"\nGenerated Password:{Fore.BLUE}" +
              f"{passphrase}{Style.RESET_ALL}")

        pool_size = len(diceware.diceware_word_list) + len(string.punctuation)
        entropy = calculate_entropy(pool_size, password_length)
        strength = get_entropy_strength(entropy)
        print(f"Entropy: {humanize.intcomma(entropy)} bits")
        print(f"Strength: {strength}")

    except ValueError as e:
        print(f"Error: {str(e)}")


def main():
    print(":'######::'####:'########::'##::::'##:'########:'########:::::")
    print("'##... ##:. ##:: ##.... ##: ##:::: ##: ##.....:: ##.... ##::::")
    print(" ##:::..::: ##:: ##:::: ##: ##:::: ##: ##::::::: ##:::: ##::::")
    print(" ##:::::::: ##:: ########:: #########: ######::: ########:::::")
    print(" ##:::::::: ##:: ##.....::: ##.... ##: ##...:::: ##.. ##::::::")
    print(" ##::: ##:: ##:: ##:::::::: ##:::: ##: ##::::::: ##::. ##:::::")
    print(". ######::'####: ##:::::::: ##:::: ##: ########: ##:::. ##::::")
    print(":......:::....::..:::::::::..:::::..::........::..:::::..:::::")
    print("'########::'#######::'########:::'######:::'########: ")
    print(" ##.....::'##.... ##: ##.... ##:'##... ##:: ##.....:: ")
    print(" ##::::::: ##:::: ##: ##:::: ##: ##:::..::: ##::::::: ")
    print(" ######::: ##:::: ##: ########:: ##::'####: ######::: ")
    print(" ##...:::: ##:::: ##: ##.. ##::: ##::: ##:: ##...:::: ")
    print(" ##::::::: ##:::: ##: ##::. ##:: ##::: ##:: ##::::::: ")
    print(" ##:::::::. #######:: ##:::. ##:. ######::: ########: ")

    print(
        Fore.CYAN + "Introducing Cipher-Forge: "
        "Your Advanced Password Generator" +
        Style.RESET_ALL + "\n")
    try:
        while True:
            print("\nMenu:")
            print("1. Test for common passwords.")
            print("2. Generate password.")
            print("3. Exit.")
            choice = prompt_user_integer("Enter your choice\
(1, 2, or 3): ", 1, 3)

            if choice == 1:
                password = input("Enter a password to test: ")
                compare_passwords = ComparePasswords()
                result = compare_passwords.validate_common_password(password)
                print(result)
            elif choice == 2:
                generate_password_suggestion()
            elif choice == 3:
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(0)

    print("\nThank you for using Cipher-Forge. Stay safe!")


if __name__ == "__main__":
    main()
    
