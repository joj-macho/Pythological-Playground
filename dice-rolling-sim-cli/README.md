# Dice Rolling Simulator

## Description

The program is a Dice Rolling Simulator that simulates rolling a dice or multiple dice and displays the corresponding ASCII characters of the rolled die.

## How it works

- The program defines a dictionary called `DICE_FACES` which stores the ASCII art representation of each possible face of a die, with the key being the number on the face of the die. The program also defines a constant called `DICE_HEIGHT`, which represents the number of rows in the ASCII art representation of a die face.

- The `main()` function prints a header for the program and then prompts the user to enter the number of dice they want to roll. It keeps prompting the user until a valid input (a number between 1 and 6) is provided. Once a valid input is received, the program rolls the dice using the `random.randint()` function, which generates a random integer between 1 and 6, inclusive, for each die. The results are stored in the `dice_roll_result` list.
- Next the `main()` function simply calls the `generate_dice_faces()` function to generate the ASCII characters of the rolled dice and displays the results to the user.

- The `generate_dice_faces()` function takes the list of dice roll results as a parameter and returns a string containing the corresponding ASCII characters of the rolled dice. The function first retrieves the appropriate ASCII characters of each dice face from the `DICE_FACES` dictionary using a list comprehension. It then constructs a list of dice face rows by iterating through each row of each dice face and appending the corresponding row of each dice face to the list. The rows are then joined together into a string using the newline character `(\n)` as a separator.


## Program Input & Output

When you run `diceRoll.py`, the output will look like this;

```
Dice Rolling Simulator

How many dice do you want to roll (max 6 dice)?
> 2
RESULTS:
+-------+  +-------+
| O   O |  | O     |
|   O   |  |       |
| O   O |  |     O |
+-------+  +-------+
```
```
Dice Rolling Simulator

How many dice do you want to roll (max 6 dice)?
> 2
RESULTS:
+-------+ +-------+
| O     | | O   O |
|       | |       |
|     O | | O   O |
+-------+ +-------+
```
```
Dice Rolling Simulator

How many dice do you want to roll (max 6 dice)?
> 4
RESULTS:
+-------+  +-------+  +-------+  +-------+
| O     |  |       |  | O   O |  | O     |
|       |  |   O   |  |   O   |  |   O   |
|     O |  |       |  | O   O |  |     O |
+-------+  +-------+  +-------+  +-------+
```