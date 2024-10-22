import time
import os
from seven_segment import seven_segment_display


def main():
    '''Start the countdown timer.'''
    print('Countdown Timer using Seven-Segment Display!\n')
    while True:
        print('Enter the numbr of seconds for the countdown. '
              'Enter (q)uit to exit:')
        response = input('> ').lower()

        if response.startswith('q'):
            print('Bye!')
            break

        try:
            seconds = int(response)
            if seconds <= 0:
                raise ValueError('Enter a positive integer.')
            else:
                countdown(seconds)  # Start the countdown
        except ValueError as e:
            print(f'Invalid Input: {e}\n')
        except KeyboardInterrupt:
            print('\nCountdown interrupted... Bye!\n')


def countdown(seconds):
    '''Performs a countdown from a given number of seconds.'''
    while seconds > 0:
        os.system('clear' if os.name == 'posix' else 'cls')
        time_formatted_str = format_time(seconds)
        display_time(time_formatted_str)
        time.sleep(1)
        seconds -= 1

    # os.system('clear')  # (Un)comment to clear screen
    display_time('00:00:00')  # Final time
    print('\nCountdown Finished!\n')


def format_time(seconds):
    '''Converts seconds to string representating hours, minutes, and
    seconds.'''
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    # Format time to HH:MM:SS
    return f'{hours:02}:{minutes:02}:{seconds:02}'


def display_time(time_str):
    '''Displays the given time string in seven-segment format.'''
    rows = ['', '', '']
    for char in time_str:
        # Get seven-segment repr of each char split to lines
        segment = seven_segment_display(char).split('\n')
        for i in range(3):
            rows[i] += segment[i]

    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
