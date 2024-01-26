# Magic Fortune Teller

## Description

The Magic Fortune Teller program is an interactive command-line application that simulates the experience of consulting a mystical fortune-telling oracle for yes or no questions. It combines elements of humor and mysticism to provide responses to user queries.

## How it Works

- The program uses the `random` and `time` modules, for mysticism...

- The `main()` function prints the ASCII art representing the "Magic Fortune Ball". The `slow_print()` function is called to display the title in a slow printing manner.
    - The `slow_print()` function takes a string and an optional interval parameter. The function iterates over each character in the string and prints it with a space after it, except for the letter 'I', which is printed without a space. The function introduces a delay between characters using the `time.sleep()` function. After each character is printed, a newline character is printed to move to the next line.

- After a short delay, the program prompts the user to ask a Yes or No question. The user's input is read but not processed further.

- Next, a list of possible replies is defined. These are brief statements that the Magic Fortune Ball might respond with before revealing the answer.

- The `random.choice()` function is used to select a random reply from the list. The selected reply is displayed using the `slow_print()` function. A random number of dots between 3 and 10 is printed using the `slow_print()` function to create a suspenseful effect.

- The Magic Fortune Ball pretends to think for a moment before revealing the answer. The `slow_print()` function is used to display "I have an answer..." with a slower interval between characters. A list of possible answers is defined. The `random.choice()` function is used to select a random answer from the list. The chosen answer is displayed using the `slow_print()` function with a faster interval, creating a scrolling effect.

- The user is prompted whether they want to ask another question. If they enter 'y' (yes), the `main()` function is called again, allowing them to play again. Otherwise, the program terminates.

## Program Input & Output

When you run the program `magic_ball.py`, the output will look like this

![Magic Ball Results](output/magic-ball-result.gif)
