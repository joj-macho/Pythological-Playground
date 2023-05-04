# Fast Draw

## Description

The program is a simple game called "Fast Draw" where the user has to press the Enter key within 0.3 seconds after the word "Draw" appears on the screen. This program can be used to test your reaction speed.

## How it Works

- The `main()` function is defined and displays the game instructions and waits for the user to press Enter to continue. The game loop starts, which runs infinitely until the user quits the game. 

- The game is played using an infinite loop. Inside the loop, the program prints "Ready ..." and waits for a random amount of time between 2 and 5 seconds, using the `sleep()` function from the time module, before printing "DRAW!" and recording the time. The program then waits for the user to press Enter, calculates the time elapsed between the "DRAW!" message and the user's input, and displays a message indicating whether the user won, lost, or was too slow.

- The program prompts the user to play again or quit the game. If the user chooses to quit the game, the `sys.exit()` function is called to terminate the program.


## Program Input & Output
When you run `fast_draw.py`, the output will look like this;

```

Fast Draw!
Let us see if you are the fastest draw in the west. 

When you see "Draw", you have 0.3 seconds to press Enter. You lose if you press Enter before the word "Draw" appears
Press Enter To Continue ...
Ready ....
DRAW!

You took 0.25 seconds to Draw. 
You are the fastest draw in the West!

Score: Wins = 1, Losses = 0
Press Enter to Play again, or enter (q)uit to quit.
Ready ....
DRAW!

You took 0.2138 seconds to Draw. 
You are the fastest draw in the West!

Score: Wins = 2, Losses = 0
Press Enter to Play again, or enter (q)uit to quit.
Ready ....
DRAW!

You took 0.4583 seconds to Draw. Too Slow

Score: Wins = 2, Losses = 1
Press Enter to Play again, or enter (q)uit to quit.
> q
Bye!
```
