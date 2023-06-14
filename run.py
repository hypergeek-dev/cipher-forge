import random
import string
import humanize
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

    def generate_diceware_passphrase(self):
        min_length = 8
        max_length = 16

        # Determine the length of the passphrase
        passphrase_length = random.randint(min_length, max_length)

        num_special_symbols = passphrase_length - 1

        # Generate the passphrase
        passphrase = ''
        for _ in range(num_special_symbols):
            passphrase += random.choice(self.diceware_word_list) + \
                random.choice(string.punctuation)

        passphrase += random.choice(self.diceware_word_list).capitalize()

        remaining_length = passphrase_length - len(passphrase)
        for _ in range(remaining_length):
            if random.random() < 0.5:
                passphrase += random.choice(self.diceware_word_list)
            else:
                passphrase += random.choice(string.punctuation)

        return passphrase[:max_length]


def prompt_user(message, valid_responses):
    response = None
    while response not in valid_responses:
        response = input(message).strip().lower()
    return response


def main():
    # Introduction
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
        Fore.CYAN + "Introducing Cyber-Forge: Your Advanced Password Generator" +
        Style.RESET_ALL + "\n"
    )
    print("In today's digital age, strong passwords are crucial "
          "for safeguarding your sensitive information.")
    print("Meet Cyber-Forge, an advanced password generator designed "
          "to help you create")
    print("robust passwords.\n")
    print("Let's start by checking your current password against "
          "a list of commonly known passwords.\n")

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

    choice = prompt_user("Do you want a generated suggestion now? (yes/no): ", ["yes", "no"])

    # Generate password suggestion
    if choice == "yes":
        diceware = Diceware()
        passphrase = diceware.generate_diceware_passphrase()
        print(Fore.GREEN + "Generated password: " + passphrase + Style.RESET_ALL)
    else:
        exit()

    # Calculate password uniqueness
    min_length = 8
    max_length = 16
    word_list_size = 2059
    special_symbol_count = len(string.punctuation)
    lowercase_letter_count = 26

    total_combinations = 0

    for length in range(min_length, max_length + 1):
        num_special_symbols = length - 1
        num_word_choices = length - num_special_symbols
        combinations = (
            (word_list_size + special_symbol_count + lowercase_letter_count) **
            num_word_choices * (special_symbol_count ** num_special_symbols)
        )
        total_combinations += combinations

    readable_combinations = humanize.intword(total_combinations)

    print(Fore.YELLOW + "This password is uniquely created, out of:\n" +
          str(readable_combinations) + " possible combinations" +
          Style.RESET_ALL)


if __name__ == "__main__":
    main()
