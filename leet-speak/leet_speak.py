import random

# Dictionary that maps characters to their possible Leetspeak replacements
CHAR_MAPPING = {
    'a': ['4', '@'],
    'b': ['8', '|3'],
    'c': ['(', '[', '<'],
    'd': ['|)', '|>'],
    'f': ['ph', '|#'],
    'g': ['6', '9'],
    'i': ['1', '!'],
    'j': ['_|', '_/'],
    'k': [']<', '|<', '|{'],
    'l': ['|', '|_'],
    'o': ['0', '()', '[]'],
    'p': ['|D', '|>', '|*', '|o'],
    'r': ['|2', '|?', '/2'],
    's': ['$', '5', 'z', 'Z', '§'],
    't': ['7', '+', '7`', '~|~'],
    'v': ['\\/'],
    'z': ['2', '7_']
}


def main():
    '''This is the main function that converts English text to Leetspeak and displays the result.'''

    print('\nWelcome to Leetspeak.\n')

    english = get_user_input('Enter your message: ')
    leetspeak = convert_to_leetspeak(english)
    print('Leetspeak:', leetspeak)


def get_user_input(prompt):
    '''This function prompts the user for input and return the input string.'''

    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print('Invalid input. Please try again.')


def convert_to_leetspeak(message):
    '''This function converts the given English string to Leetspeak string.'''

    leetspeak = ''
    # Check if the character has Leetspeak replacements and randomly decide whether to replace it
    for char in message:
        if char.lower() in CHAR_MAPPING and random.random() <= 0.70:
            possible_leet_replacements = CHAR_MAPPING[char.lower()]
            leet_replacement = random.choice(possible_leet_replacements)
            leetspeak += leet_replacement
        else:
            leetspeak += char

    return leetspeak


if __name__ == '__main__':
    main()
