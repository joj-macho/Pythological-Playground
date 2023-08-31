import sys
import time
import seven_segment


def main():
    '''Main function for the countdown timer with seven-segment display.'''

    print('\nCountDown Timer.\n')

    # Enter a valid number of seconds to countdown.
    while True:
        response = input(
            'Enter seconds to start countdown. Press Ctrl-C to quit:\n> ')
        if not response.isdecimal():
            continue
        else:
            start_time = int(response)
            break

    # Do the Countdown
    count_down(start_time)


def count_down(start_time):
    '''This function performs the countdown using the seven segment display.'''

    try:
        while True:
            # Get time components: hours, minutes, seconds
            hours = str(start_time // 3600)
            minutes, seconds = divmod(start_time, 60)

            # Generate seven-segment digit strings
            hour_digit = seven_segment.generate_seven_segments(hours, 2)
            hour_top_row, hour_middle_row, hour_bottom_row = hour_digit.splitlines()

            minute_digit = seven_segment.generate_seven_segments(minutes, 2)
            minute_top_row, minute_middle_row, minute_bottom_row = minute_digit.splitlines()

            sec_digit = seven_segment.generate_seven_segments(seconds, 2)
            sec_top_row, sec_middle_row, sec_bottom_row = sec_digit.splitlines()

            # Display the digits:
            print(hour_top_row + '     ' + minute_top_row + '     ' + sec_top_row)
            print(hour_middle_row + '  *  ' +
                  minute_middle_row + '  *  ' + sec_middle_row)
            print(hour_bottom_row + '  *  ' +
                  minute_bottom_row + '  *  ' + sec_bottom_row)

            if start_time == 0:
                print()

                print('\nCOUNTDOWN COMPLETE')

                break

            time.sleep(1)  # one-second pause.
            start_time -= 1

    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()
