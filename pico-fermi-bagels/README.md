# Pico Fermi Bagels Game

## Description

The program is a number guessing game called "Pico Fermi Bagels" or simply "Bagels", which generates a random secret number and challenges the player to guess it within a limited number of attempts. It provides feedback through clues (Pico, Fermi, Bagels) to help the player make correct guesses.


## How it Works

- The program begins by importing the `random` module which is used to generate random numbers and make the game more unpredictable and challenging. The program then defines two constants: `NUM_DIGITS`, which represents the number of digits in the secret number, and `NUM_GUESSES`, which determines the maximum number of guesses allowed.

- The `main()` function is defined. This function prints the game instructions and enters a loop that allows the player to play multiple games.

- Inside the `play_game()` function, a new secret number is generated using the `generate_secret_number()` function, which selects `NUM_DIGITS` random digits without repetition.

- The player is informed about the number of digits and the number of guesses they have. The player's guesses are collected using the `get_valid_guess()` function, which prompts the user to enter a valid `NUM_DIGITS`-digit number.

- After each guess, the program calls the `generate_clues()` function, which compares the guess with the secret number and generates clues based on the matching digits. The clues are then displayed to the player.

- The game continues until the player guesses the correct number, runs out of guesses, or decides not to play again. If the player guesses correctly, a congratulatory message is displayed. If the player runs out of guesses, the correct answer is revealed.

- The `play_again()` function prompts the player to choose whether they want to play another game or quit. It validates the input and returns a Boolean value indicating the player's decision.

- The `generateSecretNumber()` function generates a random non-repeating string of NUM_DIGITS numbers using the `random.shuffle()` function.


- The `generateClues()` function takes the user's guess and the secret number as input and returns a string of clues. The function first checks if the guess is correct and returns a message if it is. If the guess is not correct, the function generates clues based on the user's guess. If a digit in the guess is in the correct position, the function adds "Fermi" to the clues list. If a digit in the guess is in the secret number but in the wrong position, the function adds "Pico" to the clues list. If none of the digits in the guess are in the secret number, the function returns "Bagels". The clues are then sorted and returned as a string.


- The `main()` function uses a while loop to keep the game running until the user chooses to quit. In each iteration of the loop, the program prompts the user to guess the secret number and provides clues based on the guess. The loop continues until the user guesses the correct number or runs out of guesses.

- When the game is over, the `main()` function prompts the user to play again or quit. If the user chooses to play again, the while loop in `main()` restarts the game. If the user chooses to quit, the program exits.


## Program Input & Output

When you run `pico_fermi_bagels.py`, the output will look like this:

```
Pico Fermi Bagels!
Can you guess the 3-digit number...?

Here are the clues:
Pico -- One digit is correct, but in the wrong position.
Fermi --- One digit is correct, and in the right position.
Bagels --- No digit is correct.
    

I thought of a 3-digit number. Can you guess it?
You have 10 tries to guess the number correctly!

Guess: 169
Fermi
Guess: 619
Pico
Guess: 187
Fermi Pico Pico
Guess: 817
Pico Pico Pico
Guess: 178
You guessed CORRECTLY!
Congratulations! You guessed the correct number!
Do you want to play again? (y)es or (n)o: 
> y

I thought of a 3-digit number. Can you guess it?
You have 10 tries to guess the number correctly!

Guess: 236
Bagels
Guess: 123
Fermi
Guess: 145
You guessed CORRECTLY!
Congratulations! You guessed the correct number!
Do you want to play again? (y)es or (n)o:
> n
```