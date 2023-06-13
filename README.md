# password_generator
###A password generator created in python

This code implements a password generator with different options for generating passwords. It uses the argon2 library for hashing passwords and provides options for generating diceware passphrases, random passwords, and testing against commonly used passwords.

Installation
To use this code, you need to have python and the argon2 library installed. You can install it using pip:

pip install python
pip install argon2-cffi

##Usage
You will be prompted to choose one of the following options:

Argon2: Enter a password and generate an Argon2 password hash.
Diceware: Generate a diceware passphrase.
Random: Generate a random password with a specified length.
Test Against Commonly Used Passwords: Enter a password to check if it is commonly used.
Based on your choice, you will be prompted for additional input, and the generated password or result will be displayed.

Customization
The code includes a list of commonly used passwords (common_passwords). You can add more commonly used passwords to this list if desired.

Dependencies
argon2: This library is used for password hashing. Install it using pip install argon2-cffi.
Note
Please ensure that you use the generated passwords responsibly and follow best practices for password security.