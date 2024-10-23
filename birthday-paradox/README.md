# The Birthday Problem

## Description

The "Birthday Problem" simulates the probability of at least two people in a group sharing the same birthday.

The birthday paradox states that in a group of randomly selected people, there is a higher probability than expected that at least two people share the same birthday. This highlisghts a counterintuitive result in probability theory: in a group of just 23 people, there's about a 50% chance that at least two people will share the same birthday.

## How it Works

- Enter the number of birthdays/people to generate and the number of simulations to run.
- The program uses the Monte Carlo method to simulate the birthday paradox. Where for each simulation, the program:
     - Generates random birthdays for the group.
     - Checks if there are any shared birthdays in the list and records whether there was a shared birthday.
- The final probability is calculated based on the number of simulations that had at least one shared birthday.

## Running the Program

```bash
# Navigate to the project directory
cd birthday-paradox/

# Run the main script
python3 birthday_problem.py
```

## Program Input & Output

When you run `birthday_problem.py`, the output will look like this:

```
The Birthday Problem Simulator.

The birthday paradox reveals that in a group of 23 people, there is about a
50% chance that at least two people will share the same birthday.

How likely is it for at least two people to havethe same birthday in a given
group size? Let's find out...

Enter the number of people in the group (1 - 100) or (q)uit to exit:
> 23
Enter the number of simulations to run (1 - 1,000,000) or (q)uit to exit:
> 100000

23 birthdays randomly generated...
13 April, 26 June, 02 September, 20 January, 26 October, 13 March, 11 December, 25 August, 19 January, 29 June, 10 September, 20 October, 26 September, 13 March, 10 May, 19 March, 04 October, 28 February, 20 July, 08 July, 27 March, 17 June, 25 November, 

In this simulation run #0:
There are no shared birthdays.

Press Enter to start the Simulation...

Simulating 23 random birthdays 100,000 times...

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

------------------------------Simulation Results------------------------------

Number of simulations performed: 100,000
Number of simulations with at least one shared birthday: 51735
In a group of 23 people, the probability of having at least two people with the same birthday is 51.73%.

Enter the number of people in the group (1 - 100) or (q)uit to exit:
> 75
Enter the number of simulations to run (1 - 1,000,000) or (q)uit to exit:
> 100000

75 birthdays randomly generated...
01 October, 26 December, 09 June, 20 November, 19 May, 29 July, 05 July, 17 December, 08 December, 16 February, 31 August, 01 July, 11 August, 06 April, 26 June, 08 February, 19 October, 26 December, 31 August, 06 October, 05 December, 06 February, 29 June, 21 June, 04 January, 03 March, 02 July, 27 December, 13 December, 23 November, 06 December, 25 December, 15 March, 06 December, 15 February, 30 September, 13 February, 13 April, 06 December, 04 August, 18 May, 15 July, 01 August, 31 December, 09 July, 26 December, 28 December, 20 December, 08 August, 04 February, 16 September, 17 March, 17 September, 02 July, 05 June, 25 February, 01 August, 13 March, 02 September, 24 May, 01 June, 24 July, 09 March, 05 September, 09 May, 27 July, 21 March, 21 May, 10 June, 22 November, 25 February, 22 August, 28 January, 30 May, 19 March, 

In this simulation run #0:
3 people share the same birthday, 26 December.
3 people share the same birthday, 06 December.

Press Enter to start the Simulation...

Simulating 75 random birthdays 100,000 times...

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

------------------------------Simulation Results------------------------------

Number of simulations performed: 100,000
Number of simulations with at least one shared birthday: 99977
In a group of 75 people, the probability of having at least two people with the same birthday is 99.98%.

Enter the number of people in the group (1 - 100) or (q)uit to exit:
> q

Exiting simulator... Bye!
```