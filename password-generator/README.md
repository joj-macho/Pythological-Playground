# Password Generator

## Description

The "Password Generator" allows you to generate a random password of a specified length using a mix of characters (uppercase, lowercase, digits, special characters).

## How it Works
- Enter the length of the password (> 6).
- Voilà.

## Running the Program

```bash
# Navigate to the project directory
cd password-generator/

# Run the main script
python3 password_generator.py
```

## Program Input & Output

When you run `password_generator.py`, the output will look like this:

```
Password Generator

Enter the desired password length (minimum 6): 5

Error: Password length should be at least 6 characters. Please try again.
Generate another password? (y)es or (n)o: y

Enter the desired password length (minimum 6): 6

Your generated password is: >0oU7e
Generate another password? (y)es or (n)o: y

Enter the desired password length (minimum 6): 30

Your generated password is: +AhrVn&Lnk4QUPVZsYZDof?v8UO1]5
Generate another password? (y)es or (n)o: y

Enter the desired password length (minimum 6): l2

Error: invalid literal for int() with base 10: 'l2'. Please try again.
Generate another password? (y)es or (n)o: n
Bye!
```