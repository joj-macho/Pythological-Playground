import random
import json
import string
import secrets
import os
from pathlib import Path


# Set Working Directory
BASE_DIRECTORY = Path(__file__).resolve().parent
os.chdir(BASE_DIRECTORY)

PASSWORDS_FILE = 'passwords.json'

def main():
    """Main function to run the password manager."""
    
    print('\nWelcome to Password Generator\n')

    while True:
        # Display menu options
        print("1. Generate Password")
        print("2. Save Password")
        print("3. Search Password")
        print("0. Exit program")

        choice = input("Enter your choice: ")

        if choice == '0':
            print("\nBye!")
            break
        elif choice == '1':
            while True:
                try:
                    password_length = int(input("Enter the password length: "))
                    if password_length > 0:
                        break
                    else:
                        print("Password length should be a positive integer.\n")
                except ValueError:
                    print("Invalid input. Please enter a valid length (a positive integer).\n")

            password = generate_password(password_length)
            print(f"Generated Password: {password}\n")
        elif choice == '2':
            save_password()
        elif choice == '3':
            search_password()
        else:
            print("Invalid choice. Please enter 0, 1, 2, or 3.\n")

def generate_password(length, use_symbols=True, use_digits=True, use_uppercase=True):
    '''Generate a random password.'''
    characters = string.ascii_lowercase

    if use_symbols:
        characters += "!@#$%^&*()_-+=<>?"
    if use_digits:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def save_password():
    """Save a password to the passwords database."""

    website = input("Enter the website: ")
    username = input("Enter the username/email: ")

    while True:
        try:
            password_length = int(input("Enter the password length: "))
            if password_length > 0:
                break
            else:
                print("Password length should be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid length (a positive integer).")

    password = generate_password(password_length)

    data = {
        'website': website,
        'username': username,
        'password': password
    }

    try:
        with open(PASSWORDS_FILE, 'r') as file:
            passwords = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        passwords = []

    passwords.append(data)

    with open(PASSWORDS_FILE, 'w') as file:
        json.dump(passwords, file, indent=4)

    print("Password saved successfully.\n")

def search_password():
    """Search for passwords in the passwords database."""
    
    website = input("Enter the website to search for passwords: ")

    try:
        with open(PASSWORDS_FILE, 'r') as file:
            passwords = json.load(file)

        found_passwords = [data for data in passwords if data['website'] == website]

        if found_passwords:
            for data in found_passwords:
                print(f"Website: {data['website']} \nUsername: {data['username']} \nPassword: {data['password']}\n")
        else:
            print(f"No passwords found for {website}.\n")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No passwords found. Database is empty.\n")


if __name__ == "__main__":
    main()
