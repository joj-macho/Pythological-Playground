# Chohan Game

## Description

Cho-han is a dice game invented in Japan. Two six-sided dice are rolled and players must guess if the sum of the two dice is even (cho) or odd (han).


## How it Works

- The program starts by importing the `sys` and `random modules`. It also defines the constant `ENG_JAP_NUM` dictionary which maps the Japanese word for each number between 1 and 6.

- The `main()` function prints a welcome message and initializes the player's money to $5000. The program then enters a loop that continues until the player runs out of money or decides to quit.

- The program rolls two dice using the `random.randint()` function. The player is then prompted to choose cho or han, and the input is validated. The program then calculates the sum of the dice and determines the winning bet. The results of the dice roll and whether the player won or lost the bet are then displayed.

- The player's funds are updated based on the result of the bet. If the player runs out of money, the program prints a message and exits.


## Program Input & Output

When you run `chohan.py`, the output will look like this:


```
Cho-han Game.
A dice game where players must guess if the resulting sum of the dice is even (cho) or odd (han).
    
You have $5000.

Enter you bet amount. Enter (q)uit to exit.
> 2500

Dice Rolling...

Choose Cho (even) OR Han (odd)...
> cho
DICE Results:
        SAN and SAN ,(3 and 3)
You Won $ 2500!
You have $7500.

Enter you bet amount. Enter (q)uit to exit.
> 7500

Dice Rolling...

Choose Cho (even) OR Han (odd)...
> han
DICE Results:
        GO and NI ,(5 and 2)
You Won $ 7500!
You have $15000.

Enter you bet amount. Enter (q)uit to exit.
> 15000

Dice Rolling...

Choose Cho (even) OR Han (odd)...
> han
DICE Results:
        SAN and SAN ,(3 and 3)
You lost $ 15000!
You have ran out of money. Bye Loser!
```