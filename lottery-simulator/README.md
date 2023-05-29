# Lottery Simulator

## Description

This program is a Powerball Lottery simulator. It allows users to experience the excitement of playing the Powerball Lottery without spending any money.

## How it Works

- The program first imports the `random` module. The `random` module is essential in creating a realistic simulation of the lottery draw by introducing randomness in the selection of winning numbers and the powerball number.

- The program starts by defining constants for the ticket cost (`TICKET_COST`), the jackpot amount (`JACKPOT_AMOUNT`), and the maximum number of plays (`MAX_PLAYS`).

- The `main()` function is defined and calle, this function displays an introductory message to welcome the user and explain the purpose of the simulation. Inside the `main()` function, there is a while loop that allows the user to play the game multiple times.

- The `get_numbers()` function prompts the user to enter five different numbers from 1 to 69. It validates the input to ensure it meets the required criteria.

- The `get_powerball()` function prompts the user to enter the powerball number from 1 to 26. It also validates the input.

- The `get_num_of_plays()` function prompts the user to enter the number of times they want to play. It ensures that the input is within the valid range.

- The `simulate_lottery()` function takes the user's chosen numbers, powerball number, and the number of plays as input. It simulates the lottery draw by generating random winning numbers and a powerball number. It checks if the user's numbers match the winning numbers and powerball number to determine if they have won.

- After each simulation, the user is given the option to play again. If the user chooses to continue, the game repeats. Otherwise, the program ends with a thank-you message.


## Program Input & Output

When you run the program `lottery_sim.py`, the output will look like this;

```

Welcome to the Powerball Lottery Simulator!

Experience the excitement of the Powerball Lottery without spending a dime.

Each Powerball lottery ticket typically costs $2, and the current jackpot stands at $500000000.
However, with odds of 1 in 292,201,338, winning the jackpot is extremely unlikely.

This simulation allows you to enjoy the thrill of playing without the financial risk.

Enter 5 different numbers from 1 to 69, separated by spaces:
> 1 2 3 4 5
Enter the powerball number from 1 to 26:
> 6
How many times do you want to play? (Max: 1000000):
> 20

It costs $ 40 to play 20 times, but don't
worry. I'm sure you'll win it all back.
Press Enter to start...

The winning numbers are: 62 38 46 30 50 and 3You lost.

The winning numbers are: 19 53 7 63 49 and 2You lost.

The winning numbers are: 19 9 57 33 29 and 6You lost.

The winning numbers are: 67 37 19 69 29 and 19You lost.

The winning numbers are: 32 17 67 37 61 and 21You lost.

The winning numbers are: 31 25 69 40 33 and 10You lost.

The winning numbers are: 11 5 2 15 17 and 2You lost.

The winning numbers are: 20 69 40 50 56 and 10You lost.

The winning numbers are: 30 17 43 57 6 and 17You lost.

The winning numbers are: 12 16 4 39 51 and 4You lost.

The winning numbers are: 4 33 30 62 31 and 3You lost.

The winning numbers are: 25 10 52 20 63 and 14You lost.

The winning numbers are: 34 30 12 59 21 and 16You lost.

The winning numbers are: 59 68 55 38 44 and 26You lost.

The winning numbers are: 6 38 67 26 5 and 10You lost.

The winning numbers are: 28 48 21 41 58 and 25You lost.

The winning numbers are: 23 29 59 11 13 and 18You lost.

The winning numbers are: 58 30 36 10 46 and 15You lost.

The winning numbers are: 29 7 28 40 15 and 2You lost.

The winning numbers are: 37 25 69 64 49 and 14You lost.

You have wasted $ 40

Do you want to play again? Enter (y)es/(n)o:
> n
Thanks for playing!
```
