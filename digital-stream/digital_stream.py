import random
import sys
import time
import shutil

# Constants
MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAM_VAL = ['0', '1']
DENSITY = 0.02
# Terminal size: Print to last column(-1)
WIDTH = shutil.get_terminal_size()[0] - 1


def main():
    print('\nDigital Stream.\n')
    input('Press Enter to Continue...')

    try:
        columns = [0]*WIDTH
        # print('Columns:', columns)
        while True:
            for i in range(WIDTH):
                # print(f'1st columns[i] : {columns[i]}')
                if columns[i] == 0:
                    if random.random() <= DENSITY:
                        columns[i] = random.randint(
                            MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
                        # print(f'2nd columns[i] : {columns[i]}')
                if columns[i] > 0:
                    print(random.choice(STREAM_VAL), end='')
                    columns[i] -= 1
                else:
                    print(' ', end='')
            print()
            sys.stdout.flush()
            time.sleep(PAUSE)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()