# Digital Clock

## Description

This program is a digital timer that uses the `time` module to get the current time from the computer, and the `seven_segment` module to generate the seven-segment displays for the hours, minutes, and seconds of the timer.

## How it Works

- The program uses the `sys`, `time`, and `seven_segment` modules.

- The `main()` function enters an infinite loop that continuously displays the current time on a seven-segment display. 

- The loop first gets the current time using the `time.localtime()` function, which returns a `time.struct_time` object representing the current time. It then extracts the hour, minute, and second from this object and generates the corresponding seven-segment representations using the `seven_segments.generate_seven_segments()` function. The digit strings are then split into three rows, which are printed to the console along with some whitespace to create a visual separation between the different digits.

- The loop waits for one hundredth of a second using the `time.sleep()` function, and checks if the current second has changed, which signals that it's time to update the display. If a `KeyboardInterrupt` exception is raised (i.e. the user presses Ctrl-C), the program exits using the `sys.exit()` function.

## Program Input & Output

When you run the program `digital_clock.py`, the output will look like this;

![Digital Timer Results](output/timer-results.gif)