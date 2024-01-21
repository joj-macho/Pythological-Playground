import random

def number_guessing_game():
    '''Implement and play the Number Guessing Game'''
    print('\nWelcome to the Number Guessing Game!\n')

    # Get user input for the range of numbers
    while True:
        try:
            print('Enter the range of numbers:')
            lower_bound = int(input('   Lower bound: '))
            upper_bound = int(input('   Upper bound: '))

            # Validate the range
            if lower_bound >= upper_bound:
                print('Invalid range. Please ensure that the lower bound is less than the upper bound!\n')
                continue
            break
        except ValueError:
            print('Invalid input. Please enter valid numeric values!\n')

    print(f'\nI\'m thinking of a number between {lower_bound} and {upper_bound}. Can you guess it?\n')

    # Generate random secret number
    secret_number = random.randint(lower_bound, upper_bound)
    print(secret_number)  # For debugging

    attempts = 0      # For score keeping
    max_attempts = 5  # Set max number of attemps

    while attempts < max_attempts:
        try:
            # Ask the player for guess
            player_guess = int(input('Enter your guess: '))

            # Check if guess is correct 
            if player_guess == secret_number:
                print(f'\nCongratulations! You guessed the correct number {secret_number} in {attempts + 1} attempts.')
                break
            elif player_guess < secret_number:
                print('Your Guess is Too Low! Try Again.\n')
            else:
                print('Your Guess is Too High! Try Again.\n')

            attempts += 1
        except ValueError:
            print('\nInvalid input. Please enter a valid number.\n')

    else:
        print(f'Sorry, you\'ve reached the maximum attempts. The correct number was {secret_number}.')

if __name__ == '__main__':
    number_guessing_game()