import random

# Game Constants
NUM_DIGITS = 3
NUM_GUESSES = 10

def main():
    print('''
Pico Fermi Bagels!
Can you guess the 3-digit number...?

Here are the clues:
Pico -- One digit is correct, but in the wrong position.
Fermi --- One digit is correct, and in the right position.
Bagels --- No digit is correct.
    ''')

    # Main game
    while True:
        # Generate secret number
        secretNumber = generateSecretNumber()

        print(f'\nI thought of a {NUM_DIGITS}-digit number. Can you guess it?\nYou have {NUM_GUESSES} tries to guess the number correctly!\n')
        guessNumber = 1
        while guessNumber <= NUM_GUESSES:
            guess = ''
            # Prompt the user to enter a valid 3-digit number
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Enter a valid {NUM_DIGITS}-digit number.')
                guess = input(f'Guess #{guessNumber}:\n> ')

            # Genrate Clues
            clues = generateClues(guess, secretNumber)
            print(clues)
            guessNumber += 1
            # Break when out of guesses or when correct guess is made
            if guess == secretNumber:
                break
            if guessNumber > NUM_GUESSES:
                print(f'You ran out of guesses.\nThe correct answer was {secretNumber}')
        # Game Over
        print('Do want to Play Again? Enter (y)es or (n)o.')
        if input('> ').lower().startswith('n'):
            break
            
def generateSecretNumber():
    '''This function returns a string of random {NUM_DIGIT}numbers.'''
    # Generate random non-repeating numbers
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNumber = ''
    for i in range(NUM_DIGITS):
        secretNumber += str(numbers[i])

    return secretNumber

def generateClues(guess, secretNumber):
    '''This function takes the user's guess and the secret number as input and returns a string of clues.'''
    if guess == secretNumber:
        return 'You guessed CORRECTLY!'
    # Store clues in list
    clues = []
    for i in range(len(guess)):
        # One digit correct and in the right position.
        if guess[i] == secretNumber[i]:
            clues.append('Fermi')
        # One digit correct and in the wrong position.
        elif guess[i] in secretNumber:
            clues.append('Pico')
    # One digit correct and in the wrong position.
    if len(clues) == 0:
        return 'Bagels'
    # Make the game a bit hard
    else:
        clues.sort()

        return ' '.join(clues)
        

if __name__ == '__main__':
    main()