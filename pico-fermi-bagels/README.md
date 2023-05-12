# Pico Fermi Bagels Game

## Description

<p>Pico-Fermi-Bagels is a game where the player must guess a secret three-digit number based on clues. After each guess of the player, the computer answers <strong>fermi</strong> (one digit is at the right position), <strong>pico</strong> (one digit is in the code but on a different position), or <strong>bagels</strong> (none of the digits are correct). The goal is to guess the number in as few tries as possible, so players must use the answers to infer the right code. In this game, players will be given 10 tries to guess the secret number.</p>

## How it Works

- First the program defines two constants: `NUM_DIGITS`, which specifies the number of digits in the secret number, and `NUM_GUESSES`, which specifies the number of guesses the user has to correctly guess the number.

- The `main()` function is defined. This function prints the game instructions and prompts the user to enter a valid 3-digit number for each guess. It then calls two other functions, `generateSecretNumber()` and `generateClues()`, to generate the secret number and provide clues based on the user's guess.

- The `generateSecretNumber()` function generates a random non-repeating string of NUM_DIGITS numbers using the `random.shuffle()` function.

```python
def generateSecretNumber():
    '''This function returns a string of random {NUM_DIGIT}numbers.'''

    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNumber = ''
    for i in range(NUM_DIGITS):
        secretNumber += str(numbers[i])

    return secretNumber
```

- The `generateClues()` function takes the user's guess and the secret number as input and returns a string of clues. The function first checks if the guess is correct and returns a message if it is. If the guess is not correct, the function generates clues based on the user's guess. If a digit in the guess is in the correct position, the function adds "Fermi" to the clues list. If a digit in the guess is in the secret number but in the wrong position, the function adds "Pico" to the clues list. If none of the digits in the guess are in the secret number, the function returns "Bagels". The clues are then sorted and returned as a string.

```python
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
```

- The `main()` function uses a while loop to keep the game running until the user chooses to quit. In each iteration of the loop, the program prompts the user to guess the secret number and provides clues based on the guess. The loop continues until the user guesses the correct number or runs out of guesses.

- When the game is over, the `main()` function prompts the user to play again or quit. If the user chooses to play again, the while loop in `main()` restarts the game. If the user chooses to quit, the program exits.


## Program Input & Output

When you run `picoFermiBagels.py`, the output will look like this:

```
Pico Fermi Bagels!
Can you guess the 3-digit number...?

Here are the clues:
Pico -- One digit is correct, but in the wrong position.
Fermi --- One digit is correct, and in the right position.
Bagels --- No digit is correct.
    
105

I thought of a 3-digit number. Can you guess it?
You have 10 tries to guess the number correctly!

Enter a valid 3-digit number.
Guess #1:
> 012
Pico Pico
Enter a valid 3-digit number.
Guess #2:
> 013
Pico Pico
Enter a valid 3-digit number.
Guess #3:
> 014
Pico Pico
Enter a valid 3-digit number.
Guess #4:
> o15
Enter a valid 3-digit number.
Guess #4:
> 015
Fermi Pico Pico
Enter a valid 3-digit number.
Guess #5:
> 051
Pico Pico Pico
Enter a valid 3-digit number.
Guess #6:
> 510
Pico Pico Pico
Enter a valid 3-digit number.
Guess #7:
> 105
You guessed CORRECTLY!
Do want to Play Again? Enter (y)es or (n)o.
> n
```