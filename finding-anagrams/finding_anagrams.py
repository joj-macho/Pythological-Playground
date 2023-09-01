# Import Modules
import os
import sys
import json

# Set Working Directory
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

def main():
    '''Main function for generating anagrams.'''

    print('\nWelcome to Finding Anagrams.\n')
    
    # Load the dictionary
    words_dict = load_dictionary('words_dictionary.json')

    # Ask the user for a word to find anagrams
    word = input('Enter a word or name to find its anagrams:\n> ')

    # Get the anagrams for the given word
    anagrams = get_anagrams(word, words_dict)

    # Print the anagrams
    if len(anagrams) == 0:
        print(f'No anagrams found for the word {word}')
    else:
        print(f'The anagrams for the word {word} are:')
        for anagram in anagrams:
            print(anagram)

def load_dictionary(file_name):
    '''This function takes a file name as an argument, reads the file using the json.load() method and returns the loaded data.'''

    # Open and read the JSON file
    with open(file_name) as file:
        data = json.load(file)
    return data

def get_anagrams(word, words_dict):
    '''This function finds all single-word anagrams of a given word and returns a list of all single-word anagrams of the given word.'''

    # Create a dictionary to store the letter count of the input word
    word_dict = {}

    # Count the occurrences of each letter in the input word
    for letter in word.lower():
        word_dict[letter] = word_dict.get(letter, 0) + 1

    # Initialize an empty list to store anagrams
    anagrams = []

    # Iterate through words in the loaded dictionary
    for dict_word in words_dict:
        dict_word_dict = {}

        # Count the occurrences of each letter in the dictionary word
        for letter in dict_word.lower():
            dict_word_dict[letter] = dict_word_dict.get(letter, 0) + 1

        # Check if the dictionary word is an anagram of the input word
        if dict_word_dict == word_dict and dict_word != word:
            anagrams.append(dict_word)

    return anagrams


if __name__ == '__main__':
    main()
