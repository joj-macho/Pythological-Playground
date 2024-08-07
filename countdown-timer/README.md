# Countdown Timer

## Description

The "Count Down Timer" is a basic countdown timer that counts down from a specified number of seconds to 0, using the seven-segment display format.

Refer to the [Seven-Segment Display](https://github.com/joj-macho/Pythological-Playground/tree/main/seven-segment-display) program. Also, the [Digital Clock](https://github.com/joj-macho/Pythological-Playground/tree/main/digitial-clock), similar to the countdown timer, uses the seven-sgements display to format current time.

## How it Works

- Enter the number of seconds to start program.
- The program converts and formats the number of seconds into a time string (`HH:MM:SS`).
- The time string (`HH:MM:SS`) is converted into a seven-segment display format.
- Countdown starts and ends at `00:00:00` (in seven-segment format).

## Running the Program

```bash
# Navigate to the project directory
cd count-down-timer

# Run the main script
python3 countdown.py
```

## Program Input & Output

When you run `countdown.py`, the output will look like this;

```
Countdown Timer using Seven-Segment Display!

Enter the numbr of seconds for the countdown. Enter (q)uit to exit:
> 5
 _   _       _   _       _   _  
| | | |  *  | | | |  *  | | |_  
|_| |_|  *  |_| |_|  *  |_|  _| 
 _   _       _   _       _      
| | | |  *  | | | |  *  | | |_| 
|_| |_|  *  |_| |_|  *  |_|   | 
 _   _       _   _       _   _  
| | | |  *  | | | |  *  | |  _| 
|_| |_|  *  |_| |_|  *  |_|  _| 
 _   _       _   _       _   _  
| | | |  *  | | | |  *  | |  _| 
|_| |_|  *  |_| |_|  *  |_| |_  
 _   _       _   _       _      
| | | |  *  | | | |  *  | |   | 
|_| |_|  *  |_| |_|  *  |_|   | 
 _   _       _   _       _   _  
| | | |  *  | | | |  *  | | | | 
|_| |_|  *  |_| |_|  *  |_| |_| 

Countdown Finished!

Enter the numbr of seconds for the countdown. Enter (q)uit to exit:
> 0
Invalid Input: Enter a positive integer.
Please try again.

Enter the numbr of seconds for the countdown. Enter (q)uit to exit:
> 2.5
Invalid Input: invalid literal for int() with base 10: '2.5'
Please try again.

Enter the numbr of seconds for the countdown. Enter (q)uit to exit:
> 25200
 _   _       _   _       _   _  
| |   |  *  | | | |  *  | | | | 
|_|   |  *  |_| |_|  *  |_| |_| 
 _   _       _   _       _   _  
| | |_   *  |_  |_|  *  |_  |_| 
|_| |_|  *   _|  _|  *   _|  _| 
 _   _       _   _       _   _  
| | |_   *  |_  |_|  *  |_  |_| 
|_| |_|  *   _|  _|  *   _| |_| 
 _   _       _   _       _   _  
| | |_   *  |_  |_|  *  |_    | 
|_| |_|  *   _|  _|  *   _|   | 
^CCountdown Terminated!
```