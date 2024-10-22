# Rock Paper Scissors Game

## Description

The Rock-Paper-Scissors game is a classic hand game played by two or more players. Players verbally count "rock, paper, scissors" and simultaneously shape their hands to represent one of three options, rock, paper, or scissors.

The objective of the game is to anticipate and counter your opponent's move with the appropriate hand shape. Rock beats scissors, scissors beat paper, and paper beats rock.

## How it works

- Enter rock, paper, or scissors.
- Program will randomly make a move.

## Running the Program

```bash
# Navigate to the project directory
cd rock-paper-scissors-game/

# Run the main script
python3 rock_paper_scissors.py
```

## Program Input & Output

When you run `rock_paper_scissors.py`, the output will look like this;

```
Rock Paper Scissors Game.

Game Rules;
    - Rock smashes Scissors
    - Paper covers Rock
    - Scissors cut Paper

Enter (r)ock, (p)aper, or (s)cissors. Enter (q)uit to exit.
> r

Player Move: Rock 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
 
VS.

Computer Move: Paper 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

You Lose!

0 Wins | 1 Losses | 0 Ties

Enter (r)ock, (p)aper, or (s)cissors. Enter (q)uit to exit.
> p

Player Move: Paper 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
 
VS.

Computer Move: Scissors 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

You Lose!

0 Wins | 2 Losses | 0 Ties

Enter (r)ock, (p)aper, or (s)cissors. Enter (q)uit to exit.
> s

Player Move: Scissors 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
 
VS.

Computer Move: Scissors 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

A tie!

0 Wins | 2 Losses | 1 Ties

Enter (r)ock, (p)aper, or (s)cissors. Enter (q)uit to exit.
> r

Player Move: Rock 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
 
VS.

Computer Move: Scissors 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

You Win!

1 Wins | 2 Losses | 1 Ties

Enter (r)ock, (p)aper, or (s)cissors. Enter (q)uit to exit.
> q
Exiting game...Bye!
```
