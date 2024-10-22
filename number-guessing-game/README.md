# Number Guessing Game

## Description

The "Number Guessing Game" is a simple game where the player tries to guess a randomly selected secret number within a specified range. The player receives clues after each guess to help them adjust their next guess and narrow down the possibilities.

## How It Works

In the Number Guessing Game:
- Start by entering the lower and upper bounds for the range of the secret number.
- The game randomly selects a secret number within this specified range (inclusive).
- Guess the secret number
- After each guess, the following clues will be provided:
   - "Too low!" if the guess is less than the secret number.
   - "Too high!" if the guess is greater than the secret number.
   - "Correct!" if the guess matches the secret number.
- Continue guessing until you correctly guess the secret number.

## Running the Program

```bash
# Navigate to the project directory
cd number-guessing-game/

# Run the main script
python3 number_guessing.py
```

## Program Input & Output

When you run the program `number_guessing.py`, the output will look like this;

```

Welcome to the Number Guessing Game!

Here's how to play:

- Enter the lower and upper bounds for the range of the secret number.
- Guess the secret number.
- After each guess, you will receive clues:
   - "Too low!" if your guess is less than the secret number.
   - "Too high!" if your guess is greater than the secret number.
   - "Correct!" if your guess matches the secret number.

Press Enter to start guessing...

Enter the integer range of numbers (inclusive):
  Lower Bound: 0
  Upper Bound: 50

I am thinking of a number between [0, 50].
Can you guess it?
You have 5 attempts to guess it.

Attempt #1
Enter your guess:
> 1
Your guess is too low. Try Again.

Attempt #2
Enter your guess:
> 50
Your guess is too high. Try Again.

Attempt #3
Enter your guess:
> 2o

Invalid Input! Please enter a valid numeric value.

Attempt #3
Enter your guess:
> 55
Your guess is out of bounds! Please enter a number between 0 and 50

Attempt #3
Enter your guess:
> 37
Your guess is too high. Try Again.

Attempt #4
Enter your guess:
> 15
Your guess is too high. Try Again.

Attempt #5
Enter your guess:
> 20
Your guess is too high. Try Again.

Sorry, you have reached the maximum number of attempts.
The correct number was 6.

Do you want to play again? Enter (y)es or (n)o:
> y

Enter the integer range of numbers (inclusive):
  Lower Bound: 0
  Upper Bound: 20

I am thinking of a number between [0, 20].
Can you guess it?
You have 5 attempts to guess it.

Attempt #1
Enter your guess:
> 10
Your guess is too low. Try Again.

Attempt #2
Enter your guess:
> 16

Congratulations! You guessed the correct number, 16, in 2 attempts

Do you want to play again? Enter (y)es or (n)o:
> n
Bye!
```
