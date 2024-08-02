# Higher or Lower Card Game

## Description

This program is a Python implementation of the Higher or Lower Card Game. In this game, the player guesses whether the next card in a set of cards will be higher or lower than the current card shown. The goal is to make correct guesses to maximize the score.

## How it works

- The main game logic is defined in the `main()` function. This function starts by displaying the game rules and instructions to the player. The game begins with a starting card displayed on the console. Players must decide whether the next card will be higher or lower.

- Players input their prediction by pressing 'h' for higher or 'l' for lower.

- The next card is drawn, and the game evaluates the guess. Players earn points for correct guess and lose points for incorrect ones.

- The game continues for a specified number of rounds. The player's current score is displayed after each round.

## Running the Program

```bash
# Navigate to the project directory
cd pico-fermi-bagels

# Run the main script
python3 pico_fermi_bagels.py
```

## Program Input & Output

When you run `high_low.py`, the output will look like this:

```

Welcome to the Higher or Lower Card Game!

Rules:
    - Guess whether the next card will be higher or lower than the current card.
    - Correct guesses earn 20 points, incorrect guesses result in a loss of 15 points.
    - The game starts with a score of 50 points.

Starting card:
 ___ 
|7  |
| ♥ |
|__7|

Will the next card be (h)igher or (l)ower than the current card (7 of ♥)?
Press "h" for higher, "l" for lower
> l
Next card:
 ___ 
|6  |
| ♦ |
|__6|

Correct! 6 of ♦ is lower than 7 of ♥.
You earned 20 points.
Your current score: 70

Will the next card be (h)igher or (l)ower than the current card (6 of ♦)?
Press "h" for higher, "l" for lower
> h
Next card:
 ___ 
|9  |
| ♥ |
|__9|

Correct! 9 of ♥ is higher than 6 of ♦.
You earned 20 points.
Your current score: 90

Will the next card be (h)igher or (l)ower than the current card (9 of ♥)?
Press "h" for higher, "l" for lower
> l
Next card:
 ___ 
|A  |
| ♠ |
|__A|

Correct! A of ♠ is lower than 9 of ♥.
You earned 20 points.
Your current score: 110

Will the next card be (h)igher or (l)ower than the current card (A of ♠)?
Press "h" for higher, "l" for lower
> o
Invalid input. Please enter "h" for higher or "l" for lower.

Will the next card be (h)igher or (l)ower than the current card (A of ♠)?
Press "h" for higher, "l" for lower
> l
Next card:
 ___ 
|5  |
| ♥ |
|__5|

Wrong! 5 of ♥ is higher than A of ♠.
You lost 15 points.
Your current score: 95

Will the next card be (h)igher or (l)ower than the current card (5 of ♥)?
Press "h" for higher, "l" for lower
> h
Next card:
 ___ 
|A  |
| ♦ |
|__A|

Wrong! A of ♦ is lower than 5 of ♥.
You lost 15 points.
Your current score: 80

Will the next card be (h)igher or (l)ower than the current card (A of ♦)?
Press "h" for higher, "l" for lower
> h
Next card:
 ___ 
|2  |
| ♥ |
|__2|

Correct! 2 of ♥ is higher than A of ♦.
You earned 20 points.
Your current score: 100

Will the next card be (h)igher or (l)ower than the current card (2 of ♥)?
Press "h" for higher, "l" for lower
> h
Next card:
 ___ 
|8  |
| ♦ |
|__8|

Correct! 8 of ♦ is higher than 2 of ♥.
You earned 20 points.
Your current score: 120

Will the next card be (h)igher or (l)ower than the current card (8 of ♦)?
Press "h" for higher, "l" for lower
> l
Next card:
 ___ 
|Q  |
| ♣ |
|__Q|

Wrong! Q of ♣ is higher than 8 of ♦.
You lost 15 points.
Your current score: 105

Game Over!
Your final score is 105.

To play again, press ENTER, or "q" to quit:
> q
Thank you for playing! Goodbye!
```