# Pico Fermi Bagels Game

## Description

The program is a number guessing game called "Pico Fermi Bagels" or simply "Bagels", which generates a random secret number and challenges the player to guess it within a limited number of attempts. It provides feedback through clues (Pico, Fermi, Bagels) to help the player make correct guesses.


## How it Works

- The program begins by importing the `random` module which is used to generate random numbers and make the game more unpredictable and challenging. The program then defines two constants: `NUM_DIGITS`, which represents the number of digits in the secret number, and `NUM_GUESSES`, which determines the maximum number of guesses allowed.

- The `main()` function starts by printing the game instructions and enters a loop that allows the player to play multiple games. A new secret number is generated using the `generate_secret_number()` function, which selects `NUM_DIGITS` random digits without repetition.

- The player is informed about the number of digits and the number of guesses they have. The player's guesses are collected using the `get_valid_guess()` function, which prompts the user to enter a valid `NUM_DIGITS`-digit number.

- After each guess, the program calls the `generate_clues()` function, which compares the guess with the secret number and generates clues based on the matching digits. The clues are then displayed to the player.

- The game continues until the player guesses the correct number, runs out of guesses, or decides not to play again. If the player guesses correctly, a congratulatory message is displayed. If the player runs out of guesses, the correct answer is revealed.

- The `play_again()` function prompts the player to choose whether they want to play another game or quit. It validates the input and returns a Boolean value indicating the player's decision.


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