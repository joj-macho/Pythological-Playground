from pathlib import Path
import json
import sys

BASE_PATH = Path(__file__).resolve().parent


def main():
    print('Anagram Finder\n')

    dict_path = BASE_PATH / 'words_dictionary.json'
    words_dict = load_dictionary(dict_path)
    if words_dict is None:
        sys.exit(1)

    while True:
        word = input(
                'Enter a word to find its anagrams (or (q)uit to exit):\n> '
                )
        word = word.strip()
        if word.lower() in ('q', 'quit'):
            print('Bye!')
            break

        anagrams = find_anagrams(word, words_dict)
        if not anagrams:
            print(f'No anagrams found for the word "{word}".\n')
        else:
            print(f'The anagrams for the word "{word}" are:')
            for anagram in anagrams:
                print(f'- {anagram}')
            print()


def load_dictionary(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'Error: The file "{file_path}" does not exist.')
    except json.JSONDecodeError:
        print(f'Error: The file "{file_path}" is not a valid JSON file.')
    return None


def find_anagrams(word, words_dict):
    word = word.lower()
    sorted_word = ''.join(sorted(word))
    anagrams = []

    for dict_word in words_dict:
        if (dict_word.lower() != word) and \
                (''.join(sorted(dict_word.lower())) == sorted_word):
            anagrams.append(dict_word)

    return anagrams


if __name__ == '__main__':
    main()
