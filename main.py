import random
import string

print("=== Random Password Generator ===")

length = int(input("Enter password length: "))

print("Choose character types:")
use_letters = input("Include letters? (y/n): ").lower()
use_digits = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()

characters = ""

if use_letters == 'y':
    characters += string.ascii_letters

if use_digits == 'y':
    characters += string.digits

if use_symbols == 'y':
    characters += string.punctuation

if characters == "":
    print("You must select at least one character type!")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)
