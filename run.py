import random
import string
import humanize

print("Introducing Cyber-Forge: Your Advanced Password Generator\n")
print("In today's digital age, strong passwords are crucial for safeguarding your sensitive information.")
print("Meet Cyber-Forge, an advanced password generator designed to help you create robust passwords that adhere to the best practices of password security.\n")
print("Let's start by checking your current password against a list of commonly known passwords.\n")

class ComparePasswords:
    def __init__(self):
        self.common_passwords = ["12345", "123456", ...]

    def validate_common_password(self, password):
        if password in self.common_passwords:
            return False
        return True

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

        # Calculate the number of special symbols needed
        num_special_symbols = passphrase_length - 1

        # Generate the passphrase
        passphrase = ''
        for _ in range(num_special_symbols):
            passphrase += random.choice(self.diceware_word_list) + random.choice(string.punctuation)

        # Add a word with a capital letter
        passphrase += random.choice(self.diceware_word_list).capitalize()

        # Fill up the remaining space with random words and symbols
        remaining_length = passphrase_length - len(passphrase)
        for _ in range(remaining_length):
            if random.random() < 0.5:
                passphrase += random.choice(self.diceware_word_list)
            else:
                passphrase += random.choice(string.punctuation)

        return passphrase[:max_length]  # Truncate passphrase if it exceeds max_length

compare = ComparePasswords()
password = input("Enter a password to test: ")
if compare.validate_common_password(password):
    print("Your password is not a commonly known password. We still recommend changing it periodically.")
else:
    print("Your password is too common. We suggest you change it.")

choice = input("Do you want to do that now? (yes/no): ")

if choice.lower() == "yes":
    diceware = Diceware()
    passphrase = diceware.generate_diceware_passphrase()
    print("Generated Diceware Passphrase:", passphrase)
else:
    exit()