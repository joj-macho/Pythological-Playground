# Cho-Han Game

## Description

The Cho-Han program is a traditional Japanese dice game where players bet on whether the sum of two rolled dice will be even (Cho) or odd (Han).

## How it Works

- Place a bet and guess the dice result.
- The program simulate rolling two dice and displays the result.

## Running the Program

```bash
# Navigate to the project directory
cd cho-han/

# Run the main script
python3 cho_han.py
```

## Program Input & Output

When you run `cho_han.py`, the output will look like this:


```
Cho-Han Dice Game.

Guess the sum of dice roll, cho (even) or han (odd).

You have 100 in your pockets.

Enter your bet amount or (q)uit to exit:
> 50

Your bet is 50.0

Rolling the dice...

Choose Cho (even) or Han (odd):
> haan
Invalid guess! Guess Cho or Han.

Choose Cho (even) or Han (odd):
> han

Dice Results:
+-------+  +-------+
|       |  | O   O |
|   O   |  | O   O |
|       |  | O   O |
+-------+  +-------+
  ICHI    &   ROKU   

Congratulations! You won 50.0

You have 150.0 in your pockets.

Enter your bet amount or (q)uit to exit:
> 150

Your bet is 150.0

Rolling the dice...

Choose Cho (even) or Han (odd):
> han

Dice Results:
+-------+  +-------+
|       |  | O   O |
|   O   |  | O   O |
|       |  | O   O |
+-------+  +-------+
  ICHI    &   ROKU   

Congratulations! You won 150.0

You have 300.0 in your pockets.

Enter your bet amount or (q)uit to exit:
> 299

Your bet is 299.0

Rolling the dice...

Choose Cho (even) or Han (odd):
> cho

Dice Results:
+-------+  +-------+
| O   O |  | O     |
|       |  |   O   |
| O   O |  |     O |
+-------+  +-------+
   SHI    &    SAN   

Sorry, you lost $299.0

You have 1.0 in your pockets.

Enter your bet amount or (q)uit to exit:
> 1

Your bet is 1.0

Rolling the dice...

Choose Cho (even) or Han (odd):
> cho

Dice Results:
+-------+  +-------+
|       |  | O   O |
|   O   |  |   O   |
|       |  | O   O |
+-------+  +-------+
  ICHI    &    GO    

Congratulations! You won 1.0

You have 2.0 in your pockets.

Enter your bet amount or (q)uit to exit:
> 2

Your bet is 2.0

Rolling the dice...

Choose Cho (even) or Han (odd):
> cho

Dice Results:
+-------+  +-------+
| O   O |  | O     |
|   O   |  |       |
| O   O |  |     O |
+-------+  +-------+
   GO     &    NI    

Sorry, you lost $2.0

You have run out of money...Bye!
```