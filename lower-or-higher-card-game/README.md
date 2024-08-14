# Lower or Higher Card Game

## Description

The "Lower or Higher Card Game" program is a card guessing game where the player guesses whether the next card in a deck will be higher or lower than the current card shown. The goal is to make correct guesses to maximize the score.

### How It Works

- The player starts with 100 points.
- The game shows one card face-up.
- Each round, the player guesses whether the next card will be higher or lower than the current card.
- The player gains 15 points for a correct guess, and loses 10 points for an incorrect guess.
- After each guess, the game reveals the next card and adjusts the points accordingly.
- The new card becomes the current card for the next round.
- The game ends when all cards in the deck are revealed.

## Running the Program

```bash
# Navigate to the project directory
cd lower-or-higher-card-game/

# Run the main script
python3 main.py
```

## Program Input & Output

When you run `main.py`, the output will look like this:

```
Welcome to the Lower or Higher Card Game!

You start with 100 points. Gain 15 points for a correct answer, lose 10
points for an incorrect answer.

Game Rules:
    - You will be shown one card face up.
    - Each round, you guess whether the next card will be higher or lower.
    - Points are adjusted based on your guess.
    - The game ends when all cards are revealed.

Let's begin!

----------------------------------ATTEMPT 1-----------------------------------
Current card: 6 of Diamonds ♦
 ___   ___   ___   ___   ___   ___   ___   ___  
|6  | |## | |## | |## | |## | |## | |## | |## | 
| ♦ | |###| |###| |###| |###| |###| |###| |###| 
|__6| |_##| |_##| |_##| |_##| |_##| |_##| |_##| 

Is the next card (l)ower or (h)igher? Enter (q)uit to exit.
> h

Correct! +15 Points.
The next card, 8 of Clubs ♣, is higher.
Your points: 115
Cards remaining: 6

----------------------------------ATTEMPT 2-----------------------------------
Current card: 8 of Clubs ♣
 ___   ___   ___   ___   ___   ___   ___   ___  
|6  | |8  | |## | |## | |## | |## | |## | |## | 
| ♦ | | ♣ | |###| |###| |###| |###| |###| |###| 
|__6| |__8| |_##| |_##| |_##| |_##| |_##| |_##| 

Is the next card (l)ower or (h)igher? Enter (q)uit to exit.
> l

Incorrect! -10 Points.
The next card, Q of Spades ♠, is higher
Your points: 105
Cards remaining: 5

----------------------------------ATTEMPT 3-----------------------------------
Current card: Q of Spades ♠
 ___   ___   ___   ___   ___   ___   ___   ___  
|6  | |8  | |Q  | |## | |## | |## | |## | |## | 
| ♦ | | ♣ | | ♠ | |###| |###| |###| |###| |###| 
|__6| |__8| |__Q| |_##| |_##| |_##| |_##| |_##| 

Is the next card (l)ower or (h)igher? Enter (q)uit to exit.
> l

Correct! +15 Points.
The next card, A of Diamonds ♦, is lower.
Your points: 120
Cards remaining: 4

----------------------------------ATTEMPT 4-----------------------------------
Current card: A of Diamonds ♦
 ___   ___   ___   ___   ___   ___   ___   ___  
|6  | |8  | |Q  | |A  | |## | |## | |## | |## | 
| ♦ | | ♣ | | ♠ | | ♦ | |###| |###| |###| |###| 
|__6| |__8| |__Q| |__A| |_##| |_##| |_##| |_##| 

Is the next card (l)ower or (h)igher? Enter (q)uit to exit.
> h

Correct! +15 Points.
The next card, 3 of Clubs ♣, is higher.
Your points: 135
Cards remaining: 3

----------------------------------ATTEMPT 5-----------------------------------
Current card: 3 of Clubs ♣
 ___   ___   ___   ___   ___   ___   ___   ___  
|6  | |8  | |Q  | |A  | |3  | |## | |## | |## | 
| ♦ | | ♣ | | ♠ | | ♦ | | ♣ | |###| |###| |###| 
|__6| |__8| |__Q| |__A| |__3| |_##| |_##| |_##| 

Is the next card (l)ower or (h)igher? Enter (q)uit to exit.
> h

Correct! +15 Points.
The next card, J of Clubs ♣, is higher.
Your points: 150
Cards remaining: 2

----------------------------------ATTEMPT 6-----------------------------------
Current card: J of Clubs ♣
 ___   ___   ___   ___   ___   ___   ___   ___  
|6  | |8  | |Q  | |A  | |3  | |J  | |## | |## | 
| ♦ | | ♣ | | ♠ | | ♦ | | ♣ | | ♣ | |###| |###| 
|__6| |__8| |__Q| |__A| |__3| |__J| |_##| |_##| 

Is the next card (l)ower or (h)igher? Enter (q)uit to exit.
> l

Correct! +15 Points.
The next card, A of Spades ♠, is lower.
Your points: 165
Cards remaining: 1

----------------------------------ATTEMPT 7-----------------------------------
Current card: A of Spades ♠
 ___   ___   ___   ___   ___   ___   ___   ___  
|6  | |8  | |Q  | |A  | |3  | |J  | |A  | |## | 
| ♦ | | ♣ | | ♠ | | ♦ | | ♣ | | ♣ | | ♠ | |###| 
|__6| |__8| |__Q| |__A| |__3| |__J| |__A| |_##| 

Is the next card (l)ower or (h)igher? Enter (q)uit to exit.
> h

Correct! +15 Points.
The next card, 8 of Spades ♠, is higher.
Your points: 180
Cards remaining: 0

Final card: 8 of Spades ♠
 ___   ___   ___   ___   ___   ___   ___   ___  
|6  | |8  | |Q  | |A  | |3  | |J  | |A  | |8  | 
| ♦ | | ♣ | | ♠ | | ♦ | | ♣ | | ♣ | | ♠ | | ♠ | 
|__6| |__8| |__Q| |__A| |__3| |__J| |__A| |__8| 

GAME OVER!
Final Points: 180 | Correct Guesses: 6 | Wrong Guesses: 1 | Ties: 0

Play again? Enter (y)es or (n)o:
> y

Playing Another Round!
----------------------------------ATTEMPT 1-----------------------------------
Current card: 2 of Diamonds ♦
 ___   ___   ___   ___   ___   ___   ___   ___  
|2  | |## | |## | |## | |## | |## | |## | |## | 
| ♦ | |###| |###| |###| |###| |###| |###| |###| 
|__2| |_##| |_##| |_##| |_##| |_##| |_##| |_##| 

Is the next card (l)ower or (h)igher? Enter (q)uit to exit.
> h

Correct! +15 Points.
The next card, 9 of Clubs ♣, is higher.
Your points: 115
Cards remaining: 6

----------------------------------ATTEMPT 2-----------------------------------
Current card: 9 of Clubs ♣
 ___   ___   ___   ___   ___   ___   ___   ___  
|2  | |9  | |## | |## | |## | |## | |## | |## | 
| ♦ | | ♣ | |###| |###| |###| |###| |###| |###| 
|__2| |__9| |_##| |_##| |_##| |_##| |_##| |_##| 

Is the next card (l)ower or (h)igher? Enter (q)uit to exit.
> q

Exiting game... Bye!

```