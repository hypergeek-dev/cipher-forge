import argon2
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.argon2_hasher = argon2.PasswordHasher()
        self.diceware_word_list = ["abacus", "abdomen"]
        self.password_length = 0
        self.common_passwords = ["12345", "123456"]

    def generate_argon2_hash(self, password):
        password_hash = self.argon2_hasher.hash(password)
        password_hash_lines = password_hash.splitlines()
        if len(password_hash_lines) >= 2:
            return password_hash_lines[1]
        else:
            raise Exception("Invalid Argon2 password hash")

    def generate_diceware_passphrase(self):
        passphrase = ''.join(random.choice(self.diceware_word_list) for _ in range(4))
        return passphrase

    def generate_random_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(self.password_length))
        return password

    def validate_common_password(self, password):
        if password in self.common_passwords:
            return False
        return True

    def prompt_choice(self):
        print("Password Generation Options:")
        print("1. Argon2")
        print("2. Diceware")
        print("3. Random")
        print("4. Test Against Commonly Used Passwords")

        choice = input("Enter the number corresponding to your choice: ")

        if choice == "3":
            self.password_length = int(input("Enter the desired password length: "))

        if choice == "1":
            password = input("Enter a password: ")
            password_hash = self.generate_argon2_hash(password)
            print("Generated Argon2 Password Hash:", password_hash)
        elif choice == "2":
            passphrase = self.generate_diceware_passphrase()
            print("Generated Diceware Passphrase:", passphrase)
        elif choice == "3":
            password = self.generate_random_password()
            print("Generated Random Password:", password)
        elif choice == "4":
            password = input("Enter a password to test: ")
            if self.validate_common_password(password):
                print("The password is not commonly used.")
            else:
                print("The password is commonly used. Please choose a stronger password.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.prompt_choice()
