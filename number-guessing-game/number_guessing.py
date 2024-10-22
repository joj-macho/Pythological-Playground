import random

MAX_ATTEMPTS = 5


def main():
    '''Play the Number Guessing Game.'''
    print('''
Welcome to the Number Guessing Game!

Here's how to play:

- Enter the lower and upper bounds for the range of the secret number.
- Guess the secret number.
- After each guess, you will receive clues:
   - "Too low!" if your guess is less than the secret number.
   - "Too high!" if your guess is greater than the secret number.
   - "Correct!" if your guess matches the secret number.
''')

    input('Press Enter to start guessing...')

    while True:
        lower_bound, upper_bound = get_number_range()

        # Generate secret number
        secret_number = random.randint(lower_bound, upper_bound)
        # Uncomment for debugging to see secret number
        # print('\nMy secret number is:', secret_number)

        num_of_attempts = 0

        print(f'I am thinking of a number between [{lower_bound}, '
              f'{upper_bound}].')
        print('Can you guess it?')
        print(f'You have {MAX_ATTEMPTS} attempts to guess it.\n')

        while num_of_attempts < MAX_ATTEMPTS:
            try:
                print(f'Attempt #{num_of_attempts + 1}')
                player_guess = int(input('Enter your guess:\n> '))

                # check if guess within bounds
                if player_guess < lower_bound or player_guess > upper_bound:
                    print(f'Your guess is out of bounds! Please enter a '
                          f'number between {lower_bound} and {upper_bound}\n')
                    continue

                num_of_attempts += 1

                if player_guess == secret_number:
                    print('\nCongratulations! You guessed the correct number, '
                          f'{secret_number}, in {num_of_attempts} attempts\n')
                    break
                elif player_guess < secret_number:
                    print('Your guess is too low. Try Again.\n')
                else:
                    print('Your guess is too high. Try Again.\n')
            except ValueError:
                print('\nInvalid Input! Please enter a valid numeric value.\n')

        else:
            print('Sorry, you have reached the maximum number of attempts.')
            print(f'The correct number was {secret_number}.\n')

        # Guess again?
        while True:
            play_again = input(
                'Do you want to play again? Enter (y)es or (n)o:\n> ').lower()
            if play_again.startswith('y'):
                break
            elif play_again.startswith('n'):
                print('Bye!')
                return
            else:
                print('Invalid input. Please enter (y)es or (n)o!')


def get_number_range():
    '''
    Get a valid lower and upper bounds from the player.

    Returns:
        tuple: A tuple containing the lower bound and upper bound as integers.
    '''
    while True:
        try:
            print('\nEnter the integer range of numbers (inclusive):')
            lower_bound = int(input('  Lower Bound: '))
            upper_bound = int(input('  Upper Bound: '))

            if lower_bound >= upper_bound:
                print('Invalid range! Please ensure the lower bound is '
                      'less than the upper bound.\n')
                continue

            return lower_bound, upper_bound
        except ValueError:
            print('Invalid Input! Please enter a valid numeric value.\n')


if __name__ == '__main__':
    main()
