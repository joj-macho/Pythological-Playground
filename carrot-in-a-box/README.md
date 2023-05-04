# Carrot in the Box

## Description

Carrot in a Box is a two player game where the aim of the game is to bluff as well as possible and end up with a carrot.That is, player A has to bluff as best as possible, so that B ultimately selects the wrong (empty) box. B on the other hands needs to call the bluff of A. B has the "easier" task, as he has the ultimate decision; on the other hand, he has much less information than A (who actually knows which box contains the carrot).

This program is an implementation of the game Carrot in a Box

## How it Works

- Each player has a box, and only one box has a carrot in it. 

- Player A starts, he may look into his box. The other player (B) may not look into the box and does not know what is in his box (or the other).

- Player A can now either keep his own Box, or swap it with B's box. In addition, he may speak about his motives, why he keep the box or switched it.

- Once A is ready and happy, B's turn starts. He now may take the ultimate decision: does he keep his current box, or does he switch it with the current box of A? His decision is final - whichever box he chooses, is his.

## Program Input & Output

When you run `carrot_in_box.py`, the output will look like this:

```
Carrot in the Box Game. The rules are simple; To win, bluff until you have a box with a carrot in it.
    
Enter the name of player 1:
> John
Enter the name of player 2:
> Harold

HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    A    | /  |    B    | /
+---------+/   +---------+/
    John          Harold  

John you have BOX A in front of you.
Harold you have BOX B in front of you.
READY...?

John look into your BOX.
Harold close your eyes.
Press Enter when Harold closes their eyes.


Inside the BOX of John:

   ___VV____
  |   VV    |
  |   VV    |
  |___||____|    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    A    | /  |    B    | /
+---------+/   +---------+/
 (carrot!)
    John          Harold  
Press Enter to Continue...

--Blank Screen--

John tell Harold to open their eyes.
Press Enter to Continue...

Harold do you want to swap boxes with John, (y)es or (n)o?
> y
HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    B    | /  |  A     | /
+---------+/   +---------+/
    John          Harold  
Press Enter to Show the Winner.


   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|   B     | /  |  A       | /
+---------+/   +---------+/
    John          Harold  
Harold is the winner.
```