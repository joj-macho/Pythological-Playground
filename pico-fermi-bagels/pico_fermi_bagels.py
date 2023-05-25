import random

# Game Constants
NUM_DIGITS = 3
NUM_GUESSES = 10

def main():
    '''This is the main function'''

    print('''
Pico Fermi Bagels!
Can you guess the 3-digit number...?

Here are the clues:
Pico -- One digit is correct, but in the wrong position.
Fermi --- One digit is correct, and in the right position.
Bagels --- No digit is correct.
    ''')
    while True:
        play_game()
        if not play_again():
            break

def play_game():
    '''This function handles the logic of playing a single game. '''

    secret_number = generate_secret_number()
    print(f'\nI thought of a {NUM_DIGITS}-digit number. Can you guess it?\nYou have {NUM_GUESSES} tries to guess the number correctly!\n')
    # print(secret_number)
    
    number_of_guesses = 1
    while number_of_guesses <= NUM_GUESSES:
        guess = get_valid_guess()
        clues = generate_clues(guess, secret_number)
        print(clues)
        number_of_guesses += 1
        if guess == secret_number:
            print('Congratulations! You guessed the correct number!')
            break
        if number_of_guesses > NUM_GUESSES:
            print(f'You ran out of guesses. The correct answer was {secret_number}')

def generate_secret_number():
    '''This function returns a string of random NUM_DIGITS numbers.'''

    numbers = random.sample('0123456789', NUM_DIGITS)
    return ''.join(numbers)

def get_valid_guess():
    '''This function prompts the user to enter a valid 3-digit number.'''

    while True:
        guess = input(f'Guess: ')
        if len(guess) == NUM_DIGITS and guess.isdecimal():
            return guess
        else:
            print(f'Enter a valid {NUM_DIGITS}-digit number.')

def generate_clues(guess, secret_number):
    '''This function takes the user's guess and the secret number as input and returns a string of clues.'''

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
    '''This functin prompts the user to play again or quit.'''
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

