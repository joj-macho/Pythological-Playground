# Finding Anagrams

## Description

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, the word "listen" is an anagram of the word "silent".

This Python program reads words from a dictionary file called `words_dictionary.json` and generates a list of anagrams for a given input word.

## How it Works

- The program begins by importing neccessary modules, including <code>os</code>, <code>sys</code>, and <code>json</code>. The <code>os</code> and <code>sys</code> modules are used to set the working directory to the directory where the script is located, and <code>json</code> is used to load the dictionary of words from the JSON file.

- The <code>main()</code> function begins by printing the welcome message. The function loads the dictionary, prompts the user to enter a word or name for which they want to find the anagrams, then finds all single-word anagrams of the entered word. Finally this function prints out the list of anagrams. If no anagrams are found, the program prints a message indicating that no anagrams were found.

- The <code>load_dictionary(file_name)</code> function loads the dictionary of English words from the <code>words_dictionary.json</code> file using the <code>load_dictionary()</code> function. The function takes a file name as an argument, opens the file using the <code>with open(file_name) as file:</code> statement, and loads the data using the <code>json.load(file)</code> method. The function then returns the loaded dictionary.

- The <code>get_anagrams()</code> function is called with the entered word and the loaded dictionary as parameters. This function finds all single-word anagrams of the entered word using the dictionary. The function first creates a dictionary called <code>word_dict</code> that contains the count of each letter in the entered word or name. Then goes through each word in the dictionary and creates a similar dictionary called <code>dict_word_dict</code> that contains the count of each letter in the dictionary word. If <code>dict_word_dict</code> is equal to <code>word_dict</code> and the dictionary word is not equal to the entered word, then the dictionary word is an anagram of the entered word, and is added to a list called <code>anagrams</code>. The program then prints out the list of anagrams.


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
