# Hangman Game

## Description

The Hangman Game program is a text-based implementation of the classic word-guessing game. In this game, players try to guess a secret word one letter at a time, with each incorrect guess resulting in the gradual drawing of a hangman figure. The objective is to guess the word before the hangman is fully drawn. This program provides an interactive interface for players to enjoy this challenging word puzzle game.

## How it Works

- The program first imports the `random` module which is used to choose random words and ASCII art for the hangman.

- The program begins by defining a class called `Hangman`. Inside this class, it has several variables, including:
    - `HANGMAN_ART`: A list containing ASCII art representations of the hangman figure in different stages. These figures visually depict the player's progress.
    - `WORDS`: A list of tuples, where each tuple contains a category name and a list of words associated with that category.

- The `Hangman` class has an `__init__` method that initializes the game state. It sets the initial values for variables like `missed_letters`, `correct_letters`, `secret_word`, `secret_set`, and `is_game_over`. These variables are crucial for tracking and controlling the game's flow.

- The class provides several methods to handle various aspects of the game:
    - `generate_random_word`: Selects a random word from a random category in the `WORDS` list.
    - `display_board:` Displays the hangman ASCII art, the missed letters, and the current state of the word with blanks for unguessed letters.
    - `generate_guess`: Prompts the user to enter a single letter as their guess and performs input validation.
    - `play_again`: Asks the user if they want to play again and returns True if the response starts with 'y'.

- The `main` method is where the actual game loop is implemented. Inside the main game loop, it displays the current state of the hangman, prompts the user for a guess, and checks if the guess is correct. It updates the `correct_letters` or `missed_letters` accordingly. If the user has guessed all the letters in the `secret_word`, it declares the user as the winner. If the user has missed too many guesses, it declares the user as the loser.

- After each game round, the program checks if the player wants to play another round. If the player chooses to continue, the game state is reset, and a new random word is chosen. If not, the game ends.

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
