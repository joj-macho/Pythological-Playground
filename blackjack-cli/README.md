# Blackjack Card Game

## Description

This program is a Python implementation of a Blackjack Card Game where players try to get as close to 21 points as possible without going over.


## How it works

- The program begins by importing the <code>random</code> and <code>sys</code> modules. Then, it defines four variables that represent the four suits in a deck of playing cards: <code>HEARTS, DIAMONDS, SPADES, and CLUBS</code>. The four different suits of cards are represented using their Unicode character codes, i.e. <code>HEARTS = chr(9829), DIAMONDS = chr(9830), SPADES = chr(9824), CLUBS = chr(9827)</code>.

- The <code>main()</code> function begins by printing rules of the game. The game runs in a while loop, where the player is first checked if they can afford to play. The game loops until the player runs out of funds or chooses to quit the game. Inside the <code>main()</code> function, there are a series of functions that handle different aspects of the game.

- The first function to be called is <code>generateBet()</code>, which prompts the player for a bet and returns the <code>bet</code> amount. The function ensures that the <code>bet</code> amount is valid and within the player's available funds.

- The next function is <code>generateCardDeck()</code>, which returns a list of tuples representing a standard deck of 52 playing cards. The deck is shuffled using the <code>random.shuffle()</code> function from the <code>random</code> module.

- After the deck is generated, the player and dealer cards are dealt. Each player is given two cards from the deck. The player's cards are stored in the <code>playerHand</code> list, while the dealer's cards are stored in the <code>dealerHand</code> list.

- The player then decides on their next move. They can choose to "hit", "stand", or "double down". If the player chooses to "hit", they are dealt another card from the deck. The goal is to get as close to 21 as possible without going over. If the player goes over 21, they lose the game.

- Once the player has finished their turn, it is the dealer's turn to play. The dealer continues to hit until their hand value is 17 or higher.

- After both the player and dealer have completed their turns, the hands are compared to determine the winner. The winner is the player with a hand value closest to 21 without going over. If the dealer goes over 21, the player wins. If the player goes over 21 or has a lower hand value than the dealer, the player loses. If the player and dealer have the same hand value, it is a tie and the bet is returned to the player.


## Program Input & Output

When you run `blackjack.py`, the output will look like this:

```
Blackjack Card Game.

This game follows these simple rules:
    - Get as close to 21 without going over to win the game.
    - Kings, Queens, and Jacks are worth 10 points each.
    - Aces are worth 1 or 11 points.
    - Cards 2 through 10 are worth their face value.
    - The bet is returned to the player in case of a tie.
    - The dealer stops hitting at 17.
    - Enter (h)it to take another card.
    - Enter (s)tand to stop taking cards.
    - You can (d)ouble down on your first play to increase your bet + will hit one more time.
    
Available Funds: $5000
Enter bet amount between $1 - $5000. Enter (q)uit to exit.
> 200
Your bet is $200

Dealer: ???
 ___  ___ 
|## | |10 |
|###| | ♦ |
|_##| |_10|

Player: 11
 ___  ___ 
|8  ||3  |
| ♠ || ♥ |
|__8||__3|

(h)it,(s)tand,(d)ouble down
> h
You drew a 8 of ♣
Dealer: ???
 ___  ___ 
|## | |10 |
|###| | ♦ |
|_##| |_10|

Player: 19
 ___  ___  ___ 
|8  ||3  ||8  |
| ♠ || ♥ || ♣ |
|__8||__3||__8|

(h)it,(s)tand
> s
Dealer: 20
 ___  ___ 
|Q  ||10 |
| ♥ || ♦ |
|__Q||_10|

Player: 19
 ___  ___  ___ 
|8  ||3  ||8  |
| ♠ || ♥ || ♣ |
|__8||__3||__8|

You lost.
Press Enter to Continue...

Available Funds: $4800
Enter bet amount between $1 - $4800. Enter (q)uit to exit.
> 4000
Your bet is $4000

Dealer: ???
 ___  ___ 
|## | |8  |
|###| | ♥ |
|_##| |__8|

Player: 14
 ___  ___ 
|9  ||5  |
| ♦ || ♠ |
|__9||__5|

(h)it,(s)tand,(d)ouble down
> h
You drew a 4 of ♦
Dealer: ???
 ___  ___ 
|## | |8  |
|###| | ♥ |
|_##| |__8|

Player: 18
 ___  ___  ___ 
|9  ||5  ||4  |
| ♦ || ♠ || ♦ |
|__9||__5||__4|

(h)it,(s)tand
> s
Dealer: 18
 ___  ___ 
|Q  ||8  |
| ♦ || ♥ |
|__Q||__8|

Player: 18
 ___  ___  ___ 
|9  ||5  ||4  |
| ♦ || ♠ || ♦ |
|__9||__5||__4|

A tie! The bet is returned to you.
Press Enter to Continue...

Available Funds: $4800
Enter bet amount between $1 - $4800. Enter (q)uit to exit.
> 4800
Your bet is $4800

Dealer: ???
 ___  ___ 
|## | |Q  |
|###| | ♣ |
|_##| |__Q|

Player: 13
 ___  ___ 
|6  ||7  |
| ♣ || ♣ |
|__6||__7|

(h)it,(s)tand
> h
You drew a Q of ♥
Dealer: ???
 ___  ___ 
|## | |Q  |
|###| | ♣ |
|_##| |__Q|

Player: 23
 ___  ___  ___ 
|6  ||7  ||Q  |
| ♣ || ♣ || ♥ |
|__6||__7||__Q|

Dealer: 17
 ___  ___ 
|7  ||Q  |
| ♠ || ♣ |
|__7||__Q|

Player: 23
 ___  ___  ___ 
|6  ||7  ||Q  |
| ♣ || ♣ || ♥ |
|__6||__7||__Q|

You lost.
Press Enter to Continue...

No funds to Continue Game.
Bye!
```