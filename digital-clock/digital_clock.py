import sys
import time
import seven_segment

def main():
    '''Main function to display current time using the seven-segments display.'''
    print('\nDigital Timer.\n')

    try:
        while True:
            # Get time from computer
            current_time = time.localtime()
            hours = str(current_time.tm_hour % 24)
            minutes = str(current_time.tm_min)
            seconds = str(current_time.tm_sec)

            # Get digit strings from seven_segments
            hour_digit = seven_segment.display_seven_segments(hours, 2)
            hour_top_row, hour_middle_row, hour_bottom_row = hour_digit.splitlines()

            minute_digit = seven_segment.display_seven_segments(minutes, 2)
            minute_top_row, minute_middle_row, minute_bottom_row = minute_digit.splitlines()

            sec_digit = seven_segment.display_seven_segments(seconds, 2)
            sec_top_row, sec_middle_row, sec_bottom_row = sec_digit.splitlines()

            # Display the digits:
            print(hour_top_row + '     ' + minute_top_row + '     ' + sec_top_row)
            print(hour_middle_row + '  *  ' +
                  minute_middle_row + '  *  ' + sec_middle_row)
            print(hour_bottom_row + '  *  ' +
                  minute_bottom_row + '  *  ' + sec_bottom_row)

            print()
            print('Press Ctrl-C to quit.')

            # Loop through seconds
            while True:
                time.sleep(0.01)
                if time.localtime().tm_sec != current_time.tm_sec:
                    break

    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
