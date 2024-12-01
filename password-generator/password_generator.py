import random
import string


def main():
    print('Welcome to the Password Generator')

    while True:
        try:
            length = int(
                input('\nEnter the desired password length (minimum 6): '))
            password = generate_password(length)
            print(f'\nYour generated password is: {password}')
        except ValueError as e:
            print(f'\nError: {e}. Please try again.')

        choice = input(
            'Generate another password? (y)es or (n)o: ').strip().lower()
        if choice not in ('y', 'yes'):
            print('Bye!')
            break


def generate_password(length=10):
    if length < 6:
        raise ValueError('Password length should be at least 6 characters')

    upper_char = string.ascii_uppercase
    lower_char = string.ascii_lowercase
    digit_char = string.digits
    special_char = string.punctuation

    all_characters = upper_char + lower_char + digit_char + special_char
    password = [
        random.choice(upper_char),
        random.choice(lower_char),
        random.choice(digit_char),
        random.choice(special_char)
    ]
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)


if __name__ == '__main__':
    main()
