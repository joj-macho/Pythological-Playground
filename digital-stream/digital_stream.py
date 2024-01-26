import random
import sys
import time
import shutil

# Constants
MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAM_VAL = ['0', '1']
DENSITY = 0.02   # Probability density for starting a new stream in a column
WIDTH = shutil.get_terminal_size()[0] - 1  # Width of the terminal display, subtracting 1 for the last column

def main():
    '''Main function to create the stream of numbers.'''
    print('\nDigital Stream.\n')
    input('Press Enter to Continue...')

    try:
        columns = [0]*WIDTH  # State of each column in the display
        while True:
            for i in range(WIDTH):
                if columns[i] == 0:
                    # Randomly decide if a new stream should start in this column
                    if random.random() <= DENSITY:
                        columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
                if columns[i] > 0:
                    # Print a random binary digit for an active stream
                    print(random.choice(STREAM_VAL), end='')
                    columns[i] -= 1
                else:
                    # Print a space for an inactive column
                    print(' ', end='')
            print()
            sys.stdout.flush()
            time.sleep(PAUSE)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()