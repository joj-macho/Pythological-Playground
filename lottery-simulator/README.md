# Lottery Simulator

## Description

This program is a Python implementation of a Lottery Simulator where players can choose 5 numbers from 1 to 69 and a Powerball number from 1 to 26. The program allows users to specify how many times they want to play and see the results of the lottery simulation.

## How it Works

- The program first imports the `random` module. The `random` module is essential in creating a realistic simulation of the lottery draw by introducing randomness in the selection of winning numbers and the powerball number.

- The `main()` function is defined and called, this function displays an introductory message to welcome the user and provides instructions for playing the lottery simulation. Inside the `main()` function, there is a while loop that allows the user to play the game multiple times. The user is prompted to enter 5 different numbers from 1 to 69 and a Powerball number from 1 to 26. The user can also specify how many times they want to play the lottery.

The `get_user_numbers()`, `get_user_powerball()`, and `get_user_num_plays()` functions handle user inputs for numbers selection and the number of plays.

- The `simulate_lottery()` function simulates the lottery draw based on user inputs. It shuffles a range of possible numbers and randomly selects winning numbers and a Powerball number for each simulation. The function then checks for matching numbers and calculates hits.

- The `print_results()` function displays the simulation results, including the user's chosen numbers, the number of hits, and the maximum hits.

- Players can choose whether or not to gamble again.


## Program Input & Output

When you run the program `lottery_sim.py`, the output will look like this;

```

Welcome to the Lottery Simulator!
This program simulates a lottery draw where you choose 5 numbers from 1 to 69 and a Powerball number from 1 to 26.
You can specify how many times you want to play and see the results.
    
Enter 5 different numbers from 1 to 69, separated by spaces:
> 12 16 20 18 25
Enter the Powerball number from 1 to 26:
> 23
How many times do you want to play? (Max: 1000000)
> 100000
If the cost of the lotto ticket is $2. It would cost $200000 to play 100000 times...
Now then let' get our gambling freak on!
Press Enter to start...

0 Simulations Completed...
10000 Simulations Completed...
20000 Simulations Completed...
30000 Simulations Completed...
40000 Simulations Completed...
50000 Simulations Completed...
60000 Simulations Completed...
70000 Simulations Completed...
80000 Simulations Completed...
90000 Simulations Completed...

100000 Simulations Completed...

Your numbers: 12, 16, 20, 18, 25, (23-Powerball Number)
Out of 100000 Simulations...

1 Simulations matched 4 numbers:
    Attempt 19738: 16 67 12 18 25

208 Simulations matched 3 numbers:

3643 Simulations matched 2 numbers:

28183 Simulations matched 1 numbers:

67965 Simulations matched 0 numbers.

Maximum Hits: 4 numbers

Do you want to play again? Enter (y)es or (n)o: y
Enter 5 different numbers from 1 to 69, separated by spaces:
> 1 2 3 4 5
Enter the Powerball number from 1 to 26:
> 6
How many times do you want to play? (Max: 1000000)
> 25
If the cost of the lotto ticket is $2. It would cost $50 to play 25 times...
Now then let' get our gambling freak on!
Press Enter to start...

25 Simulations Completed...

Your numbers: 1, 2, 3, 4, 5, (6-Powerball Number)
Out of 25 Simulations...

2 Simulations matched 2 numbers:
    Attempt 18: 62 4 68 3 35
    Attempt 25: 37 1 12 64 5

9 Simulations matched 1 numbers:
    Attempt 2: 5 65 7 45 30
    Attempt 3: 19 3 33 13 10
    Attempt 5: 22 25 1 56 51
    Attempt 8: 12 31 29 15 4
    Attempt 11: 30 41 51 4 47
    Attempt 14: 57 39 13 19 5
    Attempt 15: 28 42 3 41 15
    Attempt 22: 5 16 34 40 30
    Attempt 23: 36 2 47 57 53

14 Simulations matched 0 numbers.

Maximum Hits: 2 numbers

Do you want to play again? Enter (y)es or (n)o: y
Enter 5 different numbers from 1 to 69, separated by spaces:
> 1 2 3 4 5
Enter the Powerball number from 1 to 26:
> 6
How many times do you want to play? (Max: 1000000)
> 800000
If the cost of the lotto ticket is $2. It would cost $1600000 to play 800000 times...
Now then let' get our gambling freak on!
Press Enter to start...

0 Simulations Completed...
100000 Simulations Completed...
200000 Simulations Completed...
300000 Simulations Completed...
400000 Simulations Completed...
You won the Powerball Lottery on attempt 450281!
500000 Simulations Completed...
600000 Simulations Completed...
700000 Simulations Completed...

Your numbers: 1, 2, 3, 4, 5, (6-Powerball Number)
Out of 800000 Simulations...

1 Simulations matched 5 numbers:
    Attempt 450281: 2 3 4 5 1

24 Simulations matched 4 numbers:

1466 Simulations matched 3 numbers:

29776 Simulations matched 2 numbers:

225744 Simulations matched 1 numbers:

542989 Simulations matched 0 numbers.

Maximum Hits: 5 numbers

Do you want to play again? Enter (y)es or (n)o: n
Thanks for playing!
```
