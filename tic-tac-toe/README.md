## Description

This program is a command-line implementation of the classic Tic-Tac-Toe game.

## How it Works

- First, the program defines some constants; `ALL_SPACES` is a list containing all the possible spaces on the Tic-Tac-Toe board. `X`, `O`, and `BLANK` represent the player marks for X, O, and empty spaces, respectively. The program also defines a dictionary called `WINNING_COMBINATIONS`, which contains all the possible winning combinations in the Tic-Tac-Toe game. Each key represents a specific combination (e.g., 'across_top', 'diagonal'), and the corresponding value is a list of spaces that form that combination.

- The `main` function is defined, inside the `main` function, the program displays a welcome message. Then the `generate_new_board` function is called to create a new blank Tic-Tac-Toe board. It returns a dictionary where each space is initially set to `BLANK`. The `current_player` variable is set to `X`, indicating that X will be the first player to make a move.

- The main game loop begins with a `while True` loop, which continues until the game is won or tied.

- The `generate_board_string` function is called to generate a string representation of the current state of the board. It displays the board's layout and the marks in each space.

- The program prompts the current player to enter their move by calling input and displaying a message. The program then validates the input using a nested while loop until a valid move is entered. The `is_valid_space` function is called to check if the entered move is a valid and empty space on the board. The `update_board` function is called to update the board with the current player's mark in the chosen space.

- The program checks if the current player has won the game by calling the `is_winner` function. It checks if any of the winning combinations have been filled with the current player's mark.

- If the current player is the winner, the program displays the final state of the board, declares the player as the winner, and breaks out of the loop.

- If the board is full and there is no winner, the program calls the `is_board_full` function to check if the game is a tie. If so, it displays the final state of the board and declares a tie before breaking out of the loop.

- If the game is still ongoing, the program calls the `switch_player` function to switch the current player between X and O.

- The loop continues to the next iteration, and the game proceeds with the next player's turn. After the loop ends, the program displays a goodbye message, indicating the end of the game.


## Program Input & Output

When you run the program `tic_tac_toe.py`, the output will look like this;

```

Welcome to Tic-Tac-Toe.


       | |   1 2 3
      -+-+-
       | |   4 5 6
      -+-+-
       | |   7 8 9
What is your move X? > 5

       | |   1 2 3
      -+-+-
       |X|   4 5 6
      -+-+-
       | |   7 8 9
What is your move O? > 9

       | |   1 2 3
      -+-+-
       |X|   4 5 6
      -+-+-
       | |O  7 8 9
What is your move X? > 3

       | |X  1 2 3
      -+-+-
       |X|   4 5 6
      -+-+-
       | |O  7 8 9
What is your move O? > 7

       | |X  1 2 3
      -+-+-
       |X|   4 5 6
      -+-+-
      O| |O  7 8 9
What is your move X? > 8

       | |X  1 2 3
      -+-+-
       |X|   4 5 6
      -+-+-
      O|X|O  7 8 9
What is your move O? > 6

       | |X  1 2 3
      -+-+-
       |X|O  4 5 6
      -+-+-
      O|X|O  7 8 9
What is your move X? > 2

       |X|X  1 2 3
      -+-+-
       |X|O  4 5 6
      -+-+-
      O|X|O  7 8 9
X won the game.
Bye.
```
