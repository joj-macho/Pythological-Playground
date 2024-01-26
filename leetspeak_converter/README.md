# Leetspeak Converter

## Description

The Leetspeak Converter is a Python program that allows users to convert English text into Leetspeak. Leetspeak, also known as "leet" or "1337," is an alternative alphabet used primarily on the internet. It replaces certain letters with numbers or special characters that resemble the letters they replace. 

## How it Works

- The program uses the `random` module to randomly select leet replacements for replacebale characters.

- The `CHAR_MAPPING` constant maps characters to their possible Leetspeak replacements. Each character is associated with a list of replacement options.

- The `main()` function allows the user to enter their message, and calls the `convert_to_leetspeak` function to convert the input into Leetspeak.

- The `convert_to_leetspeak` function iterates over each character in the input string. If the lowercase version of the character exists in the `CHAR_MAPPING` dictionary and a random number is less than or equal to 0.60 (60% chance), it selects a random replacement from the list of possible Leetspeak replacements for that character. Otherwise, it keeps the original character.

## Program Input & Output

When you run the program `leetspeak.py`, the output will look like this;

```

Welcome to Leetspeak.

Enter your message: The quick brown fox jumps over the lazy dog
Leetspeak: 7he quick br0wn f0x _|um|D5 o\/er +he |@zy |)o9

.
.
.

Enter your message: Pack my box with five dozen liquor jugs
Leetspeak: |oa[k my 8ox w1th f!ve d()zen |1qu()r jug$

.
.
.

Enter your message: How vexingly quick daft zebras jump!
Leetspeak: How vex!n9|y qu!ck d@f7 2ebras jum|*!
```
