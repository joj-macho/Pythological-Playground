# The Seven-Segment Display

## Description

The "Seven-Segment Display" program is designed to visually represent numbers and some letters (0-9, A-F) using a text-based format that mimics a real seven-segment display.

The seven-segment displays are the output display device that provide a way to display information in the form of image or text or decimal numbers. It is widely used in digital clocks, basic calculators, electronic meters, and other electronic devices that display numerical information. Each segment of the display is made up of an LED, LCD, or other display technologies, which can be turned on or off to form numbers and letters.

See the [Countdown Timer](https://github.com/joj-macho/Pythological-Playground/tree/main/count-down-timer) program and the [Digital Clock](https://github.com/joj-macho/Pythological-Playground/tree/main/digital-clock), both of which use the seven-segment display to format and display time.

## How it Works

- A seven-segment display consists of seven individual segments arranged in a rectangular fashion, as follows:

```
 __1__
|     |    Each digit in a seven-segment display:
2     4     __       __   __        __   __  __   __   __
|__3__|    |  |   |  __|  __| |__| |__  |__    | |__| |__|
|     |    |__|   | |__   __|    |  __| |__|   | |__|  __|
5     7
|__6__|
```

- Use a dictionary, `segment_map`, to map each string representation of a digit (0-9) to its corresponding seven-sgement display representation.

## Running the Program

```bash
# Navigate to the project directory
cd seven-segment-display/

# Run the main script
python3 seven_segment_display.py
```

## Program Input & Output

When you run the program, `seven_segment_display.py`, the output will look like this;

```
The Seven-Segment Display Simulator!

Enter digit(s) (0-9) to display, or (q)uit to exit.
> 4
    
|_| 
  | 

> 2
 _  
 _| 
|_  

> 42
     _  
|_|  _| 
  | |_  

> 0123456789
 _       _   _       _   _   _   _   _  
| |   |  _|  _| |_| |_  |_    | |_| |_| 
|_|   | |_   _|   |  _| |_|   | |_|  _| 

> 42!
Enter a valid positive integer (0-9)!

> 3.14
Enter a valid positive integer (0-9)!

> q
Bye!
```