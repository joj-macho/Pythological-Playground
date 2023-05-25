# Carrot in the Box

## Description

Carrot in a Box is a two player game where the aim of the game is to bluff as well as possible and end up with a carrot.That is, player A has to bluff as best as possible, so that B ultimately selects the wrong (empty) box. B on the other hands needs to call the bluff of A. B has the "easier" task, as he has the ultimate decision; on the other hand, he has much less information than A (who actually knows which box contains the carrot).

This program is an implementation of the game Carrot in a Box

## How it Works

- The program begins by importing the `random` module which it then uses to randomly determine the location of the carrot in the boxes.

- The `main()` function is defined. It starts by printing the rules of the game and prompts the players to enter their names.

- The program enters a loop that allows multiple rounds of the game to be played. Inside the loop, the `play_game()` function is called to play a single round.

- In the `play_game()` function, the boxes (Box A and Box B) are displayed using ASCII art. The names of the players are printed, and the first player (`player_1`) is instructed to look into their box while the second player (`player_2`) closes their eyes. The program waits for the second player to close their eyes by prompting the first player to press Enter. Randomly, either Box A or Box B is selected to contain the carrot. The result is stored in the `carrot_in_box_1` variable.

- The contents of the first player's box are displayed based on whether the carrot is in Box A or not. The program waits for the first player to press Enter, and then clears the screen. The first player is instructed to tell the second player to open their eyes, and the program waits for the first player to press Enter. The program prompts the second player to decide whether they want to swap boxes with the first player or not. The input is validated to ensure it's either 'y' or 'n'.

- If the second player chooses to swap boxes (responds with 'y'), the `carrot_in_box_1` variable is inverted, and the boxes (Box A and Box B) are swapped. The updated boxes are displayed, and the program prompts the user to press Enter to show the winner. The program displays the final state of the boxes based on the location of the carrot and prints the names of the players.

- Finally, the program declares the winner based on the location of the carrot and prints their name.

- After the round is complete, the program prompts the players if they want to play again. If the response doesn't start with 'y', the loop ends, and the program exits.


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