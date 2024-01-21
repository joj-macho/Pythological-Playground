# Number Guessing Game

## Description

Welcome to the Number Guessing Game! This simple Python program challenges you to guess a secret number within a specified range.

## How it Works

- The program begins by importing the `random` module, which allows the generation of random numbers.

- The `number_guessing_game()` function is initiated, presenting a welcome message and explaining the game rules. The program enters a loop, prompting the user to input the lower and upper bounds for the range of numbers. This loop ensures a valid range is provided, with the program guiding the user to correct any input errors.

- Once the range is set, the program utilizes the `random` module to generate a random secret number within that specified range.

- The program initiates a loop, offering the user 5 attempts to guess the secret number. The loop variable `attempts` keeps track of the number of guesses made, providing the user with feedback on the remaining attempts.

- The user inputs their guess, and the program evaluates the guess, providing immediate feedback. If the guess is incorrect, the program guides the user to adjust their guess based on whether it's too low or too high. If the guess is correct, the loop is exited using the `break` statement.

- After the loop, the program checks if the guess is equal to the secret number. If correct, the user is congratulated on their success, and the number of attempts is displayed. If incorrect, the user is informed of their loss, and the secret number is revealed.


## Program Input & Output

When you run the program `number_guessing.py`, the output will look like this;

```

Welcome to the Number Guessing Game!

Enter the range of numbers:
   Lower bound: 0
   Upper bound: 100

I'm thinking of a number between 0 and 100. Can you guess it?

Enter your guess: 10
Your Guess is Too Low! Try Again.

Enter your guess: 100
Your Guess is Too High! Try Again.

Enter your guess: 43
Your Guess is Too Low! Try Again.

Enter your guess: 45
Your Guess is Too High! Try Again.

Enter your guess: 49
Your Guess is Too High! Try Again.

Sorry, you've reached the maximum attempts. The correct number was 44.

.
.
.

Welcome to the Number Guessing Game!

Enter the range of numbers:
   Lower bound: 0.5
Invalid input. Please enter valid numeric values!

Enter the range of numbers:
   Lower bound: 1
   Upper bound: 20

I'm thinking of a number between 1 and 20. Can you guess it?

Enter your guess: 4
Your Guess is Too Low! Try Again.

Enter your guess: 6
Your Guess is Too High! Try Again.

Enter your guess: 5

Congratulations! You guessed the correct number 5 in 3 attempts.
```
