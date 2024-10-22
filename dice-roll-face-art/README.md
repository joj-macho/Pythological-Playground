# Dice Rolling Simulator

## Description

The Dice Rolling Simulator program simulates rolling a dice or multiple dice and displays the corresponding ASCII characters of the rolled die.

## How it works

- Enter the number of dice to roll.
- Program rolls the specified number of dice, where each die roll is a random number between 1 and 6.
- The program then displays the results of the dice rolls using ASCII art representations of dice faces.

## Running the Program

```bash
# Navigate to the project directory
cd dice-roll-face-art/

# Run the main script
python3 dice_roll_sim.py
```

## Program Input & Output

When you run `dice_roll_sim.py`, the output will look like this;

```
Dice rolling simulator.

Enter number of dice to roll or (q)uit to exit:
> 1

Rolling the dice...

+-------+ 
| O   O | 
|       | 
| O   O | 
+-------+ 

Dice face result: [4]
Sum of dice faces: 4

Enter number of dice to roll or (q)uit to exit:
> 2

Rolling the dice...

+-------+ +-------+ 
| O     | | O     | 
|   O   | |   O   | 
|     O | |     O | 
+-------+ +-------+ 

Dice face result: [3, 3]
Sum of dice faces: 6

Enter number of dice to roll or (q)uit to exit:
> 3

Rolling the dice...

+-------+ +-------+ +-------+ 
| O     | |       | | O   O | 
|   O   | |   O   | | O   O | 
|     O | |       | | O   O | 
+-------+ +-------+ +-------+ 

Dice face result: [3, 1, 6]
Sum of dice faces: 10

Enter number of dice to roll or (q)uit to exit:
> 4

Rolling the dice...

+-------+ +-------+ +-------+ +-------+ 
| O   O | | O   O | | O     | |       | 
|   O   | |       | |   O   | |   O   | 
| O   O | | O   O | |     O | |       | 
+-------+ +-------+ +-------+ +-------+ 

Dice face result: [5, 4, 3, 1]
Sum of dice faces: 13

Enter number of dice to roll or (q)uit to exit:
> 5

Rolling the dice...

+-------+ +-------+ +-------+ +-------+ +-------+ 
| O   O | | O   O | | O     | | O     | | O     | 
| O   O | | O   O | |       | |   O   | |   O   | 
| O   O | | O   O | |     O | |     O | |     O | 
+-------+ +-------+ +-------+ +-------+ +-------+ 

Dice face result: [6, 6, 2, 3, 3]
Sum of dice faces: 20

Enter number of dice to roll or (q)uit to exit:
> 6

Rolling the dice...

+-------+ +-------+ +-------+ +-------+ +-------+ +-------+ 
| O   O | | O   O | | O     | | O   O | | O   O | | O   O | 
|       | |   O   | |   O   | |   O   | |       | |       | 
| O   O | | O   O | |     O | | O   O | | O   O | | O   O | 
+-------+ +-------+ +-------+ +-------+ +-------+ +-------+ 

Dice face result: [4, 5, 3, 5, 4, 4]
Sum of dice faces: 25

Enter number of dice to roll or (q)uit to exit:
> 7

Rolling the dice...

+-------+ +-------+ +-------+ +-------+ +-------+ +-------+ +-------+ 
| O   O | | O   O | | O     | | O     | | O     | | O   O | | O     | 
|       | |       | |   O   | |   O   | |   O   | |   O   | |   O   | 
| O   O | | O   O | |     O | |     O | |     O | | O   O | |     O | 
+-------+ +-------+ +-------+ +-------+ +-------+ +-------+ +-------+ 

Dice face result: [4, 4, 3, 3, 3, 5, 3]
Sum of dice faces: 25

Enter number of dice to roll or (q)uit to exit:
> 8
Invalid Input: Enter # dice 1-7.

Enter number of dice to roll or (q)uit to exit:
> q
Exiting program...Bye!
```