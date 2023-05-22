# Rock Paper Scissors Game

## Description

This is a classic game of Rock Paper Scissors (also known as jan-ken-pon)! Rock Paper Scissors is a hand game played by two or more players. In this game, participants verbally count "rock, paper, scissors" and simultaneously shape their hands to represent one of three options. The options include a rock (formed by making a fist with your hand), paper (represented by holding your hand with the palm facing downward), or scissors (formed by extending two fingers).

The objective of the game is to anticipate and counter your opponent's move with the appropriate hand shape. Rock beats scissors, scissors beat paper, and paper beats rock. The game is played in rounds, and the winner of each round is determined based on the combination of hand shapes formed by the players.

## How it works

- The program begins by importing the `random`, `time`, and `sys` modules. These modules are used for generating random numbers, introducing delays, and exiting the program, respectively.

- The program then defines three constant variables (`ROCK`, `PAPER`, `SCISSORS`) that store the ASCII art representations of rock, paper, and scissors. The available options for the game (rock, paper, scissors) are stored in a dictionary called `OPTIONS`. Each option is associated with a key ('r' for rock, 'p' for paper, 's' for scissors) and a tuple value containing the name of the option and its corresponding ASCII art.

- The `main()` function is defined. This function begins by printing a welcome message. Then it initializes variables to keep track of the score: `wins`, `losses`, and `ties`.

- The program enters an outer while loop that runs indefinitely until the user chooses to quit the game. Inside the outer loop, there is an inner while loop that prompts the user to enter their move (rock, paper, scissors) or to quit the game.

- The program checks the user's input. If the user chooses to quit by entering 'q', the program prints "Bye!" and exits using `sys.exit()`. If the user enters a valid move ('r', 'p', 's' for rock, paper, scissors), the loop is exited using break.

- After the inner loop, the program determines the player's move based on their input. The player's move is stored in the `player_move `variable, which is retrieved from the `OPTIONS` dictionary based on the user's input. The player's move is displayed by printing the name and ASCII art associated with the chosen option.

- The computer's move is randomly selected from the `OPTIONS` dictionary using `ranom.choice()` function. It assigns the move as a string to the `computer_move` variable. The computer's move is displayed similarly to the player's move.
    - The program introduces a delay of 1 second using `time.sleep()` and then displays the computer's move. Another delay of 0.5 seconds is introduced using `time.sleep()`.

- The program compares the player's move and the computer's move to determine the game result. If the moves are the same, it is a tie. The program prints "A tie!" and increments the ties variable. If the player wins according to the game rules, the program prints "You Win!" and increments the wins variable. If the player loses according to the game rules, the program prints "You Lose" and increments the losses variable. After each round, the updated scores are displayed.

- After displaying the game results, the program goes back to the outer loop and repeats the process until the user chooses to quit.

## Program Input & Output

When you run `rock_paper_scissors.py`, the output will look like this;

![Rock Paper Scissors Results](output/rps-results.gif)