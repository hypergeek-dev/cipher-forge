import random
import string

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
    
        self.password_length = 0
        self.common_passwords = ["12345", "123456", "123456789", "test1", "password", "12345678", "zinch", "g_czechout", "asdf", "qwerty", "1234567890", "1234567", "Aa123456.", "iloveyou", "1234", "abc123", "111111", "123123", "dubsmash", "test", "princess", "qwertyuiop", "sunshine", "BvtTest123", "11111", "ashley", "00000", "000000", "password1", "monkey", "livetest", "55555", "soccer", "charlie", "asdfghjkl", "654321", "family", "michael", "123321", "football", "baseball", "q1w2e3r4t5y6", "nicole", "jessica", "purple", "shadow", "hannah", "chocolate", "michelle", "daniel", "maggie", "qwerty123", "hello", "112233", "jordan", "tigger", "666666", "987654321", "superman", "12345678910", "summer", "1q2w3e4r5t", "fitness", "bailey", "zxcvbnm", "fuckyou", "121212", "buster", "butterfly", "dragon", "jennifer", "amanda", "justin", "cookie", "basketball", "shopping", "pepper", "joshua", "hunter", "ginger", "matthew", "abcd1234", "taylor", "samantha", "whatever", "andrew", "1qaz2wsx3edc", "thomas", "jasmine", "animoto", "madison", "54321", "flower", "Password", "maria", "babygirl", "lovely", "sophie", "Chegg123", "computer", "qwe123", "anthony", "1q2w3e4r", "peanut", "bubbles", "asdasd", "qwert", "1qaz2wsx", "pakistan", "123qwe", "liverpool", "elizabeth", "harley", "chelsea", "familia", "yellow", "william", "george", "7777777", "loveme", "123abc", "letmein", "oliver", "batman", "cheese", "banana", "testing", "secret", "angel", "friends", "jackson", "aaaaaa", "softball", "chicken", "lauren", "welcome", "asdfgh", "robert", "orange", "Testing1", "pokemon", "555555", "melissa", "morgan", "123123123", "qazwsx", "diamond", "brandon", "jesus", "mickey", "olivia", "changeme", "danielle", "victoria", "gabriel", "123456a", "0.00000000", "hockey", "freedom", "azerty", "snoopy", "skinny", "myheritage", "qwerty1", "159753", "forever", "killer", "joseph", "master", "mustang", "hellokitty", "school", "Password1", "patrick", "blink182", "tinkerbell", "rainbow", "n, , athan", "cooper", "onedirection", "alexander", "jordan23", "lol123", "jasper", "junior", "q1w2e3r4", "222222", "benjamin", "jonathan", "passw0rd", "a123456", "samsung", "123", "love123", "picture1", "senha", "qwertyu", "123456789a", "unknown", "123456q", "qweqwe", "212121", "741852963", "232323", "999999999", "qwerty12345", "qwaszx", "1234567891", "456123", "444444", "qq123456", "xxx"] 

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
        print("1. Diceware")
        print("2. Random")
        print("3. Test Against Commonly Used Passwords")

        choice = input("Enter the number corresponding to your choice: ")

        if choice == "2":
            self.password_length = int(input("Enter the desired password length: "))

        if choice == "1":
            passphrase = self.generate_diceware_passphrase()
            print("Generated Diceware Passphrase:", passphrase)
        elif choice == "2":
            password = self.generate_random_password()
            print("Generated Random Password:", password)
        elif choice == "3":
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