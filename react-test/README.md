# Fast Draw Game

## Description

The Fast Draw program is a reaction time test that measures how quickly a user can press the Enter key after seeing the "DRAW!" prompt.

## How it Works

- Press Enter when after the "DRAW!" text.

## Running the Program

```bash
# Navigate to the project directory
cd react-test/

# Run the main script
python3 fast_draw.py
```

## Program Input & Output

When you run `fast_draw.py`, the output will look like this;

```
Fast Draw Game!

When you see "Draw", you have 0.3 seconds to press Enter.
You lose if you press Enter before the word "Draw" appears
    
Press Enter To Continue ...

Round 1:
Ready ....
DRAW!

You took 0.28 seconds to Draw.
You are the fastest draw in the West!
Press Enter to Play again, or enter (q)uit to exit.
> 

Round 2:
Ready ....

DRAW!
You drew before "DRAW" appeared. You lose!
Press Enter to Play again, or enter (q)uit to exit.
> 

Round 3:
Ready ....
DRAW!

You took 0.26 seconds to Draw.
You are the fastest draw in the West!
Press Enter to Play again, or enter (q)uit to exit.
> 

Round 4:
Ready ....
DRAW!

You took 0.22 seconds to Draw.
You are the fastest draw in the West!
Press Enter to Play again, or enter (q)uit to exit.
> q
Bye!
```
