# Blackjack Card Game

## Description

This program is a Python implementation of a Blackjack Card Game where players try to get as close to 21 points as possible without going over.

## How it works

- To play the game, execute the `main()` function in the `blackjack.py` file. Follow the on-screen prompts to place bets and make moves during the game.

- The `main()` creates an instance of the of the `BlackjackGame`. The `BlackjackGame` class represents the core of the game with the following key methods:
    - `get_player_bet(player_funds)`: Prompt the player to enter a valid bet amount.
    - `display_hands(show_dealer_hand)`: Display the current hands of the dealer and player.
    - `calculate_hand_value(hand)`: Calculate the total value of a hand.
    - `get_player_move()`: Prompt the player to choose a move.

- The game starts with a welcoming introduction, explaining the rules and how to play.

- The player is prompted to enter a bet amount, ensuring it is within their available funds.

- Initial cards are dealt to both the player and the dealer.

- The player takes turns hitting, standing, or doubling down until they either win, lose, or choose to stand.

- If the player doesn't bust, the dealer takes their turn, hitting until their hand reaches 17 or higher.

- The final hands are compared, and the winner is determined. The player's funds are adjusted accordingly.

## Program Input & Output

When you run `blackjack.py`, the output will look like this:

```

Welcome to the Blackjack Card Game!

The aim is to get as close to 21 without going over. Let's go over the rules:
  - Kings, Queens, and Jacks are worth 10 points each.
  - Aces can be worth 1 or 11 points.
  - Cards 2 through 10 are valued at their face value.
  - The dealer stops hitting at 17.
  - If you tie with the dealer, your bet is returned.

Now, Let's get our gambling freak on!

Your Available Funds: $1000
Enter bet amount between $1 - $1000. Enter (q)uit to exit.
> 500

Your bet is $500


------ Current Hands ------

Dealer: ???
 ___ 
|## |
|###|
|_##|
 ___ 
|A  |
| ♠ |
|__A|

Player: 20
 ___ 
|Q  |
| ♣ |
|__Q|
 ___ 
|10 |
| ♦ |
|_10|

Choose your move: (h)it, (s)tand, or (d)ouble down
> s

------ Final Hands ------

Dealer: 20
 ___ 
|9  |
| ♠ |
|__9|
 ___ 
|A  |
| ♠ |
|__A|

Player: 20
 ___ 
|Q  |
| ♣ |
|__Q|
 ___ 
|10 |
| ♦ |
|_10|

It's a tie! The bet is returned to you.

Player Wins: 0 | Dealer Wins: 0
Your Total Funds: $1000

Do you want to play another round? (y/n)
> y
Your Available Funds: $1000
Enter bet amount between $1 - $1000. Enter (q)uit to exit.
> 500

Your bet is $500


------ Current Hands ------

Dealer: ???
 ___ 
|## |
|###|
|_##|
 ___ 
|8  |
| ♠ |
|__8|

Player: 9
 ___ 
|2  |
| ♦ |
|__2|
 ___ 
|7  |
| ♦ |
|__7|

Choose your move: (h)it, (s)tand, or (d)ouble down
> h

------ Current Hands ------

Dealer: ???
 ___ 
|## |
|###|
|_##|
 ___ 
|8  |
| ♠ |
|__8|

Player: 14
 ___ 
|2  |
| ♦ |
|__2|
 ___ 
|7  |
| ♦ |
|__7|
 ___ 
|5  |
| ♠ |
|__5|

Choose your move: (h)it, (s)tand, or (d)ouble down
> h

------ Current Hands ------

Dealer: ???
 ___ 
|## |
|###|
|_##|
 ___ 
|8  |
| ♠ |
|__8|

Player: 21
 ___ 
|2  |
| ♦ |
|__2|
 ___ 
|7  |
| ♦ |
|__7|
 ___ 
|5  |
| ♠ |
|__5|
 ___ 
|7  |
| ♥ |
|__7|

BLACKJACK! You Win.

------ Final Hands ------

Dealer: 18
 ___ 
|J  |
| ♥ |
|__J|
 ___ 
|8  |
| ♠ |
|__8|

Player: 21
 ___ 
|2  |
| ♦ |
|__2|
 ___ 
|7  |
| ♦ |
|__7|
 ___ 
|5  |
| ♠ |
|__5|
 ___ 
|7  |
| ♥ |
|__7|

You won $500

Player Wins: 1 | Dealer Wins: 0
Your Total Funds: $1500

Do you want to play another round? (y/n)
> y
Your Available Funds: $1500
Enter bet amount between $1 - $1500. Enter (q)uit to exit.
> 1200

Your bet is $1200


------ Current Hands ------

Dealer: ???
 ___ 
|## |
|###|
|_##|
 ___ 
|Q  |
| ♦ |
|__Q|

Player: 19
 ___ 
|Q  |
| ♥ |
|__Q|
 ___ 
|9  |
| ♣ |
|__9|

Choose your move: (h)it, (s)tand, or (d)ouble down
> s

------ Final Hands ------

Dealer: 19
 ___ 
|9  |
| ♦ |
|__9|
 ___ 
|Q  |
| ♦ |
|__Q|

Player: 19
 ___ 
|Q  |
| ♥ |
|__Q|
 ___ 
|9  |
| ♣ |
|__9|

It's a tie! The bet is returned to you.

Player Wins: 1 | Dealer Wins: 0
Your Total Funds: $1500

Do you want to play another round? (y/n)
> y
Your Available Funds: $1500
Enter bet amount between $1 - $1500. Enter (q)uit to exit.
> 1500

Your bet is $1500


------ Current Hands ------

Dealer: ???
 ___ 
|## |
|###|
|_##|
 ___ 
|J  |
| ♦ |
|__J|

Player: 12
 ___ 
|K  |
| ♥ |
|__K|
 ___ 
|2  |
| ♥ |
|__2|

Choose your move: (h)it, (s)tand, or (d)ouble down
> h

------ Current Hands ------

Dealer: ???
 ___ 
|## |
|###|
|_##|
 ___ 
|J  |
| ♦ |
|__J|

Player: 22
 ___ 
|K  |
| ♥ |
|__K|
 ___ 
|2  |
| ♥ |
|__2|
 ___ 
|10 |
| ♠ |
|_10|

Player busts! You lose.

------ Final Hands ------

Dealer: 16
 ___ 
|6  |
| ♦ |
|__6|
 ___ 
|J  |
| ♦ |
|__J|

Player: 22
 ___ 
|K  |
| ♥ |
|__K|
 ___ 
|2  |
| ♥ |
|__2|
 ___ 
|10 |
| ♠ |
|_10|

You lose!

Player Wins: 1 | Dealer Wins: 1
Your Total Funds: $0

Do you want to play another round? (y/n)
> y
No funds to Continue Game.
Bye!
```