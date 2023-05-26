# Dice Rolling Simulator

## Description

The program is a Dice Rolling Simulator that simulates rolling a dice or multiple dice and displays the corresponding ASCII characters of the rolled die.

## How it works

- The program begins by importing the `random` module which us ysed ti simulate rolling dice.

- The program defines a dictionary `DICE_FACES` that contains ASCII representations of each possible dice face. Each face is represented as a tuple of strings, where each string represents a row of the dice face. The `DICE_HEIGHT` constant is defined to store the height of each dice face in rows. It is calculated based on the number of rows in one of the dice faces in `DICE_FACES`.

- The `main()` function prints a header for the program and then prompts the user to enter the number of dice they want to roll. It keeps prompting the user until a valid input (a number between 1 and 6) is provided. Once a valid input is received, the number of dice to roll is stored in the `num_of_dice` variable. Otherwise, an error message is displayed, and the user is prompted to enter a valid input.

- The program then rolls the dice by generating random numbers between 1 and 6. The number of dice rolled is determined by `num_of_dice`, and the results are stored in the `dice_roll_results` list.

- Next the program calls the `generate_dice_face()` function, passing the `dice_roll_results` list as a parameter. This function takes the list of dice roll results and generates the ASCII representation of the dice faces. Inside `generate_dice_face()`, the dice_face list is created by retrieving the corresponding ASCII face for each dice roll result from the `DICE_FACES` dictionary.

- The `dice_face_rows` list is then populated by iterating over the rows of the dice faces. For each row, the program retrieves the corresponding row elements from each dice face in `dice_face` and joins them together with spaces. The resulting row text is added to `dice_face_rows`. The `show_dice_face` variable is created by joining the rows in `dice_face_rows` with newline characters.

- Finally, in the `main()` function, the program displays the "`RESULTS`" header and prints the `show_dice_face`, which shows the ASCII representation of the rolled dice faces.


## Program Input & Output

When you run `dice_roll_sim.py`, the output will look like this;

```
Dice Rolling Simulator

How many dice do you want to roll (max 6 dice)?
> 1
RESULTS:
+-------+
| O   O |
|       |
| O   O |
+-------+
Do you want to roll again? (y/n)
> y
How many dice do you want to roll (max 6 dice)?
> 3
RESULTS:
+-------+ +-------+ +-------+
| O   O | | O   O | | O   O |
|   O   | |   O   | |       |
| O   O | | O   O | | O   O |
+-------+ +-------+ +-------+
Do you want to roll again? (y/n)
> y
How many dice do you want to roll (max 6 dice)?
> 7 
Enter a valid number of dice to roll (1-6)!
How many dice do you want to roll (max 6 dice)?
> 6
RESULTS:
+-------+ +-------+ +-------+ +-------+ +-------+ +-------+
| O   O | | O   O | |       | | O   O | | O     | | O     |
|   O   | | O   O | |   O   | | O   O | |   O   | |   O   |
| O   O | | O   O | |       | | O   O | |     O | |     O |
+-------+ +-------+ +-------+ +-------+ +-------+ +-------+
Do you want to roll again? (y/n)
> n
```