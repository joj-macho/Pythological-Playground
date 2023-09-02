import random

# Game Constants
NUM_DIGITS = 3
NUM_GUESSES = 10

def main():
    '''Main function to handle the logic of the game.'''

    print('''
Pico Fermi Bagels!
Can you guess the 3-digit number...?

Here are the clues:
Pico -- One digit is correct, but in the wrong position.
Fermi --- One digit is correct, and in the right position.
Bagels --- No digit is correct.
    ''')

    while True:
        # Generate a secret number.
        secret_number = generate_secret_number()
        print(f'\nI thought of a {NUM_DIGITS}-digit number. Can you guess it?\nYou have {NUM_GUESSES} tries to guess the number correctly!\n')
        # print(secret_number)
        
        number_of_guesses = 1
        while number_of_guesses <= NUM_GUESSES:
            # Get a valid guess from the player
            guess = get_valid_guess()

            # Generate clues based on the player's guess and the secret number
            clues = generate_clues(guess, secret_number)
            print(clues)
            number_of_guesses += 1

            # Check if the player guessed the correct number
            if guess == secret_number:
                print('Congratulations! You guessed the correct number!')
                break

            # When you run out of guesses
            if number_of_guesses > NUM_GUESSES:
                print(f'You ran out of guesses. The correct answer was {secret_number}')
                
        if not play_again():
            break


def generate_secret_number():
    '''Generate and return a string of random NUM_DIGITS numbers.'''

    # Generate unique digits
    numbers = random.sample('0123456789', NUM_DIGITS)

    return ''.join(numbers)


def get_valid_guess():
    '''Prompt the user to enter a valid 3-digit number.'''

    while True:
        guess = input(f'Guess: ')
        if len(guess) == NUM_DIGITS and guess.isdecimal():
            return guess
        else:
            print(f'Enter a valid {NUM_DIGITS}-digit number.')


def generate_clues(guess, secret_number):
    '''Generate and return a string of clues based on the user's guess and the secret number.'''

    if guess == secret_number:
        return 'You guessed CORRECTLY!'

    clues = []
    for i in range(NUM_DIGITS):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


def play_again():
    '''Prompt the user to play again or quit.'''

    while True:
        response = input('Do you want to play again? (y)es or (n)o:\n> ').lower()
        if response.startswith('y'):
            return True
        elif response.startswith('n'):
            return False
        else:
            print('Invalid input. Please enter (y)es or (n)o.')


if __name__ == '__main__':
    main()