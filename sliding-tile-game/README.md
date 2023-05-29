# Sliding Tile Game

## Description

This program is a sliding tile puzzle game implemented in Python. The goal of the game is to rearrange the numbered tiles on a 4x4 board to match the original order. The player can use the WASD keys to move the tiles. The program displays the initial board configuration and prompts the player for moves until the board is solved. Once the player solves the puzzle, a "You won!" message is displayed, and the program exits.

## How it Works

- `main()`: The main function that orchestrates the game flow.
- `generate_new_board()`: Generates a new board configuration representing a solved puzzle state.
- `display_board(board)`: Displays the current board on the screen.
- `find_blank_space(board)`: Finds the position of the blank space on the board.
- `ask_for_player_move(board)`: Asks the player to enter a move (WASD keys) and validates the input.
- `make_move(board, move)`: Moves the tile based on the player's input.
- `make_random_move(board): Performs a random slide in a valid direction.
- `generate_new_puzzle(moves=200)`: Generates a new puzzle by making random slides from the solved state.
- `check_win(board)`: Checks if the given board configuration matches the solved state.

## Program Input & Output

When you run the program `sliding_tile.py`, the output will look like this;

```
```
