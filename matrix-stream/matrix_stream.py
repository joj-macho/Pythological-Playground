import random
import os
import time

# Matrix settings
MIN_STREAM = 6
MAX_STREAM = 15
STREAM_VAL = ('0', '1')
DENSITY = 0.05
WIDTH = os.get_terminal_size()[0] - 1

# ANSI color codes
GREEN = '\033[32m'
RESET = '\033[0m'


def main():
    '''Print the matrix stream animation.'''
    print('Matrix Stream Animation.\n')
    input('Press Enter to Start...')
    try:
        columns = [0 for _ in range(WIDTH)]
        while True:
            for i in range(WIDTH):
                if columns[i] == 0:
                    if random.random() <= DENSITY:
                        columns[i] = random.randint(MIN_STREAM, MAX_STREAM)
                if columns[i] > 0:
                    print(GREEN + random.choice(STREAM_VAL) + RESET, end='')
                    columns[i] -= 1
                else:
                    print(' ', end='')
            print()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('\nAnimation Interrupted! Exiting...')


if __name__ == '__main__':
    main()
