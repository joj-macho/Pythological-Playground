# Digital Stream

## Description

Digital stream is a simulation of number flowing on the screen, concept from the Matrix Movies. This program simulates a digital stream that consists of randomly generated 0s and 1s. The stream is displayed in the terminal window and is constantly updated.

## How it Works

- The program uses the `random` module for generating random numbers, `sys` for handling system-related functionality, `time` for introducing pauses, and `shutil` to determine the width of the terminal.

- The program uses various constants, including `MIN_STREAM_LENGTH`, `MAX_STREAM_LENGTH`, `PAUSE`, `STREAM_VAL`, `DENSITY`, `WIDTH`. These constants control various aspects of the digital stream, such as the minimum and maximum length of each stream, the pause duration between updates for controlling the speed, the possible values in the stream (binary digits), the probability density for starting a new stream in a column, and the width of the terminal display.

- The `main` function enters a loop where at each iteration of the loop, the program checks each column and determines whether a new stream should be generated. If the column has a value of 0, there is no active stream in that column, and the program generates a new stream with a random length, based on the `MIN_STREAM_LENGTH` and `MAX_STREAM_LENGTH`.

- If a stream is active, the program prints a random 0 or 1 for each position in the column until the stream ends, at which point spaces are printed to maintain the width of the terminal window. The `DENSITY` constant determines the probability that a new stream will be generated in any given column at each iteration. 

- The program is executed in an infinite loop until the user interrupts it with a `KeyboardInterrupt` exception, by pressing Ctrl-C.

## Program Output

When you run `digital_stream.py`, the output will look like this;

![Digital Timer Results](output/stream-results.gif)