def main():
    '''
    This program checks if one number is a factor of another number entered by the user.
    '''
    print('\nFactor Checker\n')

    # Get input from the user
    while True:
        try:
            factor = int(input('Enter the potential factor: '))
            number = int(input('Enter the number to be checked: '))
            break
        except ValueError:
            print('Invalid input. Please enter valid integers.')

    # Check if factor is a factor of number
    result = is_factor(factor, number)

    # Display the result
    print(f"{factor} is a factor of {number}: {result}")

def is_factor(factor, number):
    '''
    Check if factor is a factor of number.

    Parameters:
    - factor (int): The potential factor.
    - number (int): The number to be checked for divisibility.

    Returns:
    - bool: True if factor is a factor of number, False otherwise.
    '''
    return number % factor == 0

if __name__ == '__main__':
    main()
