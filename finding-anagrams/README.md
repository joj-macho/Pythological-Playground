# Finding Anagrams

## Description

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, the word "listen" is an anagram of the word "silent".

This Python program reads words from a dictionary file (`words_dictionary.json`) and generates a list of anagrams for a given input word. You can download the dictionary file [here]('https://github.com/dwyl/english-words/blob/master/words_dictionary.json')

## How it Works

- Enter text and get anagrams

## Running the Program

```bash
# Navigate to the project directory
cd finding-anagrams/

# Run the main script
python3 finding_anagrams.py
```

## Program Input & Output

When you run the program `finding_anagrams.py`, the output will look like this;

```
Anagram Finder

Enter a word to find its anagrams (or (q)uit to exit):
> silent
The anagrams for the word "silent" are:
- enlist
- inlets
- listen
- slinte
- tinsel

Enter a word to find its anagrams (or (q)uit to exit):
> power
No anagrams found for the word "power".

Enter a word to find its anagrams (or (q)uit to exit):
> yes
The anagrams for the word "yes" are:
- sey
- sye

Enter a word to find its anagrams (or (q)uit to exit):
> q
Bye!
```
