# Leetspeak Converter

## Description

The Leetspeak Converter is a Python program that allows users to convert English text into Leetspeak. Leetspeak, also known as "leet" or "1337," is an alternative alphabet used primarily on the internet. It replaces certain letters with numbers or special characters that resemble the letters they replace. 

## How it Works

- The program begins by importing the `random` module, which is used to randomly select leet replacements for certain characters.

- It defines a dictionary called `CHAR_MAPPING` that maps characters to their possible Leetspeak replacements. Each character is associated with a list of replacement options.

- The `main()` function begins by printing a welcome message and prompting the user to enter their English message, and calls the `convert_to_leetspeak` function to convert the input into Leetspeak. The resulting Leetspeak message is then printed.

- The `convert_to_leetspeak` function takes an English string as input and converts it to Leetspeak. It iterates over each character in the input string. If the lowercase version of the character exists in the `CHAR_MAPPING` dictionary and a random number is less than or equal to 0.70 (70% chance), it selects a random replacement from the list of possible Leetspeak replacements for that character. Otherwise, it keeps the original character. The converted Leetspeak string is built character by character and returned.


## Program Input & Output

When you run the program `leetspeak.py`, the output will look like this;

```

Welcome to Leetspeak.

Enter your message: The quick brown fox jumps over the lazy dog
Leetspeak: The qu1<|{ |3r0wn f()x _|umps over the la7_y |)og

.
.
.

Enter your message: Pack my box with five dozen liquor jugs
Leetspeak: |o@<|{ my box w1th fi\/e |)ozen |_1qu()r _|ug5

.
.
.

Enter your message: How vexingly quick daft zebras jump!
Leetspeak: H()w \/ex!ngly qu1<|{ |)@f7 2e|3r@§ _|um|*!

```
