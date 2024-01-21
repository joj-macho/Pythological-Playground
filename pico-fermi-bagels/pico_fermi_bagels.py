import random

def main():
    '''Main function to play the Bagels game.'''

    print('''
Welcome To The Pico Fermi Bagels Game!

Your challenge is to guess the secret three-digit number with no repeated digits.

Here are the clues:
    - Pico: One digit is correct but in the wrong position.
    - Fermi: One digit is correct and in the right position.
    - Bagels: No digit is correct.
''')

    input('Press Enter to start the game...')

    while True:
        secret_number = generate_secret_number()
        # print(secret_number)  # Uncomment for debugging to see the secret number

        attempts = 0
        max_attempts = 10

        print(f'\nI\'ve chosen a three-digit number. Can you guess it?\nYou have {max_attempts} attempts to guess the number correctly!\n')

        while attempts < max_attempts:
            guess = get_user_guess()
            attempts += 1

            if guess == secret_number:
                print(f'\nCongratulations! You guessed the correct number {secret_number} in {attempts} attempts.\n')
                break
            else:
                clues = generate_clues(guess, secret_number)
                print(clues)

        else:
            print(f'\nSorry, you\'ve reached the maximum attempts. The correct number was {secret_number}.\n')

        play_again = input('Do you want to play again? (y)es or (n)o: ').lower()
        if play_again.startswith('y'):
            continue
        else:
            print('Bye!')
            break

def generate_secret_number():
    '''Generate a secret three-digit number with no repeated digits.'''
    numbers = random.sample('0123456789', 3)
    return ''.join(numbers)

def get_user_guess():
    '''Get a three-digit number guess from the player.'''
    while True:
        try:
            guess = input('Enter your guess: ')
            if len(guess) == 3 and guess.isdecimal():
                return guess
            else:
                print('\nInvalid Input. Please enter a valid three-digit integer number with no repeated digits.\n')
        except ValueError:
            print('\nInvalid input. Please enter a valid three-digit integer number with no repeated digits.\n')

def generate_clues(guess, secret_number):
    '''Generate clues based on the user guess.'''
    clues = []
    for i in range(3):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')
    
    if not clues:
        clues.append('Bagels')
    else:
        clues.sort()
    return ' '.join(clues)

if __name__ == '__main__':
    main()