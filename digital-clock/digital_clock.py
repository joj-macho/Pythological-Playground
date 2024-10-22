import time
import os
from seven_segment import seven_segment_display


def main():
    '''Run the digital clock with a seven-segment display.'''
    print('Digital Clock using Seven-Segment Display!\n')
    try:
        while True:
            os.system('clear')  # (Un)comment to clear screen
            display_time(format_time(time.localtime()))
            time.sleep(1)
    except KeyboardInterrupt:
        print('\nClock interrupted... Bye!')


def format_time(current_time):
    '''Converts the current time to HH:MM:SS format.'''
    # Extract the hour, minute, and second from the current time structure
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    return f'{hours:02}:{minutes:02}:{seconds:02}'


def display_time(time_str):
    '''Displays the given time string in seven-segment format.'''
    rows = ['', '', '']
    for char in time_str:
        segment = seven_segment_display(char).split('\n')
        for i in range(3):
            rows[i] += segment[i]

    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
