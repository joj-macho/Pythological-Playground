import time
import sys

def main():
    '''Main function to run the countdown timer.'''
    print('\nCountdown Timer.\n')

    while True:
        response = input('Enter number of seconds to start countdown:\n> ')
        if not response.isdecimal():
            continue
        else:
            start_time = int(response)
            break

    # Do the countdown
    count_down(start_time)

def count_down(start_time):
    '''Perform the countdown and displays the time.'''
    try:
        while start_time:
            # Get minutes and seconds using divmod() function
            minutes, seconds = divmod(start_time, 60)

            timer = f'{minutes:02} : {seconds:02}'
            print(timer, end='\r')

            time.sleep(1)  # one-second pause.

            start_time -= 1

        print('\nCOUNTDOWN COMPLETE')

    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
