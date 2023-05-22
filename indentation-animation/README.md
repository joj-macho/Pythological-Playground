# Indentation Animation

## Description

This program, Indentation Animation, creates a visually appealing effect by displaying an animation of indentation using asterisks. It utilizes a loop to dynamically adjust the number of spaces preceding a line of asterisks, creating the illusion of indentation. The animation smoothly transitions between increasing and decreasing indentation, giving a visually pleasing and engaging output. The speed of the animation can be adjusted by modifying the sleep duration. The program runs indefinitely until interrupted by the user.

## How it Works

- The program starts by importing the `time` and `sys` modules.

- The `main()` function is defined. It contains the main logic for the animation. The program starts by printing a header indicating the name of the animation and initializes three variables:
    - The `indent` variable keeps track of the number of spaces to indent.
    - The `is_indent_increasing` variable is a boolean flag indicating whether the indentation is currently increasing or not.
    - The `sleep_duration` variable specifies the duration in seconds for the pause between each frame of the animation.

- The program enters a `try-except` block to catch a `KeyboardInterrupt` exception (Ctrl+C) and exit gracefully. Within the `try` block. The program enters a loop (`while True`) that runs indefinitely until a keyboard interrupt is encountered.

- In each iteration of the loop, the program prints a line with the number of spaces determined by the current value of indent, followed by a line of asterisks (`********`).

- After printing the line, the program pauses for `sleep_duration` seconds using `time.sleep(0.1)` to create a smooth animation effect.

- The program checks the value of `is_indent_increasing` to determine whether to increase or decrease the indentation:
    - If `is_indent_increasing` is `True`, the program increments the value of `indent` by 1. When `indent` reaches 20, it sets `is_indent_increasing` to `False`, indicating that the next step is to decrease the indentation.
    - If `is_indent_increasing` is `False`, the program decrements the value of `indent` by 1. When `indent` reaches 0, it sets `is_indent_increasing` back to True, indicating that the next step is to increase the indentation again.

- The loop continues indefinitely, creating a back-and-forth motion of the asterisks with changing indentation.

- If the user interrupts the program by pressing Ctrl+C (`KeyboardInterrupt`), the program catches the exception and calls `sys.exit()` to terminate the program cleanly.

## Program Input & Output

When you run the program `indentation_animation.py`, the output will look like a visually appealing animation of a moving pattern that continuously oscillates between increasing and decreasing indentation;

![Indentation Animation Results](output/indent-result.gif)
