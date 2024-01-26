# Finding Palindromes

## Description

Palindromes are words, phrases, or sentences that read the same backward as forward.

This program is a simple Python script that works with a dictionary of words, in JSON format to find and display palindromes.

This Python program reads words from a dictionary file (`words_dictionary.json`). You can download the dictionary file [here]('https://github.com/dwyl/english-words/blob/master/words_dictionary.json')

## How it Works

- The program uses the `os` and `sys` modules to set the working directory to the directory where the script is located, and `json` is used to load the dictionary of words from the JSON file. The `random` module is used to select a random palindrome from the dictionary.

- The `main()` function loads the dictionary, prompts the user to enter a word, checks if the word is a palindrome using the `is_palindrome()` function and displays a random palindrome from the dictionary using the `get_random_palindrome()` function.

- The `load_dictionary()` function loads the dictionary of English words from the `words_dictionary.json` file. This function loads the data using the `json.load(file)` method and returns the loaded dictionary.

- The `is_palindrome()` function checks if a given word is a palindrome. The function takes a string `word` as an argument and checks if the length of the word is greater than 1 and if the word is equal to its reverse, which is obtained using the slice notation `[::-1]`. If the word is a palindrome, the function returns `True`, otherwise, it returns `False`.

- The `get_random_palindrome()` function selects a random palindrome from the dictionary. The function takes a dictionary `words_dict` as an argument and uses a list comprehension to create a list of palindromes from the dictionary using the `is_palindrome()` function. If the list of palindromes is not empty, the function selects a random palindrome from the list using the `random.choice()` method and returns it. Otherwise, it returns `None`.

## Program Input & Output

When you run the program `find_palindromes.py`, the output will look like this;

```

Welcome To Palindrome Checker.

Enter a word to check if it is a palindrome:
> rotator
rotator is a palindrome!

Here is a random palindrome from the dictionary: mum

...

Welcome To Palindrome Checker.

Enter a word to check if it is a palindrome:
> dog
dog is not a palindrome.

Here is a random palindrome from the dictionary: abba
```






