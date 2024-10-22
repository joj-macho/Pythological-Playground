import random

# Dictionary mapping for char to leet char
CHAR_MAPPING = {
    'a': ['@'],
    'b': ['8', '|3'],
    'c': ['[', '<'],
    'd': ['|)'],
    'g': ['9'],
    'i': ['1', '!'],
    'j': ['_|'],
    'k': ['|<', '|{'],
    'l': ['|', '|_'],
    'o': ['0', '()'],
    'p': ['|D', '|*', '|o'],
    's': ['$', '5', '§'],
    't': ['7', '+'],
    'v': ['\\/'],
    'z': ['2', '7_']
}


def main():
    '''Converts English text to Leetspeak.'''
    print('Leetspeak Converter.\n')

    while True:
        english = input('Enter your message or (q) to quit: ').strip()

        if english.lower() in ('q', 'quit'):
            print('Bye!')
            break

        if english:
            leetspeak = convert_to_leetspeak(english)
            print('Leetspeak:', leetspeak, '\n')
        else:
            print('Invalid input. Please try again.\n')


def convert_to_leetspeak(message):
    '''Converts the given English string to Leetspeak.'''
    leetspeak = ''

    # Check if the character has Leetspeak replacements
    # and randomly decide whether to replace it
    for char in message:
        if char.lower() in CHAR_MAPPING and random.random() <= 0.60:
            possible_leet_replacements = CHAR_MAPPING[char.lower()]
            leet_replacement = random.choice(possible_leet_replacements)
            leetspeak += leet_replacement
        else:
            leetspeak += char

    return leetspeak


if __name__ == '__main__':
    main()
