# Tic-Tac-Toe Game

## Description

This program is an implementation of the classic Tic-Tac-Toe game. It follows the traditional rules of the game, where two players take turns marking spaces on a 3x3 grid. 

## How it Works

- Take turns between Player 1 (`X`) and Player 2 (`O`).

## Running the Program

```bash
# Navigate to the project directory
cd tic-tac-toe

# Run the main script
python3 tic_tac_toe.py
```

## Program Input & Output

When you run the program `tic_tac_toe.py`, the output will look like this;

```
Tic Tac Toe Game.

Current board:
   |   |      1 2 3
---+---+---
   |   |      4 5 6
---+---+---
   |   |      7 8 9

Player O will start.
Player O's turn.
Enter your move (1-9): 5
(1, 1)

Current board:
   |   |      1 2 3
---+---+---
   | O |      4 5 6
---+---+---
   |   |      7 8 9

Player X's turn.
Enter your move (1-9): 1
(0, 0)

Current board:
 X |   |      1 2 3
---+---+---
   | O |      4 5 6
---+---+---
   |   |      7 8 9

Player O's turn.
Enter your move (1-9): 7
(2, 0)

Current board:
 X |   |      1 2 3
---+---+---
   | O |      4 5 6
---+---+---
 O |   |      7 8 9

Player X's turn.
Enter your move (1-9): .
Invalid input. Please enter a number between 1 and 9.
Enter your move (1-9): 3
(0, 2)

Current board:
 X |   | X    1 2 3
---+---+---
   | O |      4 5 6
---+---+---
 O |   |      7 8 9

Player O's turn.
Enter your move (1-9): 2
(0, 1)

Current board:
 X | O | X    1 2 3
---+---+---
   | O |      4 5 6
---+---+---
 O |   |      7 8 9

Player X's turn.
Enter your move (1-9): 8
(2, 1)

Current board:
 X | O | X    1 2 3
---+---+---
   | O |      4 5 6
---+---+---
 O | X |      7 8 9

Player O's turn.
Enter your move (1-9): 4
(1, 0)

Current board:
 X | O | X    1 2 3
---+---+---
 O | O |      4 5 6
---+---+---
 O | X |      7 8 9

Player X's turn.
Enter your move (1-9): 6
(1, 2)

Current board:
 X | O | X    1 2 3
---+---+---
 O | O | X    4 5 6
---+---+---
 O | X |      7 8 9

Player O's turn.
Enter your move (1-9): 9
(2, 2)

Current board:
 X | O | X    1 2 3
---+---+---
 O | O | X    4 5 6
---+---+---
 O | X | O    7 8 9

The game is a draw!
Scores: Player X: 0 | Player O: 0
Do you want to play again? (yes or no): y

Current board:
   |   |      1 2 3
---+---+---
   |   |      4 5 6
---+---+---
   |   |      7 8 9

Player X will start.
Player X's turn.
Enter your move (1-9): 5
(1, 1)

Current board:
   |   |      1 2 3
---+---+---
   | X |      4 5 6
---+---+---
   |   |      7 8 9

Player O's turn.
Enter your move (1-9): 0
Invalid move. Please enter a number between 1 and 9.
Enter your move (1-9): 1
(0, 0)

Current board:
 O |   |      1 2 3
---+---+---
   | X |      4 5 6
---+---+---
   |   |      7 8 9

Player X's turn.
Enter your move (1-9): 2
(0, 1)

Current board:
 O | X |      1 2 3
---+---+---
   | X |      4 5 6
---+---+---
   |   |      7 8 9

Player O's turn.
Enter your move (1-9): 3
(0, 2)

Current board:
 O | X | O    1 2 3
---+---+---
   | X |      4 5 6
---+---+---
   |   |      7 8 9

Player X's turn.
Enter your move (1-9): 8
(2, 1)

Current board:
 O | X | O    1 2 3
---+---+---
   | X |      4 5 6
---+---+---
   | X |      7 8 9

Player X wins!
Scores: Player X: 1 | Player O: 0
Do you want to play again? (yes or no): n
Bye!
```
