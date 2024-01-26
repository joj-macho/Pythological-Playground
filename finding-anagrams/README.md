# Finding Anagrams

## Description

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, the word "listen" is an anagram of the word "silent".

This Python program reads words from a dictionary file (`words_dictionary.json`) and generates a list of anagrams for a given input word. You can download the dictionary file [here]('https://github.com/dwyl/english-words/blob/master/words_dictionary.json')

## How it Works

- The program uses the `os` and `sys` modules to set the working directory to the directory where the script is located, and `json` is used to load the dictionary of words from the JSON file.

- The `main()` function loads the dictionary, prompts the user to enter a word or name for which they want to find the anagrams, then finds all single-word anagrams of the entered word. Finally this function prints out the list of anagrams. If no anagrams are found, the program prints a message indicating that no anagrams were found.

- The `load_dictionary()` function loads the dictionary of English words from the `words_dictionary.json` file. This function loads the data using the `json.load(file)` method and returns the loaded dictionary.

- The `get_anagrams()` function finds all single-word anagrams of the entered word using the dictionary. The function first creates a dictionary called `word_dict` that contains the count of each letter in the entered word or name. Then goes through each word in the dictionary and creates a similar dictionary called `dict_word_dict` that contains the count of each letter in the dictionary word. If `dict_word_dict` is equal to `word_dict` and the dictionary word is not equal to the entered word, then the dictionary word is an anagram of the entered word, and is added to a list called `anagrams`. The program then prints out the list of anagrams.

## Program Input & Output

When you run the program `finding_anagrams.py`, the output will look like this;

```

Welcome to Finding Anagrams.

Enter a word or name to find its anagrams:
> python
The anagrams for the word python are:
phyton
typhon

...

Welcome to Finding Anagrams.

Enter a word or name to find its anagrams:
> lives
The anagrams for the word lives are:
elvis
evils
levis
slive
veils

...

Welcome to Finding Anagrams.

Enter a word or name to find its anagrams:
> yelp
No anagrams found for the word yelp
```
