# High and Low Number Guessing Game

## Description

The program you provided is a simple number guessing game.

## How it Works

- First, the program imports the `random` module, which allows for generating random numbers.

- Then the `main()` function is defined. The program begins prints a welcome message and briefly explains the rules of the game. It generates a random secret number using the `random.randint()` function. The secret number is a random integer between 1 and 20. The program prompts the user to guess the number.

- The `main` funcion then enters a loop that gives the user five attempts to guess the number. The loop variable `num_guesses` keeps track of the number of guesses made. Inside the loop, the program informs the user about the number of remaining guesses.

- The user is prompted to enter their guess using the `input()` function. The input is converted to an integer using `int()`.

- The program provides feedback/cluess based on the user's guess. If the guess is lower than the secret number, it informs the user that the guess is too low. If the guess is higher, it informs the user that the guess is too high. If the guess is correct, the loop is exited using the break statement.

- After the loop, the program checks if the guess is equal to the secret number. If it is, the user is notified that they guessed correctly and the number of guesses made is displayed. If the guess is incorrect, the user is informed that they lost and the secret number is revealed.


## Program Input & Output

When you run the program `number_guessing.py`, the output will look like this;

```

Welcome to the Number Guessing Game. Can you guess which number I am thinking of between 1 and 20?

I am thinking of a number between 1 and 20... Can you figure it out?
You have 5 guesses remaining
Enter your guess:
> 20
Your guess is too high.

You have 4 guesses remaining
Enter your guess:
> 10
You guess is too low.

You have 3 guesses remaining
Enter your guess:
> 16
Your guess is too high.

You have 2 guesses remaining
Enter your guess:
> 14
You guess is too low.

You have 1 guesses remaining
Enter your guess:
> 15
Correct! You guessed the secret number in 5 guesses
```
