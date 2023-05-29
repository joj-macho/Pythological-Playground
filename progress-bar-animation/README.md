# Progress Bar Animation

## Description

This program simulates a progress bar for a download process using random values to simulate the download speed. The progress bar shows the percentage completed, the amount of downloaded data, and the total amount of data to be downloaded.

## How it Works

- The program imports the `random` and `time` modules which are used to generate random numbers and control the timing of the progress bar simulation, respectively.

- The program defines a constant `BAR` which is set to the Unicode character for a filled block (▇) and `DOWNLOAD_SIZE` which represents the total size of the download.

- The `main()` function is responsible for running the progress bar simulation. It initializes the `downloaded` variable to 0 and sets the `total_size` to the predefined `DOWNLOAD_SIZE`. It then enters a loop that continues until the amount of downloaded data is equal to or greater than the total download size.

- Inside the main loop, the `downloaded` variable is updated by generating a random number between 10 and 1000, simulating the download speed. The `generate_progress_bar()` function is then called to generate the progress bar string based on the current progress and the total size. The progress bar is printed to the console using `print()` with the `end=''` argument to avoid printing a newline character. The `flush=True` argument ensures that the output is immediately displayed.

- After printing the progress bar, a small delay of 0.2 seconds is added using `time.sleep()` to simulate the passage of time. The number of backspaces (`\b`) equivalent to the length of the progress bar string is printed to move the cursor back to the start of the progress bar line.

- This process continues until the `downloaded` variable reaches or exceeds the `total_size`. Once the download is completed, the program prints a message indicating that the download is finished.

- The `generate_progress_bar()` function takes the `progress`, `total`, and `bar_width` as inputs and returns a string representing the progress bar. It calculates the number of filled bars based on the ratio of the `progress` to the `total` using integer division. The remaining empty spaces are filled with spaces. The percentage of completion and the current progress and total size are appended to the progress bar string.


## Program Input & Output

When you run the program `progress_bar.py`, the output will look like this;

![Progress Bar Results](output/progress-bar-results.gif)
