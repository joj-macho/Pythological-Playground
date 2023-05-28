# Four In A Row Game

## Description

This program is an implementation of the game "Four in a Row". The game is played by two players taking turns to drop tiles into one of seven columns, trying to make four in a row horizontally, vertically, or diagonally. The program uses a console interface to display the game board and accept player input.

## How it Works

- The program starts by importing a necessary modules, `sys` module, which it uses to exit the program early if so desired. Then the game board is initialized as a nested list, representing the grid of columns and rows.

- The `main()` function orchestrates the game flow and begins by printing a brief description of the game and its objective. The main game loop begins, where players take turns until a win or tie occurs. Here a new game board is created with the `get_new_board()`, and `player_turn` is set to be 'X'.
    - The `get_new_board()` function creates a new game board as a nested list.

- For each turn, the current game board is displayed with the `display_board()` function, and the current player is prompted to enter a column number to drop their tile into by the `ask_for_player_move()` function. The program validates the player's input and checks if the selected column is full. If the input is valid, the program updates the game board with the player's move.
    - The `display_board(board)` displays the current state of the game board on the console.
    - The `ask_for_player_move(player_tile, board)` prompts the current player to enter a column number and validates their input.
    - The `update_board(move, player_tile, board)` updates the game board with the player's move.

- The program checks if the current player has won by checking for four consecutive tiles in a row, column, or diagonal. If a win is detected, the program displays the final game board and declares the current player as the winner. If there is no win but the game board is full, the program declares a tie. The program switches the turn to the other player and continues the loop.
    - The `update_board(move, player_tile, board)` updates the game board with the player's move.
    - The `is_full(board)` checks if the game board is completely filled with tiles.
    - The `is_winner(player_tile, board)` checks if the current player has won the game.

- If the game loop is exited, the program terminates.




- The `main()` function starts the game and runs a loop of the game until either a player wins or there is a tie. It first displays an introduction to the game, creates a new game board with `getNewBoard()`, and sets `playerTurn` to be 'X'. Then, in a loop, it displays the game board with `displayBoard()`, prompts the current player to make a move with `askForPlayerMove()`, updates the game board with the player's move, and checks whether the game has been won or tied with `isWinner()` and `isFull()`. If there is a winner or tie, it displays the final game board and ends the program with `sys.exit()`.


- The `displayBoard(board)` function takes a board dictionary as input and prints a string representation of the game board with ASCII characters. It first creates a list of tile characters by iterating through each position in the board and adding its value to the list. Then, it uses the `format()` string method to insert the tile characters into a template string representing the game board, and prints the resulting string to the console.

- The `askForPlayerMove(playerTile, board)` function takes a player tile ('X' or 'O') and a board dictionary as input and prompts the player to select a column on the board to drop their tile into. It validates the player's input, making sure it is a valid column number and that the column is not already full, and returns the `(columnIndex, rowIndex)` tuple of the position where the player's tile should be placed.

- The `isFull(board)` function takes a board dictionary as input and returns True if the board has no empty spaces, and False otherwise. It iterates through all positions in the board and returns False if it finds an empty space.

- The `isWinner(playerTile, board)` function takes a player tile ('X' or 'O') and a board dictionary as input and returns True if the player has four tiles in a row on the board, and False otherwise. It checks for four-in-a-row horizontally, vertically, and diagonally by iterating through all possible combinations of four tiles in a row and checking whether they all have the same value as `playerTile`.

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
