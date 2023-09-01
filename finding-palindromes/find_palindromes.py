import os
import sys
import json
import random

# Set Working Directory
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

# Main Function
def main():
    '''Main function for checking and generating palindromes.'''

    print('\nWelcome To Palindrome Checker.\n')

    # Load the dictionary
    words_dict = load_dictionary('words_dictionary.json')

    # Ask the user for a word and check if it's a palindrome
    word = input('Enter a word to check if it is a palindrome:\n> ')
    if is_palindrome(word):
        print(f'{word} is a palindrome!')
    else:
        print(f'{word} is not a palindrome.')

    # Print a random palindrome from the dictionary
    random_palindrome = get_random_palindrome(words_dict)
    print(f'\nHere is a random palindrome from the dictionary: {random_palindrome}')


def load_dictionary(file_name):
    '''Load a dictionary from a JSON file and return it.'''

    with open(file_name) as file:
        data = json.load(file)

    return data

def is_palindrome(word):
    '''Check if a given word is a palindrome.'''

    return len(word) > 1 and word == word[::-1]

def get_random_palindrome(words_dict):
    '''Get a random palindrome from a dictionary of words.'''

    palindromes = [word for word in words_dict if is_palindrome(word)]
    return random.choice(palindromes)


if __name__ == '__main__':
    main()
