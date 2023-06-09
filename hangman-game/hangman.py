import random

class Hangman:
    HANGMAN_ART = [
        '''
         +---+
             |
             |
             |
            ===''', '''
         +---+
         O   |
             |
             |
            ===''', '''
         +---+
         O   |
         |   |
             |
            ===''', '''
         +---+
         O   |
        /|   |
             |
            ===''', '''
         +---+
         O   |
        /|\  |
             |
            ===''', '''
         +---+
         O   |
        /|\  |
        /    |
            ===''', '''
         +---+
         O   |
        /|\  |
        / \  |
            ===''', '''
         +---+
        [O   |
        /|\  |
        / \  |
            ===''', '''
         +---+
        [O]  |
        /|\  |
        / \  |
            ==='''
    ]

    # Word categories and their corresponding word lists
    WORDS = [
    ('Colors', 'red orange yellow green blue indigo violet white black brown'.split()),
    ('Animals', 'cat dog lion elephant giraffe monkey tiger bear panda kangaroo dolphin penguin owl snake turtle bee'.split()),
    ('Shapes', 'circle square triangle rectangle oval diamond star heart crescent pentagon hexagon octagon'.split()),
    ('Fruits', 'apple orange banana strawberry watermelon pineapple mango grape cherry lemon pear kiwi peach'.split()),
    ('Vegetables', 'carrot broccoli cucumber spinach potato tomato onion garlic celery pumpkin zucchini eggplant radish cauliflower cabbage'.split()),
    ('Sports', 'soccer basketball tennis baseball golf volleyball cricket rugby badminton swimming cycling boxing skiing gymnastics surfing'.split()),
    ('Countries', 'afghanistan albania algeria argentina australia brazil canada china denmark egypt france germany india italy japan kenya mexico netherlands pakistan qatar russia spain turkey united states vietnam yemen zimbabwe'.split()),
    ('Emotions/Feelings', 'happy sad angry excited surprised nervous proud confident calm curious jealous bored'.split()),
    ('School Subjects', 'math science history geography English literature art music physical education chemistry biology physics'.split()),
    ('Body Parts', 'head arm leg hand foot eye ear nose mouth hair face shoulder knee stomach chest back'.split()),
    ('Weather', 'sunny rainy cloudy windy stormy snowy foggy hot cold humid dry'.split()),
    ('Jobs/Occupations', 'doctor teacher engineer chef firefighter police musician actor artist lawyer nurse pilot scientist writer'.split())
]

    def __init__(self):
        '''Initialize the Hangman game.'''

        # Strings to store missed letters and correct letters
        self.missed_letters = ''
        self.correct_letters = ''
        # Generate a random word and set
        self.secret_word, self.secret_set = self.generate_random_word()
        # Flag to indicate if the game is over
        self.is_game_over = False

    def generate_random_word(self):
        '''This function generates a random word and its corresponding set from the WORDS list.'''

        # Select a random word set and random word from the set
        word_set = random.choice(self.WORDS)
        word = random.choice(word_set[1])
        return word, word_set[0]

    def display_board(self):
        '''This function displays the hangman art, missed letters, and current word progress.'''

        print(self.HANGMAN_ART[len(self.missed_letters)])
        print()

        print('Missed letters:', ' '.join(self.missed_letters))
        print()

        blanks = '_' * len(self.secret_word)
        for i, letter in enumerate(self.secret_word):
            if letter in self.correct_letters:
                blanks = blanks[:i] + letter + blanks[i+1:]

        for letter in blanks:
            print(letter, end=' ')
        print()

    def generate_guess(self):
        '''This function prompts the player to enter a guess and validate the input.'''

        while True:
            guess = input('Guess a letter: ').lower()
            if len(guess) != 1:
                print('Please enter a single letter.')
            elif guess in self.correct_letters or guess in self.missed_letters:
                print('You have already guessed that letter. Choose again.')
            elif not guess.isalpha():
                print('Please enter a LETTER.')
            else:
                return guess

    def play_again(self):
        '''This function prompts the player to play again.'''

        response = input('Do you want to play again? (yes or no): ').lower()
        return response.startswith('y')

    def play(self):
        '''This is the main play function that starts the Hangman game.'''

        print('\nWelcome to Hangman.\n')

        difficulty = ''
        while difficulty not in 'EMH':
            difficulty = input('Enter difficulty: E - Easy, M - Medium, H - Hard: ').upper()

        if difficulty == 'M':
            del self.HANGMAN_ART[8]
            del self.HANGMAN_ART[7]
        elif difficulty == 'H':
            del self.HANGMAN_ART[8]
            del self.HANGMAN_ART[7]
            del self.HANGMAN_ART[5]
            del self.HANGMAN_ART[3]

        while True:
            print('The secret word is in the set:', self.secret_set)
            self.display_board()

            guess = self.generate_guess()

            if guess in self.secret_word:
                self.correct_letters += guess

                if all(letter in self.correct_letters for letter in self.secret_word):
                    print('Yes! The secret word is "' + self.secret_word + '"! You have won!')
                    self.is_game_over = True
            else:
                self.missed_letters += guess

                if len(self.missed_letters) == len(self.HANGMAN_ART) - 1:
                    self.display_board()
                    print('You have run out of guesses!\nAfter', len(self.missed_letters), 'missed guesses and', len(self.correct_letters), 'correct guesses, the word was "', self.secret_word, '"')
                    self.is_game_over = True

            if self.is_game_over:
                if self.play_again():
                    self.missed_letters = ''
                    self.correct_letters = ''
                    self.is_game_over = False
                    self.secret_word, self.secret_set = self.generate_random_word()
                else:
                    break

hangman = Hangman()
hangman.play()
