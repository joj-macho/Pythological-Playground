# Password Generator

## Description

The Password Generator is a command-line program that assists users in generating, saving, and searching for passwords. It provides functionalities such as generating 'secure' passwords with various options, saving passwords to a database, and searching for saved passwords based on the website.

## How it Works

- The program uses the following modules:
    - The `random` module to generate random choices for creating passwords.
    - The `json` module for reading and writing JSON data.
    - The `string` module provides a collection of string constants, including ASCII letters (both lowercase and uppercase), digits, and punctuation symbols.
    - The `secrets` modulefor generating cryptographically secure random numbers.
    - The `os` module to interact with the operating system.
    - The `Path` class from the `pathlib` module for working with file system paths.

- The `main` function displays a menu with options to generate a password, save a password, search for passwords, or exit the program. The user is prompted to enter their choice, and the corresponding action is performed.

- The `generate_password` function generates a random password with the specified length and character types (lowercase letters, symbols, digits, uppercase letters). It utilizes the `secrets` module for secure random choices.

- The `save_password` function allows the user to save a password to the password database. It prompts the user to enter the website, username/email, and password length. The actual password is then generated using the `generate_password` function, and the data is saved to the 'passwords.json' file.

- The `search_password` function enables users to search for passwords in the database based on a website. It prompts the user to enter the website they want to search for, reads the 'passwords.json' file, and displays the matching passwords.

## Program Input & Output

When you run `password_generator.py`, the output will look like this:

```

Welcome to Password Generator

1. Generate Password
2. Save Password
3. Search Password
0. Exit program
Enter your choice: 1
Enter the password length: 12
Generated Password: YMiW5^VF!Muv

1. Generate Password
2. Save Password
3. Search Password
0. Exit program
Enter your choice: 2
Enter the website: www.reddit.com
Enter the username/email: jonathan
Enter the password length: 10
Password saved successfully.

1. Generate Password
2. Save Password
3. Search Password
0. Exit program
Enter your choice: 3
Enter the website to search for passwords: www.redidit.com
No passwords found for www.redidit.com.

1. Generate Password
2. Save Password
3. Search Password
0. Exit program
Enter your choice: 3
Enter the website to search for passwords: www.reddit.com
Website: www.reddit.com 
Username: jonathan 
Password: J+H0Sm@+&J

1. Generate Password
2. Save Password
3. Search Password
0. Exit program
Enter your choice: 0

Bye!
```