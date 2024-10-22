import random

MAX_ATTEMPTS = 10  # Max number of attempts for each game
NUM_DIGITS = 3  # Number of digits of the secret numner


def main():
    '''Run and play the Pico Fermi Balges Game.'''
    print(f'''
Welcome to the Pico Fermi Bagels Game!

Your challenge is to guess the secret {NUM_DIGITS}-digit number with no
repeating digits.

Here are the clues to guide you to the solution:
  - Fermi: One digit is correct and in the right position.
  - Pico: One digit is correct but in the wrong position.
  - Bagels: No digit is correct.
''')

    input('Press Enter to start the game...')

    while True:
        secret_number = generate_secret_number()
        # Uncomment for debugging to see secret number
        # print('\nMy secret number:', secret_number)

        num_of_attempts = 0

        print(f'\nI have chosen a {NUM_DIGITS}-digit random number.')
        print('Can you guess it?')
        print(f'You have {MAX_ATTEMPTS} attempts to guess the number '
              'correctly.\n')

        while num_of_attempts < MAX_ATTEMPTS:
            print(f'Attempt #{num_of_attempts + 1}')
            player_guess = get_player_guess()
            num_of_attempts += 1

            if player_guess == secret_number:
                print(f'\nCongratulations! You guessed the correct number '
                      f'{secret_number} in {num_of_attempts} attempts.\n')
                break
            else:
                clues = generate_clues(player_guess, secret_number)
                print(clues)
                print()

        else:
            print('Sorry, you have reached the maximum number of attempts.')
            print(f'The correct number was {secret_number}.\n')

        # Play again?
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


def generate_secret_number():
    '''
    Generate a random N-digit secret number with no repeating digits.

    Returns:
        str: Random and unique secret number of length NUM_DIGITS.
    '''
    n_digit_unique_number = random.sample('0123456789', NUM_DIGITS)
    secret_number = ''.join(n_digit_unique_number)

    return secret_number


def get_player_guess():
    '''Get a valid N-digit guess from the user.

    Returns:
        str: Valid guess of length NUM_DIGITS
    '''
    while True:
        try:
            guess = input('Enter your guess:\n> ')
            if len(guess) != NUM_DIGITS:
                print(f'You guess must be exactly {NUM_DIGITS} digits long.\n')
                continue
            if not guess.isdecimal():
                print('Your guess must only contain numeric digits.\n')
                continue
            if len(set(guess)) != NUM_DIGITS:
                print('All digits in you guess must be unique.\n')
                continue
            return guess
        except Exception as e:
            print(f'Error: {e}\n')


def generate_clues(guess, secret_number):
    '''
    Generate cluess based on the player guess.

    Parameters:
        guess (str): THe player's guess.
        secret_number (str): The secret number to be guessed.

    Returns:
        str: A string containing clues ('Fermi', 'Pico', 'Bagels') based on
        the guess.
    '''
    clues = []
    for i in range(len(guess)):
        # Correct digit in the correct place
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        # Correct digit but in the wrong place
        elif guess[i] in secret_number:
            clues.append('Pico')

    # If no clues, then no correct digit, Bagels
    if not clues:
        clues.append('Bagels')
    else:
        clues.sort()

    return ' '.join(clues)


if __name__ == '__main__':
    main()
