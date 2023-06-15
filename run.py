import random
import string
import humanize
import math
from colorama import Fore, Style


class ComparePasswords:
    def __init__(self):
        self.common_passwords = self.load_common_passwords()

    def load_common_passwords(self):
        with open("common_passwords.txt", "r") as file:
            return [line.strip() for line in file]

    def validate_common_password(self, password):
        return password not in self.common_passwords


class Diceware:
    def __init__(self):
        self.diceware_word_list = self.load_wordlists()

    def load_wordlist_from_file(self, filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file]

    def load_wordlists(self):
        word_list = []
        word_list.extend(self.load_wordlist_from_file("3_letter_wordlist.txt"))
        word_list.extend(self.load_wordlist_from_file("4_letter_wordlist.txt"))
        return word_list

    def generate_diceware_passphrase(self, passphrase_length):
        min_length = 6
        max_length = 16

        if passphrase_length < min_length or passphrase_length > max_length:
            raise ValueError
            (f"Password length must be between {min_length} and {max_length}.")

        num_special_symbols = passphrase_length // 3

        # Generate the passphrase
        passphrase = ""
        for _ in range(num_special_symbols):
            passphrase += random.choice(self.diceware_word_list)
            + random.choice(string.punctuation)

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
    while response not in valid_responses:
        response = input(message).strip().lower()
    return response


def prompt_user_integer(message, min_value, max_value):
    while True:
        try:
            response = int(input(message))
            if min_value <= response <= max_value:
                return response
            else:
                print(f"Please enter a number between|\
                {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_entropy(pool_size, password_length):
    entropy = int(password_length * math.log2(pool_size))
    return entropy


def get_entropy_strength(entropy):
    if entropy < 28:
        return "Very Weak; might keep out family members"
    elif entropy <= 35:
        return "Weak; should keep out most people, " \
               "often good for desktop login passwords"
    elif entropy <= 59:
        return "Reasonable; fairly secure passwords " \
               "for network and company passwords"
    elif entropy <= 127:
        return "Strong; can be good for guarding financial information"
    else:
        return "Very Strong; often overkill"


def generate_password_suggestion():
    diceware = Diceware()
    min_length = 6
    max_length = 16
    passphrase_length = prompt_user_integer(
        f"Enter the desired password length ({min_length}-{max_length}): ",
        min_length,
        max_length
    )
    passphrase = diceware.generate_diceware_passphrase(passphrase_length)
    print("Generated password:", Fore.CYAN + passphrase + Style.RESET_ALL)

    # Calculate password entropy
    pool_size = len(diceware.diceware_word_list) + len(string.punctuation)
    entropy = calculate_entropy(pool_size, passphrase_length)
    entropy_strength = get_entropy_strength(entropy)
    print("\nYour passwords strength:", entropy, "bits")
    print(entropy_strength, "\n")

    # Calculate password uniqueness
    word_list_size = 2059
    special_symbol_count = len(string.punctuation)
    lowercase_letter_count = 26

    total_combinations = 0

    for length in range(min_length, max_length + 1):
        num_special_symbols = length - 1
        num_word_choices = length - num_special_symbols
        combinations = (
                (word_list_size + special_symbol_count
                 + lowercase_letter_count) **
                num_word_choices * (special_symbol_count **
                                    num_special_symbols)
        )
        total_combinations += combinations

    readable_combinations = humanize.intword(total_combinations)

    print(
        Fore.GREEN + f"There are approximately {readable_combinations}\
        possible passwords of this length." +
        Style.RESET_ALL)

    return passphrase


def main():
    print(":'######::'####:'########::'##::::'##:'########:'########:::::")
    print("'##... ##:. ##:: ##.... ##: ##:::: ##: ##.....:: ##.... ##::::")
    print(" ##:::..::: ##:: ##:::: ##: ##:::: ##: ##::::::: ##:::: ##::::")
    print(" ##:::::::: ##:: ########:: #########: ######::: ########:::::")
    print(" ##:::::::: ##:: ##.....::: ##.... ##: ##...:::: ##.. ##::::::")
    print(" ##::: ##:: ##:: ##:::::::: ##:::: ##: ##::::::: ##::. ##:::::")
    print(". ######::'####: ##:::::::: ##:::: ##: ########: ##:::. ##::::")
    print(":......:::....::..:::::::::..:::::..::........::..:::::..:::::")
    print("'########::'#######::'########:::'######:::'########:         ")
    print(" ##.....::'##.... ##: ##.... ##:'##... ##:: ##.....::         ")
    print(" ##::::::: ##:::: ##: ##:::: ##: ##:::..::: ##:::::::         ")
    print(" ######::: ##:::: ##: ########:: ##::'####: ######:::         ")
    print(" ##...:::: ##:::: ##: ##.. ##::: ##::: ##:: ##...::::         ")
    print(" ##::::::: ##:::: ##: ##::. ##:: ##::: ##:: ##:::::::         ")
    print(" ##:::::::. #######:: ##:::. ##:. ######::: ########:         ")

    print(
        Fore.CYAN + "Introducing Cipher-Forge:\
        Your Advanced Password Generator" +
        Style.RESET_ALL + "\n"
    )
    print("Let's start by checking your current password against ")
    print("a list of commonly known passwords.\n")

    compare = ComparePasswords()
    password = input("Enter a password to test: ")

    # Sanitize user input
    password = password.strip()

    # Password validation
    if compare.validate_common_password(password):
        print("Your password is not a commonly known password.")
        print("We still recommend changing it periodically.")
    else:
        print(Fore.RED + "Your password is too common.")
        print("We suggest you change it." + Style.RESET_ALL)

    choice = prompt_user("Do you want a generated suggestion now?\
    (yes/no): ", ["yes", "no"])

    while choice == "yes":
        print("\n# Generate password suggestion")
        passphrase = generate_password_suggestion()
        choice = prompt_user("Do you want to generate another password?\
        (yes/no): ", ["yes", "no"])

    print("\nThank you for using Cipher-Forge. Stay safe!")


if __name__ == "__main__":
    main()
