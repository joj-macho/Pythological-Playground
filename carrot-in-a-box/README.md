# Carrot in the Box

## Description

THe Carrot in the Box program is a two-player Carrot in the Box game where players can bluff and try to guess which box contains a carrot.

## How it Works

- The program randomly assigns the carrot to box A or box B.
- Player 1 has to bluf so that player 2 selects the empty box. Player 1 knows which box contains the carrrot.
- Player 2 needs to call the bluff of player 1, and ultimately decides whether to switch boxes or keep current boxes.

## Running the Program

```bash
# Navigate to the project directory
cd carrot-in-a-box/

# Run the main script
python3 carrot_in_box.py
```

## Program Input & Output

When you run `carrot_in_box.py`, the output will look like this:

```
Carrot in the Box Game.

Bluff until you have a box with a carrot in it.

Enter the name of Player 1:
> Alice
Enter the name of Player 2:
> Bob

HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    A    | /  |    B    | /
+---------+/   +---------+/
   Alice             Bob    

Alice, you have BOX A in front of you.
Bob, you have BOX B in front of you.
READY...?

Alice, look into your BOX.
Bob, close your eyes.
Press Enter when Bob closes their eyes.

Inside the BOX of Alice:

   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    A    | /  |    B    | /
+---------+/   +---------+/
 (carrot!)
   Alice             Bob    
Press Enter to Continue...

Alice, tell Bob to open their eyes.
Press Enter to Continue...

Bob, do you want to swap boxes with Alice? (y)es or (n)o
> y
HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    B    | /  |    A    | /
+---------+/   +---------+/
   Alice             Bob    
Press Enter to Show the Winner.


   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    B    | /  |    A    | /
+---------+/   +---------+/
(no carrot!)
   Alice             Bob    

Bob is the winner.

Do you want to play again? (y)es or (n)o
> n
Bye!
```