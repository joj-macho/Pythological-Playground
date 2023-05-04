# Countdown Timer

## Description

This program is a simple countdown timer that accepts user input in the form of a number of seconds to count down from.

The second version of the countdown timer uses the Seven Segment Display. The seven segment displays are the output display device that provide a way to display information in the form of image or text or decimal numbers. It is widely used in digital clocks, basic calculators, electronic meters, and other electronic devices that display numerical information. It consists of seven segments of light emitting diodes (LEDs) which is assembled like numerical 8.

A labeled seven-segment display, with each segment labeled A to G:
```
 __A__
|     |    Each digit in a seven-segment display:
F     B     __       __   __        __   __  __   __   __
|__G__|    |  |   |  __|  __| |__| |__  |__    | |__| |__|
|     |    |__|   | |__   __|    |  __| |__|   | |__|  __|
E     C
|__D__|
```

## How it Works

### countdownV1.py

- The program begins by importing the `time` module.

- The `main()` program first displays a welcome message. Then, it uses a while loop to continuously prompt the user to enter a valid number of seconds to count down from. The program ensures that the user input is a decimal number using the `isdecimal()` method.

- The program then calls the `count_down()` function and passes the user input as an argument to it. The `count_down()` function then takes the start time as an argument and enters a loop that subtracts one second from the start time variable in each iteration. The `divmod()` function is used to calculate the minutes and seconds left in the countdown. These values are then formatted into a string using the f-string syntax and displayed to the user.

- The loop continues until the start time variable becomes zero. Finally, the program prints a message to indicate that the countdown is complete.

### countdownV2.py

- The program `countdownV2.py` is a countdown timer that displays the remaining time using a seven-segment display.

- The program first imports the `sys` and `time` modules, as well as the `seven_segments` module, which contains a function to generate seven-segment display strings for numbers.

- The `main()` function begins by displaying a welcome message. Then prompts the user to enter a valid number of seconds to countdown, using a while loop that continues to ask for input until a valid integer is entered. Once a valid integer is entered, the `count_down` function is called with the entered integer as an argument.

- The `count_down` function takes the starting time as an argument and performs the countdown using a while loop. Within each iteration of the loop, the number of hours, minutes, and seconds remaining are calculated and passed to the `generate_seven_segment` function from the `seven_segments` module, which returns seven-segment display strings for each digit. These strings are then split into three lines each. The resulting strings are printed to the console, separated by spaces and asterisks, to create a visually appealing display of the remaining time in the countdown. The loop also includes a one-second pause using the `time.sleep` function and decrements the `start_time` variable by one each iteration.

- If the countdown reaches zero, the program prints "COUNTDOWN COMPLETE" to the console and exits the loop.


## Program Input & Output

When you run `countdownV1.py`, the output will look like this;

```
Countdown Timer.

Enter seconds to start countdown:
> 6
00 : 06
00 : 05
00 : 04
00 : 03
00 : 02
00 : 01

COUNTDOWN COMPLETE
```

When you run `countdownV2.py`, the output will look like this;

```
CountDown Timer.

Enter seconds to start countdown. Press Ctrl-C to quit:
> 5
 __   __       __   __       __   __ 
|  | |  |  *  |  | |  |  *  |  | |__ 
|__| |__|  *  |__| |__|  *  |__|  __|
 __   __       __   __       __      
|  | |  |  *  |  | |  |  *  |  | |__|
|__| |__|  *  |__| |__|  *  |__|    |
 __   __       __   __       __   __ 
|  | |  |  *  |  | |  |  *  |  |  __|
|__| |__|  *  |__| |__|  *  |__|  __|
 __   __       __   __       __   __ 
|  | |  |  *  |  | |  |  *  |  |  __|
|__| |__|  *  |__| |__|  *  |__| |__ 
 __   __       __   __       __      
|  | |  |  *  |  | |  |  *  |  |    |
|__| |__|  *  |__| |__|  *  |__|    |
 __   __       __   __       __   __ 
|  | |  |  *  |  | |  |  *  |  | |  |
|__| |__|  *  |__| |__|  *  |__| |__|


COUNTDOWN COMPLETE
```