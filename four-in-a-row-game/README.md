# Four In A Row Game

## Description

The "Four In A Row" program is an interactive console-based implementation of the classic game "Connect Four". In this two-player game, participants take turns dropping their tiles into one of seven columns with the objective of forming a sequence of four of their tiles either horizontally, vertically, or diagonally within the game grid.

## How it Works

- The program starts by importing the `sys` module, which it uses to exit the program early if so desired. Then the game board is initialized as a nested list, representing the grid of columns and rows.

- The `main()` function controls the game flow and begins by printing a brief description of the game. Then the main game loop begins, where players take turns until a win or tie occurs. Here a new game board is created with the `get_new_board()`, and `player_turn` is set to be 'X'.
    - The `get_new_board()` function creates a new game board as a nested list with empty spaces.

- For each turn, the current game board is displayed with the `display_board()` function, and the current player is prompted to enter a column number to drop their tile into by the `ask_for_player_move()` function. The program validates the player's input and checks if the selected column is full. If the input is valid, the program updates the game board with the player's move.
    - The `display_board()` function displays the current state of the game board on the console.
    - The `ask_for_player_move()` function prompts the current player to enter a column number and validates their input.
    - The `update_board()` function updates the game board with the player's move.

- The program checks if the current player has won by checking for four consecutive tiles in a row, column, or diagonal. If a win is detected, the program displays the final game board and declares the current player as the winner. If there is no win but the game board is full, the program declares a tie. The program switches the turn to the other player and continues the loop.
    - The `update_board()` function updates the game board with the player's move.
    - The `is_full()` function checks if the game board is completely filled with tiles.
    - The `is_winner()` function checks if the current player has won the game.

- If the game loop is exited, the program terminates.



## Program Input & Output

When you run `four_in_a_row.py`, the output will look like this;

```
Four in a Row,

Two players take turns dropping tiles into one of seven columns, trying to make four in a row horizontally, vertically, or diagonally.


 1 2 3 4 5 6 7
+ - - - - - - - +
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
+ - - - - - - - +
Player X, enter a column or (q)uit:
> 2

 1 2 3 4 5 6 7
+ - - - - - - - +
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . X . . . . . |
+ - - - - - - - +
Player O, enter a column or (q)uit:
> 1

 1 2 3 4 5 6 7
+ - - - - - - - +
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| O X . . . . . |
+ - - - - - - - +
Player X, enter a column or (q)uit:
> 3

 1 2 3 4 5 6 7
+ - - - - - - - +
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| O X X . . . . |
+ - - - - - - - +
Player O, enter a column or (q)uit:
> 4

 1 2 3 4 5 6 7
+ - - - - - - - +
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| O X X O . . . |
+ - - - - - - - +
Player X, enter a column or (q)uit:
> 2

 1 2 3 4 5 6 7
+ - - - - - - - +
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . X . . . . . |
| O X X O . . . |
+ - - - - - - - +
Player O, enter a column or (q)uit:
> 1

 1 2 3 4 5 6 7
+ - - - - - - - +
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| O X . . . . . |
| O X X O . . . |
+ - - - - - - - +
Player X, enter a column or (q)uit:
> 2

 1 2 3 4 5 6 7
+ - - - - - - - +
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| . X . . . . . |
| O X . . . . . |
| O X X O . . . |
+ - - - - - - - +
Player O, enter a column or (q)uit:
> 1

 1 2 3 4 5 6 7
+ - - - - - - - +
| . . . . . . . |
| . . . . . . . |
| . . . . . . . |
| O X . . . . . |
| O X . . . . . |
| O X X O . . . |
+ - - - - - - - +
Player X, enter a column or (q)uit:
> 2

 1 2 3 4 5 6 7
+ - - - - - - - +
| . . . . . . . |
| . . . . . . . |
| . X . . . . . |
| O X . . . . . |
| O X . . . . . |
| O X X O . . . |
+ - - - - - - - +
Player X has won!
```
