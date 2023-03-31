# Finding Palindromes

## Description

Palindromes are words, phrases, or sentences that read the same backward as forward.

This program is a simple Python script that works with a dictionary of words, in JSON format to find and display palindromes.

You can download the dictionary file [here]('https://github.com/dwyl/english-words/blob/master/words_dictionary.json') 

## How it Works

- The program begins by importing neccessary modules, including <code>os</code>, <code>sys</code>, <code>json</code>, and <code>random</code>. The <code>os</code> and <code>sys</code> mdoules are used to set the working directory to the directory where the script is located, and <code>json</code> is used to load the dictionary of words from the JSON file. The <code>random</code> module is used to select a random palindrome from the dictionary.

- The <code>main()</code> function begins by printing the welcome message. The function loads the dictionary, prompts the user to enter a word, checks if the word is a palindrome using the <code>is_palindrome()</code> function and displays a random palindrome from the dictionary using the <code>get_random_palindrome()</code> function.

- The <code>load_dictionary(file_name)</code> function loads the dictionary from the specified JSON file. The function takes a file name as an argument, opens the file using the <code>with open(file_name) as file:</code> statement, and loads the data using the <code>json.load(file)</code> method. The function then returns the loaded dictionary.

- The <code>is_palindrome(word)</code> function checks if a given word is a palindrome. The function takes a string <code>word</code> as an argument and checks if the length of the word is greater than 1 and if the word is equal to its reverse, which is obtained using the slice notation <code>[::-1]</code>. If the word is a palindrome, the function returns <code>True</code>, otherwise, it returns <code>False</code>.

- The <code>get_random_palindrome(words_dict)</code> function selects a random palindrome from the dictionary. The function takes a dictionary <code>words_dict</code> as an argument and uses a list comprehension to create a list of palindromes from the dictionary using the <code>is_palindrome()</code> function. If the list of palindromes is not empty, the function selects a random palindrome from the list using the <code>random.choice()</code> method and returns it. Otherwise, it returns <code>None</code>.

- To use the program, run the script and follow the prompts. The program will load the <code>words_dictionary.json</code> file and allow you to enter a word to check if it's a palindrome. It will then display a random palindrome from the dictionary.



## Program Input & Output

When you run the program `find_palindromes.py`, the output will look like this;

```

Welcome To Palindrome Checker.

Enter a word to check if it is a palindrome:
> rotator
rotator is a palindrome!

Here is a random palindrome from the dictionary: sus

...

Welcome To Palindrome Checker.

Enter a word to check if it is a palindrome:
> dog
dog is not a palindrome.

Here is a random palindrome from the dictionary: abba
```






