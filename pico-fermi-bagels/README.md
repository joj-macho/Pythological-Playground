# Pico Fermi Bagels Game

## Description

The "Pico Fermi Bagels" game is a number guessing game where the player attempts to guess a secret number composed of unique digits. After each guess, the player receives feedback, clues indicating how close their guess is to the secret number.

## How It Works

In this game, the secret number consists of a specified number of unique digits, `NUM_DIGITS`. The player makes guesses to determine the secret number. After each guess, the program provides the following:

- **Fermi**: A digit in the guess is correct and in the correct position.
- **Pico**: A digit in the guess is correct but in the wrong position.
- **Bagels**: No digit in the guess is correct.

Use these clues to make informed guesses and continues to guess until either correctly guess the secret number or run out of attempts, `MAX_ATTEMPTS`.

## Running the Program

```bash
# Navigate to the project directory
cd pico-fermi-bagels

# Run the main script
python3 pico_fermi_bagels.py
```

## Program Input & Output

When you run `pico_fermi_bagels.py`, the output will look like this:

```

Welcome to the Pico Fermi Bagels Game!

Your challenge is to guess the secret 3-digit number with no
repeating digits.

Here are the clues to guide you to the solution:
  - Fermi: One digit is correct and in the right position.
  - Pico: One digit is correct but in the wrong position.
  - Bagels: No digit is correct.

Press Enter to start the game...

I have chosen a 3-digit random number.
Can you guess it?
You have 10 attempts to guess the number correctly.

Attempt #1
Enter your guess:
> 135
Bagels

Attempt #2
Enter your guess:
> 123
Pico

Attempt #3
Enter your guess:
> 213
Fermi

Attempt #4
Enter your guess:
> 420
Pico Pico Pico

Attempt #5
Enter your guess:
> 240
Fermi Pico Pico

Attempt #6
Enter your guess:
> 204

Congratulations! You guessed the correct number 204 in 6 attempts.

Do you want to play again? Enter (y)es or (n)o:
> y

I have chosen a 3-digit random number.
Can you guess it?
You have 10 attempts to guess the number correctly.

Attempt #1
Enter your guess:
> 1234
You guess must be exactly 3 digits long.

Enter your guess:
> 1o4
Your guess must only contain numeric digits.

Enter your guess:
> 112
All digits in you guess must be unique.

Enter your guess:
> 032

Congratulations! You guessed the correct number 032 in 1 attempts.

Do you want to play again? Enter (y)es or (n)o:
> n
Thanks for playing! Goodbye!
```