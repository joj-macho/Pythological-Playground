# Import modules
import random

def main():
    '''This is the main function'''

    print('\nWelcome to the Number Guessing Game. Can you guess which number I am thinking of between 1 and 20?\n')

    # Generate a secret number between 1 and 10
    secret_number = random.randint(1, 20)

    # Prompt the user for to guess the number
    print('I am thinking of a number between 1 and 20... Can you figure it out?')
    for num_guesses in range(1, 6):
        print('You have {} guesses remaining'.format(6 - num_guesses))
        guess = int(input('Enter your guess:\n> '))
        # Generate clues --> Too high or Too low
        if guess < secret_number:
            print('You guess is too low.\n')
        elif guess > secret_number:
            print('Your guess is too high.\n')
        else:
            break
    
    if guess == secret_number:
        print('Correct! You guessed the secret number in {} guesses'.format(num_guesses))
    else:
        print('You lose! The secret number was {}'.format(secret_number))


if __name__ ==  '__main__':
    main()
