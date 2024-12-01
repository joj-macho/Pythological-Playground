import random

# Hangman ASCII Art
HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===
    ''',
    '''
     +---+
     O   |
         |
         |
        ===
    ''',
    '''
     +---+
     O   |
     |   |
         |
        ===
    ''',
    '''
     +---+
     O   |
    /|   |
         |
        ===
    ''',
    '''
     +---+
     O   |
    /|\\  |
         |
        ===
    ''',
    '''
     +---+
     O   |
    /|\\  |
    /    |
        ===
    ''',
    '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    '''
]

# List of words to choose from for the game
WORDS = [
    'attack',
    'training',
    'musical',
    'retire',
    'eliminate',
    'rally',
    'mainstream',
    'climb',
    'handicap',
    'flag',
    'unit',
    'share',
    'courtesy',
    'continuation',
    'litigation',
    'suspect',
    'observation',
    'swallow',
    'pleasure',
    'supplementary',
    'conglomerate',
    'conviction',
    'win',
    'orgy',
    'rugby']


def main():
    print('Hangman Game\n')
    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word(WORDS)
    game_over = False

    while True:
        display_game_state(
            HANGMAN_PICS,
            missed_letters,
            correct_letters,
            secret_word)

        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters += guess

            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print(
                    f'The secret word is \'{secret_word}\'! You won!')
                game_over = True
        else:
            missed_letters += guess

            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_game_state(
                    HANGMAN_PICS,
                    missed_letters,
                    correct_letters,
                    secret_word)
                print(f'You have run out of guesses!\nAfter '
                      f'{str(len(missed_letters))} missed guesses and '
                      f'{str(len(correct_letters))} correct guesses, '
                      f'the word was \'{secret_word}\'')
                game_over = True

        if game_over:
            print('Do you want to play again? (yes or no)')
            if input().lower().startswith('y'):
                missed_letters = ''
                correct_letters = ''
                game_over = False
                secret_word = get_random_word(WORDS)
            else:
                break


def get_random_word(word_list):
    return random.choice(word_list)


def display_game_state(HANGMAN_PICS, missed_letters,
                       correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])

    print('\nMissed letters: ', end='')
    for letter in missed_letters:
        print(letter, end=' ')
    print('\n')

    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)
                   ):  # Replace blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
    print('\n')


def get_guess(already_guessed):
    while True:
        print('Guess a letter:')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a letter.')
        else:
            return guess


if __name__ == '__main__':
    main()
