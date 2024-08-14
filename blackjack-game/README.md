# Blackjack Game

## Description

The Blackjack game allows a single player to play against a dealer, following traditional Blackjack rules. The player has to try to get as close to 21 points as possible without going over.

## How It Works

- **Initial Bet and Deal**:
    - The player places a bet at the start of each round. Bets are adjusted based on the final outcome.
    - The game deals two cards each to the player and the dealer. The dealer's first card is concealed, while the second card is shown.

- **Player and Dealer Actions**:
    - The player can choose to "Hit" (receive another card), "Stand" (keep their current hand), or "Double-Down" (double their bet and receive one more card).
    - The player makes decisions until they choose to stand or their hand exceeds 21.
    - After the player stands, the dealer continues hitting until reaching a hand value of 17 or higher.

- **Determining the Winner**:
    - The program compares the player's hand with the dealer's hand.
    - The player wins if their hand is closer to 21 without exceeding it, or if the dealer busts.
    - The dealer wins if their hand is closer to 21 without exceeding it, or if the player busts.
    - Player keeps their cash if they tie with the dealeer.
    - The player's funds are adjusted accordingly.

## Running the Program

```bash
# Navigate to the project directory
cd blackjack-game/

# Run the main script
python3 main.py
```

## Program Input & Output

When you run `main.py`, the output will look like this:

```
Welcome to the Blackjack Card Game!

The aim is to get as close to 21 without going over. Here are the rules:
    - Kings, Queens, and Jacks are worth 10 points each.
    - Aces can be worth 1 or 11 points, depending on your hand total.
    - Cards 2 through 10 are valued at their face value.
    - The dealer stops hitting at <= 17.

Now, let's get our gambling freak on!

Player Funds: 100

Enter your bet or enter (q)uit to exit:
> 10
Your bet is 10.0

---------------------------------Initial Hands:--------------------------------

Player's Hand: 9
 ___   ___  
|7  | |2  | 
| ♦ | | ♠ | 
|__7| |__2| 

Dealer's Hand: ???
 ___   ___  
|## | |5  | 
|###| | ♦ | 
|_##| |__5| 

Enter (h)it, (s)tand, (d)ouble-down
> d
Bet Doubled to 20.0

                          ----- Player Move: Hit -----                         

Player's Hand: 11
 ___   ___   ___  
|7  | |2  | |2  | 
| ♦ | | ♠ | | ♦ | 
|__7| |__2| |__2| 

Dealer's Hand: ???
 ___   ___  
|## | |5  | 
|###| | ♦ | 
|_##| |__5| 

                          ----- Dealer Move: Hit -----                         

Player's Hand: 11
 ___   ___   ___  
|7  | |2  | |2  | 
| ♦ | | ♠ | | ♦ | 
|__7| |__2| |__2| 

Dealer's Hand: ???
 ___   ___   ___  
|## | |5  | |8  | 
|###| | ♦ | | ♠ | 
|_##| |__5| |__8| 

                            ----- Final Hands -----                            

Player's Hand: 11
 ___   ___   ___  
|7  | |2  | |2  | 
| ♦ | | ♠ | | ♦ | 
|__7| |__2| |__2| 

Dealer's Hand: 23
 ___   ___   ___  
|J  | |5  | |8  | 
| ♦ | | ♦ | | ♠ | 
|__J| |__5| |__8| 

Dealer Busts! You win!

Wins: 1 | Losses: 0
Player Funds: 120.0

Enter your bet or enter (q)uit to exit:
> 50
Your bet is 50.0

---------------------------------Initial Hands:--------------------------------

Player's Hand: 8
 ___   ___  
|5  | |3  | 
| ♥ | | ♠ | 
|__5| |__3| 

Dealer's Hand: ???
 ___   ___  
|## | |8  | 
|###| | ♠ | 
|_##| |__8| 

Enter (h)it, (s)tand, (d)ouble-down
> h

                          ----- Player Move: Hit -----                         

Player's Hand: 15
 ___   ___   ___  
|5  | |3  | |7  | 
| ♥ | | ♠ | | ♥ | 
|__5| |__3| |__7| 

Dealer's Hand: ???
 ___   ___  
|## | |8  | 
|###| | ♠ | 
|_##| |__8| 

Enter (h)it, (s)tand
> h

                          ----- Player Move: Hit -----                         

Player's Hand: 18
 ___   ___   ___   ___  
|5  | |3  | |7  | |3  | 
| ♥ | | ♠ | | ♥ | | ♦ | 
|__5| |__3| |__7| |__3| 

Dealer's Hand: ???
 ___   ___  
|## | |8  | 
|###| | ♠ | 
|_##| |__8| 

Enter (h)it, (s)tand
> s
                            ----- Final Hands -----                            

Player's Hand: 18
 ___   ___   ___   ___  
|5  | |3  | |7  | |3  | 
| ♥ | | ♠ | | ♥ | | ♦ | 
|__5| |__3| |__7| |__3| 

Dealer's Hand: 18
 ___   ___  
|10 | |8  | 
| ♠ | | ♠ | 
|_10| |__8| 

It's a Tie!

Wins: 1 | Losses: 0
Player Funds: 120.0

Enter your bet or enter (q)uit to exit:
> 50
Your bet is 50.0

---------------------------------Initial Hands:--------------------------------

Player's Hand: 13
 ___   ___  
|4  | |9  | 
| ♥ | | ♥ | 
|__4| |__9| 

Dealer's Hand: ???
 ___   ___  
|## | |8  | 
|###| | ♦ | 
|_##| |__8| 

Enter (h)it, (s)tand, (d)ouble-down
> d
Bet Doubled to 100.0

                          ----- Player Move: Hit -----                         

Player's Hand: 14
 ___   ___   ___  
|4  | |9  | |A  | 
| ♥ | | ♥ | | ♥ | 
|__4| |__9| |__A| 

Dealer's Hand: ???
 ___   ___  
|## | |8  | 
|###| | ♦ | 
|_##| |__8| 

                          ----- Dealer Move: Hit -----                         

Player's Hand: 14
 ___   ___   ___  
|4  | |9  | |A  | 
| ♥ | | ♥ | | ♥ | 
|__4| |__9| |__A| 

Dealer's Hand: ???
 ___   ___   ___  
|## | |8  | |8  | 
|###| | ♦ | | ♥ | 
|_##| |__8| |__8| 

Dealer Move... Press Enter to continue...

                            ----- Final Hands -----                            

Player's Hand: 14
 ___   ___   ___  
|4  | |9  | |A  | 
| ♥ | | ♥ | | ♥ | 
|__4| |__9| |__A| 

Dealer's Hand: 20
 ___   ___   ___  
|4  | |8  | |8  | 
| ♣ | | ♦ | | ♥ | 
|__4| |__8| |__8| 

You Lost!

Wins: 1 | Losses: 1
Player Funds: 20.0

Enter your bet or enter (q)uit to exit:
> 10
Your bet is 10.0

---------------------------------Initial Hands:--------------------------------

Player's Hand: 17
 ___   ___  
|7  | |J  | 
| ♣ | | ♣ | 
|__7| |__J| 

Dealer's Hand: ???
 ___   ___  
|## | |6  | 
|###| | ♦ | 
|_##| |__6| 

Enter (h)it, (s)tand, (d)ouble-down
> h

                          ----- Player Move: Hit -----                         

Player's Hand: 27
 ___   ___   ___  
|7  | |J  | |10 | 
| ♣ | | ♣ | | ♠ | 
|__7| |__J| |_10| 

Dealer's Hand: ???
 ___   ___  
|## | |6  | 
|###| | ♦ | 
|_##| |__6| 

                            ----- Final Hands -----                            

Player's Hand: 27
 ___   ___   ___  
|7  | |J  | |10 | 
| ♣ | | ♣ | | ♠ | 
|__7| |__J| |_10| 

Dealer's Hand: 16
 ___   ___  
|K  | |6  | 
| ♣ | | ♦ | 
|__K| |__6| 

Player Busts! Dealer Wins

Wins: 1 | Losses: 2
Player Funds: 10.0

Enter your bet or enter (q)uit to exit:
> 10
Your bet is 10.0

---------------------------------Initial Hands:--------------------------------

Player's Hand: 19
 ___   ___  
|A  | |8  | 
| ♣ | | ♠ | 
|__A| |__8| 

Dealer's Hand: ???
 ___   ___  
|## | |9  | 
|###| | ♥ | 
|_##| |__9| 

Enter (h)it, (s)tand
> d
Enter (h)it, (s)tand
> h

                          ----- Player Move: Hit -----                         

Player's Hand: 19
 ___   ___   ___  
|A  | |8  | |Q  | 
| ♣ | | ♠ | | ♥ | 
|__A| |__8| |__Q| 

Dealer's Hand: ???
 ___   ___  
|## | |9  | 
|###| | ♥ | 
|_##| |__9| 

Enter (h)it, (s)tand
> s
                            ----- Final Hands -----                            

Player's Hand: 19
 ___   ___   ___  
|A  | |8  | |Q  | 
| ♣ | | ♠ | | ♥ | 
|__A| |__8| |__Q| 

Dealer's Hand: 18
 ___   ___  
|9  | |9  | 
| ♣ | | ♥ | 
|__9| |__9| 

You won!

Wins: 2 | Losses: 2
Player Funds: 20.0

Enter your bet or enter (q)uit to exit:
> 20
Your bet is 20.0

---------------------------------Initial Hands:--------------------------------

Player's Hand: 21
 ___   ___  
|A  | |10 | 
| ♥ | | ♣ | 
|__A| |_10| 

Dealer's Hand: ???
 ___   ___  
|## | |2  | 
|###| | ♥ | 
|_##| |__2| 

Enter (h)it, (s)tand
> h

                          ----- Player Move: Hit -----                         

Player's Hand: 21
 ___   ___   ___  
|A  | |10 | |Q  | 
| ♥ | | ♣ | | ♥ | 
|__A| |_10| |__Q| 

Dealer's Hand: ???
 ___   ___  
|## | |2  | 
|###| | ♥ | 
|_##| |__2| 

Enter (h)it, (s)tand
> h

                          ----- Player Move: Hit -----                         

Player's Hand: 27
 ___   ___   ___   ___  
|A  | |10 | |Q  | |6  | 
| ♥ | | ♣ | | ♥ | | ♥ | 
|__A| |_10| |__Q| |__6| 

Dealer's Hand: ???
 ___   ___  
|## | |2  | 
|###| | ♥ | 
|_##| |__2| 

                            ----- Final Hands -----                            

Player's Hand: 27
 ___   ___   ___   ___  
|A  | |10 | |Q  | |6  | 
| ♥ | | ♣ | | ♥ | | ♥ | 
|__A| |_10| |__Q| |__6| 

Dealer's Hand: 8
 ___   ___  
|6  | |2  | 
| ♦ | | ♥ | 
|__6| |__2| 

Player Busts! Dealer Wins

Wins: 2 | Losses: 3
No funds to continue the game!

```