# Fast Draw

## Description

The program is a simple game called "Fast Draw" where the user has to press the Enter key within 0.3 seconds after the word "Draw" appears on the screen. This program can be used to test your reaction speed.

## How it Works

- The program begins by importing the `random` module to introduce randomness, `time` module for measuring time, and the `sys` module for system-related features.

- The program defines some constants such as the minimum and maximum delay before the word "Draw" appears (`DRAW_DELAY_MIN` and `DRAW_DELAY_MAX`), the delay before displaying results for the next round (`DELAY_BEFORE_RESULTS`), and the total number of rounds in the game (`ROUND_LIMIT`).

- The `main()` function is defined and displays the game instructions and waits for the user to press Enter to continue. Next, the score counters `wins` and `losses` are initialized to 0.

- The game consists of a series of rounds, controlled by a `for` loop that iterates from 1 to `ROUND_LIMIT`. This loop executes the game logic for each round. Inside the loop, the program displays the round number and prompts the user by printing "Ready ....".

- The program then pauses for a random interval between `DRAW_DELAY_MIN` and `DRAW_DELAY_MAX` seconds using the `time.sleep()` function. After the pause, the program displays "DRAW!" and records the current time using `time.time()`.

- The program waits for user input (Enter key press) using the `input()` function.

- The time elapsed since "DRAW!" was displayed is calculated by subtracting the recorded time from the current time. The program determines the outcome based on the response time:
    - If the response time is less than 0.01 seconds, it means the user pressed Enter before "DRAW" appeared, and the program prints "You drew before 'DRAW' appeared. You lose!" and increments the `losses` counter.
    - If the response time is greater than 0.3 seconds, the program prints "You took [time] seconds to Draw. Too Slow" (rounded to 3 decimal places) and increments the `losses` counter.
    - If the response time is between 0.01 and 0.3 seconds (inclusive), the program prints "You took [time] seconds to Draw. You are the fastest draw in the West!" (rounded to 2 decimal places) and increments the `wins` counter.

- The program displays the current score by printing "Score: Wins = [wins], Losses = [losses]". If the round number is equal to the `ROUND_LIMIT`, the game is over. The program prints the final score and breaks out of the loop. Otherwise, the program asks the user if they want to play again or quit. It validates the user's input and prompts again if it's invalid.

- If the user chooses to quit, the program prints "Bye!" and exits using `sys.exit()`.

- The loop continues to the next round, and the game repeats until the round limit is reached or the user chooses to quit.

## Program Input & Output
When you run `fast_draw.py`, the output will look like this;

```

Fast Draw!
Let us see if you are the fastest draw in the west. 

When you see "Draw", you have 0.3 seconds to press Enter. You lose if you press Enter before the word "Draw" appears
Press Enter To Continue ...

Round 1:
Ready ....
DRAW!

You took 0.25 seconds to Draw.
You are the fastest draw in the West!
Score: Wins = 1, Losses = 0
Press Enter to Play again, or enter (q)uit to quit.
> 

Round 2:
Ready ....
DRAW!

You took 0.23 seconds to Draw.
You are the fastest draw in the West!
Score: Wins = 2, Losses = 0
Press Enter to Play again, or enter (q)uit to quit.
> 

Round 3:
Ready ....
DRAW!

You took 0.901 seconds to Draw. Too Slow
Score: Wins = 2, Losses = 1
Press Enter to Play again, or enter (q)uit to quit.
> 

Round 4:
Ready ....
DRAW!

You drew before "DRAW" appeared. You lose!
Score: Wins = 2, Losses = 2
Press Enter to Play again, or enter (q)uit to quit.
> 

Round 5:
Ready ....
DRAW!

You took 0.27 seconds to Draw.
You are the fastest draw in the West!
Score: Wins = 3, Losses = 2
Press Enter to Play again, or enter (q)uit to quit.
> q
Bye!
```
