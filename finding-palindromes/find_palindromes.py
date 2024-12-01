from pathlib import Path
import json
import sys

BASE_PATH = Path(__file__).resolve().parent


def main():
    print('Palindrome Finder\n')

    dict_path = BASE_PATH / 'words_dictionary.json'
    words_dict = load_dictionary(dict_path)
    if words_dict is None:
        sys.exit(1)

    while True:
        word = input(
            'Enter a word to chec palindromes (or (q)uit to exit):\n> '
        ).strip()
        if word.lower() in ('q', 'quit'):
            print('Bye!')
            break

        if is_palindrome(word):
            print(f'The word "{word}" is a palindrome.')
        else:
            print(f'The word "{word}" is not a palindrome.')

        found_palindromes = find_palindromes(word, words_dict)
        if not found_palindromes:
            print(f'No related palindromes found for the word "{word}".\n')
        else:
            print(f'Palindromes related to the word "{word}" are:')
            for palindrome in found_palindromes:
                print(f'- {palindrome}')
            print()

        show_all = input(
            'Want to see all palindromes in the dictionary? (y/n): '
        ).strip().lower()
        if show_all in ('y', 'yes'):
            all_palindromes = find_all_palindromes(words_dict)
            print('Here are all palindromes from the dictionary:')
            for palindrome in all_palindromes:
                print(f'- {palindrome}')
            print()


def load_dictionary(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(json.load(file).keys())
    except FileNotFoundError:
        print(f'Error: The file "{file_path}" does not exist.')
    except json.JSONDecodeError:
        print(f'Error: The file "{file_path}" is not a valid JSON file.')
    return None


def is_palindrome(word):
    word = word.lower()
    return len(word) > 1 and word == word[::-1]


def find_palindromes(word, words_dict):
    word_lower = word.lower()
    return [
        dict_word for dict_word in words_dict
        if dict_word.lower() != word_lower and is_palindrome(dict_word)
    ]


def find_all_palindromes(words_dict):
    return [word for word in words_dict if is_palindrome(word)]


if __name__ == '__main__':
    main()
