'''This program find palindromes from a dictionary file.'''
'Use Python to search an English language dictionary file for palindromes.'

# Import Modules
import os
import sys
import json
import random

# Set Working Directory
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

# Main Function
def main():
    '''This is the main function of the program'''

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
    '''This function takes a file name as an argument, reads the file using the json.load() method and returns the loaded data.'''

    with open(file_name) as file:
        data = json.load(file)
    return data

def is_palindrome(word):
    '''This function checks if a given word is a palindrome by comparing the word with its reverse. It returns True if the word is a palindrome and False otherwise.'''

    return len(word) > 1 and word == word[::-1]

def get_random_palindrome(words_dict):
    '''This function takes a dictionary of words as an argument and returns a random palindrome from the dictionary.'''

    palindromes = [word for word in words_dict if is_palindrome(word)]
    return random.choice(palindromes)



if __name__ == '__main__':
    main()
