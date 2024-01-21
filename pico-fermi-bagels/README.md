# Pico Fermi Bagels Game

## Description

The program is a number guessing game called "Pico Fermi Bagels" or simply "Bagels". This Python program challenges you to guess a secret three-digit number with no repeated digits, within a limited number of attempts. The game provides clues (Pico, Fermi, Bagels) to help you make correct guesses.

## How it Works

- The program begins by importing the `random` module which is used to generate random numbers.

- The `main()` function starts by printing the game instructions and enters a loop that allows the player to play multiple games. Inside this game loop, a new secret number is generated for each round using the `generate_secret_number()` function, which selects 3 random digits without repetition.

- The player is informed about the number of digits and the number of guesses they have. The player's guesses are collected using the `get_user_guess()` function, which prompts the user to enter a valid 3-digit number.

- The program checks if the guess is correct. If correct, the user is congratulated on their success, and the number of attempts is displayed. If incorrect, the program generates clues using the `generate_clues()` function, guiding the user toward the correct answer.

- If the user reaches the maximum allowed attempts, the correct number is revealed, and the game ends for that round.

- After each round, the user is given the option to play again. If the user chooses to play again, a new round starts with a new secret number. If they choose not to play again, the program exits.

## Program Input & Output

When you run `pico_fermi_bagels.py`, the output will look like this:

```

Welcome To The Pico Fermi Bagels Game!

Your challenge is to guess the secret three-digit number with no repeated digits.

Here are the clues:
    - Pico: One digit is correct but in the wrong position.
    - Fermi: One digit is correct and in the right position.
    - Bagels: No digit is correct.

Press Enter to start the game...

I've chosen a three-digit number. Can you guess it?
You have 10 attempts to guess the number correctly!

Enter your guess: 123
Fermi Pico Pico
Enter your guess: 231
Fermi Pico Pico
Enter your guess: 132

Congratulations! You guessed the correct number 132 in 3 attempts.

Do you want to play again? (y)es or (n)o: y
716

I've chosen a three-digit number. Can you guess it?
You have 10 attempts to guess the number correctly!

Enter your guess: 12

Invalid Input. Please enter a valid three-digit integer number with no repeated digits.

Enter your guess: 123
Pico
Enter your guess: 145
Pico
Enter your guess: 167
Pico Pico Pico
Enter your guess: 176
Fermi Pico Pico
Enter your guess: 716

Congratulations! You guessed the correct number 716 in 5 attempts.

Do you want to play again? (y)es or (n)o: y
496

I've chosen a three-digit number. Can you guess it?
You have 10 attempts to guess the number correctly!

Enter your guess: 12e

Invalid Input. Please enter a valid three-digit integer number with no repeated digits.

Enter your guess: dad

Invalid Input. Please enter a valid three-digit integer number with no repeated digits.

Enter your guess: 496

Congratulations! You guessed the correct number 496 in 1 attempts.

Do you want to play again? (y)es or (n)o: n
Bye!
```