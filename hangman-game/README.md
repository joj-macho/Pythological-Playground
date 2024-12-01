# Hangman Game

## Description

The Hangman Game program is an implementation of the classic word-guessing game, where user tries to guess a secret word one letter at a time, with each incorrect guess resulting in the gradual drawing of a hangman figure.

## How it Works

- Following the Hangman game rules, enter the guess of the letter of a secret word.
- The prgoram will display the current state of the game including the hangman picture, missed letters, and correctly guessed letters of the secret word.
- Do this until win or until hanged-man fully drawn.

## Running the Program

```bash
# Navigate to the project directory
cd hangman-game/

# Run the main script
python3 hangman.py
```

## Program Input & Output

When you run the program `hangman.py`, the output will look like this;

```
H A N G M A N
The secret word is in the set: Vegetables

         +---+
             |
             |
             |
            ===

Missed letters: 

_ _ _ _ _ _ _ _ _ _ _ 
Guess a letter: b
The secret word is in the set: Vegetables

         +---+
         O   |
             |
             |
            ===

Missed letters: b

_ _ _ _ _ _ _ _ _ _ _ 
Guess a letter: e
The secret word is in the set: Vegetables

         +---+
         O   |
             |
             |
            ===

Missed letters: b

_ _ _ _ _ _ _ _ _ e _ 
Guess a letter: a
The secret word is in the set: Vegetables

         +---+
         O   |
             |
             |
            ===

Missed letters: b

_ a _ _ _ _ _ _ _ e _ 
Guess a letter: u
The secret word is in the set: Vegetables

         +---+
         O   |
             |
             |
            ===

Missed letters: b

_ a u _ _ _ _ _ _ e _ 
Guess a letter: r
The secret word is in the set: Vegetables

         +---+
         O   |
             |
             |
            ===

Missed letters: b

_ a u _ _ _ _ _ _ e r 
Guess a letter: c
The secret word is in the set: Vegetables

         +---+
         O   |
             |
             |
            ===

Missed letters: b

c a u _ _ _ _ _ _ e r 
Guess a letter: l
The secret word is in the set: Vegetables

         +---+
         O   |
             |
             |
            ===

Missed letters: b

c a u l _ _ l _ _ e r 
Guess a letter: i
The secret word is in the set: Vegetables

         +---+
         O   |
             |
             |
            ===

Missed letters: b

c a u l i _ l _ _ e r 
Guess a letter: f
The secret word is in the set: Vegetables

         +---+
         O   |
             |
             |
            ===

Missed letters: b

c a u l i f l _ _ e r 
Guess a letter: o
The secret word is in the set: Vegetables

         +---+
         O   |
             |
             |
            ===

Missed letters: b

c a u l i f l o _ e r 
Guess a letter: w
Yes! The secret word is "cauliflower"! You have won!
Do you want to play again? (yes or no): y
The secret word is in the set: Shapes

         +---+
             |
             |
             |
            ===

Missed letters: 

_ _ _ _ _ _ _ _ _ 
Guess a letter: e
The secret word is in the set: Shapes

         +---+
             |
             |
             |
            ===

Missed letters: 

_ e _ _ _ _ _ _ e 
Guess a letter: o
The secret word is in the set: Shapes

         +---+
         O   |
             |
             |
            ===

Missed letters: o

_ e _ _ _ _ _ _ e 
Guess a letter: i
The secret word is in the set: Shapes

         +---+
         O   |
         |   |
             |
            ===

Missed letters: o i

_ e _ _ _ _ _ _ e 
Guess a letter: h
The secret word is in the set: Shapes

         +---+
         O   |
        /|   |
             |
            ===

Missed letters: o i h

_ e _ _ _ _ _ _ e 
Guess a letter: r
The secret word is in the set: Shapes

         +---+
         O   |
        /|   |
             |
            ===

Missed letters: o i h

r e _ _ _ _ _ _ e 
Guess a letter: c
The secret word is in the set: Shapes

         +---+
         O   |
        /|   |
             |
            ===

Missed letters: o i h

r e c _ _ _ _ _ e 
Guess a letter: t
The secret word is in the set: Shapes

         +---+
         O   |
        /|   |
             |
            ===

Missed letters: o i h

r e c t _ _ _ _ e 
Guess a letter: j
The secret word is in the set: Shapes

         +---+
         O   |
        /|\  |
             |
            ===

Missed letters: o i h j

r e c t _ _ _ _ e 
Guess a letter: e
You have already guessed that letter. Choose again.
Guess a letter: dds
Please enter a single letter.
Guess a letter: l
The secret word is in the set: Shapes

         +---+
         O   |
        /|\  |
             |
            ===

Missed letters: o i h j

r e c t _ _ _ l e 
Guess a letter: a
The secret word is in the set: Shapes

         +---+
         O   |
        /|\  |
             |
            ===

Missed letters: o i h j

r e c t a _ _ l e 
Guess a letter: n
The secret word is in the set: Shapes

         +---+
         O   |
        /|\  |
             |
            ===

Missed letters: o i h j

r e c t a n _ l e 
Guess a letter: g
Yes! The secret word is "rectangle"! You have won!
Do you want to play again? (yes or no): y
The secret word is in the set: Sports

         +---+
             |
             |
             |
            ===

Missed letters: 

_ _ _ _ 
Guess a letter: q
The secret word is in the set: Sports

         +---+
         O   |
             |
             |
            ===

Missed letters: q

_ _ _ _ 
Guess a letter: w
The secret word is in the set: Sports

         +---+
         O   |
         |   |
             |
            ===

Missed letters: q w

_ _ _ _ 
Guess a letter: e
The secret word is in the set: Sports

         +---+
         O   |
        /|   |
             |
            ===

Missed letters: q w e

_ _ _ _ 
Guess a letter: r
The secret word is in the set: Sports

         +---+
         O   |
        /|\  |
             |
            ===

Missed letters: q w e r

_ _ _ _ 
Guess a letter: t
The secret word is in the set: Sports

         +---+
         O   |
        /|\  |
        /    |
            ===

Missed letters: q w e r t

_ _ _ _ 
Guess a letter: y
The secret word is in the set: Sports

         +---+
         O   |
        /|\  |
        / \  |
            ===

Missed letters: q w e r t y

_ _ _ _ 
Guess a letter: u
The secret word is in the set: Sports

         +---+
        [O   |
        /|\  |
        / \  |
            ===

Missed letters: q w e r t y u

_ _ _ _ 
Guess a letter: i

         +---+
        [O]  |
        /|\  |
        / \  |
            ===

Missed letters: q w e r t y u i

_ _ _ _ 
You have run out of guesses!
After 8 missed guesses and 0 correct guesses, the word was " golf "
Do you want to play again? (yes or no): n
```
