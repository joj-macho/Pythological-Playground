# Four In A Row Game

## Description

The "Four In A Row" program is an implementation of the classic game "Connect Four". In this two-player game, participants take turns dropping their tiles into one of seven columns with the objective of forming a sequence of four of their tiles either horizontally, vertically, or diagonally within the game grid.

## How it Works

- Play the game and see for yourself

## Running the Program

```bash
# Navigate to the project directory
cd four-in-a-row-game

# Run the main script
python3 four_in_a_row.py
```

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
