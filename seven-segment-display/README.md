# The Seven-Segment Display

## Description

The seven segment displays are the output display device that provide a way to display information in the form of image or text or decimal numbers. It is widely used in digital clocks, basic calculators, electronic meters, and other electronic devices that display numerical information. It consists of seven segments of light emitting diodes (LEDs) which is assembled like numerical 8.

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

- The `main()` function of the program starts by prompting the user to enter a number to display. It checks whether the user input is a valid integer or not. If the input is not a valid integer, the program continues to prompt the user until a valid integer is entered. Once a valid integer is entered, the program calls the `generate_seven_segments()` function to generate the string representation of the seven-segment display for the entered integer.

- The `generate_seven_segments()` function first converts the input integer to a string and pads it with leading zeros to meet a minimum width. Then, it initializes a list of three empty strings to store the rows of the seven-segment display.

- The function iterates through each digit of the input integer and determines which segments to light up based on the value of the digit. For example, if the digit is '0', the function lights up the top, middle, and bottom segments of the first row, the left and right segments of the second row, and the top, middle, and bottom segments of the third row.

- The function appends the segments for each digit to the corresponding row in the list of rows. If the next digit is not a decimal point, the function adds a space to separate the digits.

- Finally, the function joins the rows with newline characters and returns the resulting string representation of the seven-segment display.

## Program Input & Output

When you run the program, `seven-segment-display.py`, the output will look like this;

```
Seven-Segment Number Display

Enter number to show:
> 123456789
      __   __        __   __   __   __   __ 
   |  __|  __| |__| |__  |__     | |__| |__|
   | |__   __|    |  __| |__|    | |__|  __|


Seven-Segment Number Display

Enter number to show:
> 42
      __ 
|__|  __|
   | |__ 


Seven-Segment Number Display

Enter number to show:
> 0
 __ 
|  |
|__|

```