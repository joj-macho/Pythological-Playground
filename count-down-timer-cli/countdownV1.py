import time
import sys


def main():
    print('\nCountdown Timer.\n')

    # Enter a valid number of seconds to countdown.
    while True:
        response = input('Enter seconds to start countdown:\n> ')
        if not response.isdecimal():
            continue
        else:
            start_time = int(response)
            break

    # Do the countdown
    count_down(start_time)


def count_down(start_time):
    '''This function returns a preceding countdown of input seconds'''
    try:
        while start_time:
            # Get minutes and seconds using divmod() function
            minutes, seconds = divmod(start_time, 60)

            timer = f'{minutes:02} : {seconds:02}'
            print(timer)

            time.sleep(1)

            start_time -= 1

        print('\nCOUNTDOWN COMPLETE')

    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()
