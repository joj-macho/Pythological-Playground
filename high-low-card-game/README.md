# Higher or Lower Card Game

## Description

This program is a Python implementation of the Higher or Lower Card Game. In this game, the player guesses whether the next card in a set of cards will be higher or lower than the current card shown. The goal is to make correct guesses to maximize the score.


## How it works

- The program begins by importing the <code>random</code> and <code>sys</code> modules. It then defines variables representing the four suits in a deck of playing cards: <code>HEARTS</code>, <code>DIAMONDS</code>, <code>SPADES</code>, and <code>CLUBS</code>. Each suit is represented using their Unicode character codes.

- The main game logic is defined in the <code>main()</code> function. This function starts by displaying the game rules and instructions to the player, generates a deck of cards using <code>generate_card_deck()</code>, and starts the game loop. The player is prompted to guess if the next card will be higher or lower than the current card, and points are awarded or deducted accordingly.

- The <code>generate_card_deck()</code> function creates a deck of cards by iterating through suits and ranks, creating tuples to represent each card. It shuffles the deck using <code>random.shuffle()</code>.

- The <code>show_card()</code> function displays a card in a stylized format using Unicode characters.

- The game continues for a specified number of rounds (<code>NUM_OF_CARDS</code>). In each round, the player guesses whether the next card will be higher or lower than the current card. The score is updated based on correct or incorrect guesses.

- The player is given the option to play again or quit. If the player chooses to quit, the game terminates.

## Program Input & Output

When you run `high_low.py`, the output will look like this:

```

Welcome to Higher or Lower card game!

In this game, you have to choose whether the next card will be higher or lower than the current card.
    - Starting with 50 points...
    - If you guess correctly, you get 20 points
    - If you guess incorrectly, you lose 15 points

How to Play:
    - Enter (h)igher to guess higher card.
    - Enter (l)lower to guess lower card.
    - You can (q)uit to exit program.
    
Starting card:
 ___ 
|Q  |
| ♠ |
|__Q|

Do you think the next card will be (h)igher or (l)ower? (q)uit to exit: l
Next Card is:
 ___ 
|3  |
| ♠ |
|__3|

Correct! You guessed lower.
Your Score: 70.

Do you think the next card will be (h)igher or (l)ower? (q)uit to exit: h
Next Card is:
 ___ 
|4  |
| ♥ |
|__4|

Correct! You guessed higher.
Your Score: 90.

Do you think the next card will be (h)igher or (l)ower? (q)uit to exit: h
Next Card is:
 ___ 
|A  |
| ♣ |
|__A|

Correct! You guessed higher.
Your Score: 110.

Do you think the next card will be (h)igher or (l)ower? (q)uit to exit: h
Next Card is:
 ___ 
|8  |
| ♥ |
|__8|

Wrong! The card is lower.
Your Score: 95.

Do you think the next card will be (h)igher or (l)ower? (q)uit to exit: l
Next Card is:
 ___ 
|9  |
| ♦ |
|__9|

Wrong! The card is higher.
Your Score: 80.

Do you think the next card will be (h)igher or (l)ower? (q)uit to exit: l
Next Card is:
 ___ 
|K  |
| ♠ |
|__K|

Wrong! The card is higher.
Your Score: 65.

Do you think the next card will be (h)igher or (l)ower? (q)uit to exit: l
Next Card is:
 ___ 
|3  |
| ♣ |
|__3|

Correct! You guessed lower.
Your Score: 85.

Do you think the next card will be (h)igher or (l)ower? (q)uit to exit: h
Next Card is:
 ___ 
|7  |
| ♥ |
|__7|

Correct! You guessed higher.
Your Score: 105.

Press ENTER to play again, press (q)uit to exit: q
```