# LeetSpeak

## Description

This is a Python program that converts English text to Leetspeak. Leetspeak is a form of writing that replaces certain letters with numbers, symbols, or combinations of characters.

## How it Works

- To use the program, the user is prompted to enter an English message. The program then converts the message to Leetspeak based on the defined character mappings and displays the converted Leetspeak message.

- The program begins by importing the `random` module, which is used to randomly select leet replacements for certain characters.

- It defines a dictionary called `CHAR_MAPPING` that maps characters to their possible Leetspeak replacements. Each character is associated with a list of replacement options.

- The `main()` function is defined. It begins by printing a welcome message and prompting the user to enter their English message, and calls the `convert_to_leetspeak` function to convert the input into Leetspeak. The resulting Leetspeak message is then printed.

- The `get_user_input` function is defined to prompt the user for input and return the input string. It ensures that the input is not empty or consists only of whitespace.

- The `convert_to_leetspeak` function takes an English string as input and converts it to Leetspeak. It iterates over each character in the input string. If the lowercase version of the character exists in the `CHAR_MAPPING` dictionary and a random number is less than or equal to 0.70 (70% chance), it selects a random replacement from the list of possible Leetspeak replacements for that character. Otherwise, it keeps the original character. The converted Leetspeak string is built character by character and returned.


## Program Input & Output

When you run the program `leet_speak.py`, the output will look like this;

```


Welcome to Leetspeak.

Enter your message: The quick brown fox jumps over the lazy dog
Leetspeak: +he qu!<k |3|2[]wn ph[]x jum|*z 0\/e/2 7he |_@7_y d[]9
sh-5.1$ /usr/bin/python3 ".../leet-speak/leet_speak.py"

Welcome to Leetspeak.

Enter your message: Pack my box with five dozen liquor jugs
Leetspeak: Pa[|{ my |3()x wi~|~h f!\/e |>o7_en l!qu[]|2 jug5
sh-5.1$ /usr/bin/python3 ".../leet-speak/leet_speak.py"

Welcome to Leetspeak.

Enter your message: How vexingly quick daft zebras jump!
Leetspeak: H[]w \/exing|y quick |>@f7 7_e|3|?aZ _/um|*!
```
