# Chohan Game

## Description

Cho-han is a dice game invented in Japan. Two six-sided dice are rolled and players must guess if the sum of the two dice is even (cho) or odd (han).

## How it Works

- The program uses the `sys` module to exit early and the `random` module to roll the dice. The constant `ENG_JAP_NUM` dictionary maps the Japanese word for each number between 1 and 6.

- The `main()` function initializes the player's money to $5000. The program then enters a loop that continues until the player runs out of money or decides to quit.

- The program rolls two dice using the `random.randint()` function. The player is prompted to choose cho or han, their input is validated, and the sum of the dice is calculated to determine the winning bet. The results of the dice roll and whether the player won or lost the bet are then displayed.

- The player's funds are updated based on the result of the bet. If the player runs out of money, the program prints a message and exits.

## Program Input & Output

When you run `chohan.py`, the output will look like this:


```

Welcome to the Cho-han Dice Game.

Guess if the resulting sum of the dice is even (cho) or odd (han).
    
You have $1000 cash monies.

Enter you bet amount. Enter (q)uit to exit.
> 500

Dice Rolling...

Choose Cho (even) OR Han (odd)...
> han
DICE Results:
        ROKU and GO: (6 and 5)
You Won $500!
You have $1500 cash monies.

Enter you bet amount. Enter (q)uit to exit.
> 1400

Dice Rolling...

Choose Cho (even) OR Han (odd)...
> odd
Choose Cho or Han!
Choose Cho (even) OR Han (odd)...
> han
DICE Results:
        ICHI and SHI: (1 and 4)
You Won $1400!
You have $2900 cash monies.

Enter you bet amount. Enter (q)uit to exit.
> 2900

Dice Rolling...

Choose Cho (even) OR Han (odd)...
> cho
DICE Results:
        SAN and ICHI: (3 and 1)
You Won $2900!
You have $5800 cash monies.

Enter you bet amount. Enter (q)uit to exit.
> 5800

Dice Rolling...

Choose Cho (even) OR Han (odd)...
> han
DICE Results:
        SAN and ICHI: (3 and 1)
You lost $5800!
You have ran out of money. Bye Loser!
```