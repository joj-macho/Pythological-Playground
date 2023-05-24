'''
Calculate the absolute value of a number entered by the user.

This program prompts the user to enter a number and calculates its absolute value.
The absolute value of a number is the magnitude of the number without considering its sign.
The program handles invalid inputs and ensures that a valid number is entered by the user.

Usage:
    1. The program prompts the user to enter a number.
    2. The user enters a number (can be positive, negative, or zero).
    3. The program calculates the absolute value of the entered number.
    4. The program displays the absolute value of the number.

Example:
    Enter a number: -4.5
    The absolute value of -4.5 is 4.5.

Note:
    - The program uses the built-in abs() function to calculate the absolute value.
    - If the user enters an invalid input (non-numeric), an error message is displayed, and the user is prompted to enter a valid number.
'''

def main():
    '''This program calculates the absolute value of a number entered by the user.'''

    print('\nAbsolute Value Calculator\n')

    # Enter a valid number
    while True:
        try:
            number = float(input('Enter a number:\n> '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid number!')

    absolute_value = abs(number)
    print(f'The absolute value of {number} is {absolute_value}.')


if __name__ == '__main__':
    main()

