# Lottery Simulator

## Description

The Lottery Simulator program simulates multiple rounds of lottery drawings, where a user selects a set of lottery numbers and a Powerball number, and the program generates random lottery results to see how often the user's selections match the drawn numbers and Powerball.

## How it Works

- Enter 5 unique numbers between 1 and 69 and a separate Powerball number between 1 and 26.
- The program simulates a specified number of lottery drawings. In each simulation:
    - Five unique numbers between 1 and 69 are randomly selected to represent the drawn lottery numbers.
    - A single Powerball number between 1 and 26 is randomly selected.
- The program compares the drawn numbers and Powerball with the picked numbers.
- The program checks how many of the picked numbers match the drawn numbers. It also checks if the picekd Powerball number matches the drawn Powerball.

## Running the Program

```bash
# Navigate to the project directory
cd lottery-simulator/

# Run the main script
python3 lottery_sim.py
```

## Program Input & Output

When you run the program `lottery_sim.py`, the output will look like this;

```
The Lottery Simulator.

Test your luck by choosing 5 unique numbers between 1 and 69,
along with a Powerball number between 1 and 26.

This simulator will run multiple simulations to see how often
your chosen numbers match the randomly drawn numbers and Powerball.
Will you hit the jackpot or waste your time and money?

Let's find out!

Enter 5 unique numbers from 1 to 69, separated by spaces. Enter (q)uit to exit.
> 1 2 3 4 5
Enter the Powerball number from 1 to 26. Enter (q)uit to exit.
> 6
Enter the number of simulations < 1,000,000. Enter (q)uit to exit.
> 1000000

Press Enter to Start Simulation...
Progress: 10%
Progress: 20%
Progress: 30%
Progress: 40%
Progress: 50%
Progress: 60%
Progress: 70%
Progress: 80%
Progress: 90%
Progress: 100%

--------------- Simulation Results ---------------
Your Lottery Numbers + Powerball: 1, 2, 3, 4, 5 + 6
Number of simulations: 1,000,000

23 Simulations matched 4 numbers.
1806 Simulations matched 3 numbers.
37303 Simulations matched 2 numbers.
282640 Simulations matched 1 number and the Powerball.
678228 Simulations matched 0 numbers.

Max number of matches: 4 numbers.
Simulation #161879 numbers: 4, 3, 22, 1, 2 + 6 and 22 other simulation(s) matched 4 numbers.

--------------------------------------------------

Enter 5 unique numbers from 1 to 69, separated by spaces. Enter (q)uit to exit.
> 12 15 42 5 1
Enter the Powerball number from 1 to 26. Enter (q)uit to exit.
> 22
Enter the number of simulations < 1,000,000. Enter (q)uit to exit.
> 500000

Press Enter to Start Simulation...
Progress: 10%
Progress: 20%
Progress: 30%
Progress: 40%
Progress: 50%
Progress: 60%
Progress: 70%
Progress: 80%
Progress: 90%
Progress: 100%

--------------- Simulation Results ---------------
Your Lottery Numbers + Powerball: 1, 5, 12, 15, 42 + 22
Number of simulations: 500,000

11 Simulations matched 4 numbers.
922 Simulations matched 3 numbers.
18660 Simulations matched 2 numbers.
141000 Simulations matched 1 number and the Powerball.
339407 Simulations matched 0 numbers.

Max number of matches: 4 numbers.
Simulation #390156 numbers: 5, 42, 26, 15, 1 + 22 and 10 other simulation(s) matched 4 numbers.

--------------------------------------------------

Enter 5 unique numbers from 1 to 69, separated by spaces. Enter (q)uit to exit.
> q
Exiting program... Bye!
```
