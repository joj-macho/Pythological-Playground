# Coin Flip Simulation

## Description

The "Coin Flip Simulation" program allows users to simulate flipping a coin multiple times and track the outcomes (heads and tails).

## How It Works

This simulation provides a simple and interactive way to understand coin flipping probabilities and statistics.

- Enter the number of coin flips. The limit to the number of simulations you can run is $1,000,000$, just because,
- The program performs the flips and updates the counts.
- Displays statistics, including the total number of flips, the number of heads and tails, and their percentages.

## Running the Program

```bash
# Navigate to the project directory
cd coin-flips/

# Run the main script
python3 coin_flip_sim.py
```

## Program Input & Output

When you run `coin_flip_sim.py`, the output will look like this:

```
Welcome to the Coin Flip Simulator!

Enter the number of coin flips to simulate. Enter (q)uit to exit.
> 1

Simulating 1 coin flips...

----------- Results -----------
Total Flips: 1
Heads: 1     | P(H) = 100.00%
Tails: 0     | P(T) = 0.00%
-------------------------------

Enter the number of coin flips to simulate. Enter (q)uit to exit.
> 10

Simulating 10 coin flips...

----------- Results -----------
Total Flips: 10
Heads: 2     | P(H) = 20.00%
Tails: 8     | P(T) = 80.00%
-------------------------------

Enter the number of coin flips to simulate. Enter (q)uit to exit.
> 1000

Simulating 1,000 coin flips...

----------- Results -----------
Total Flips: 1,000
Heads: 509   | P(H) = 50.90%
Tails: 491   | P(T) = 49.10%
-------------------------------

Enter the number of coin flips to simulate. Enter (q)uit to exit.
> 1000000

Simulating 1,000,000 coin flips...

----------- Results -----------
Total Flips: 1,000,000
Heads: 499,597 | P(H) = 49.96%
Tails: 500,403 | P(T) = 50.04%
-------------------------------

Enter the number of coin flips to simulate. Enter (q)uit to exit.
> 1000000000

Simulating 1,000,000 coin flips...

----------- Results -----------
Total Flips: 1,000,000
Heads: 499,875 | P(H) = 49.99%
Tails: 500,125 | P(T) = 50.01%
-------------------------------

Enter the number of coin flips to simulate. Enter (q)uit to exit.
> q
Bye!
```