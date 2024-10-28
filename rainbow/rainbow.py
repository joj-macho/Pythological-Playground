import time
import os


WIDTH = os.get_terminal_size().columns
BASE_TEXT = 'RAINBOW'
AMPLITUDE = 10  # Height of the wave

# ANSI eRainbow colors
RAINBOW_COLORS = [
    '\033[91m',  # Red
    '\033[93m',  # Orange
    '\033[92m',  # Yellow
    '\033[96m',  # Green
    '\033[94m',  # Blue
    '\033[95m',  # Indigo
    '\033[35m'   # Violet
]
RESET_COLOR = '\033[0m'


def main():
    '''Animate rainbow text.'''
    try:
        while True:
            for i in range(len(RAINBOW_COLORS)):
                os.system('clear' if os.name == 'posix' else 'cls')
                print('Rainbow Text Animation.\n')
                for j in range(len(RAINBOW_COLORS)):
                    # Create a wavy thingy by adjusting the number of spaces
                    wave_offset = AMPLITUDE * j
                    spaces_before = ' ' * (wave_offset % WIDTH)
                    spaces_after = ' ' * \
                        ((WIDTH - len(BASE_TEXT) - wave_offset) % WIDTH)
                    rainbow_pattern = spaces_before + BASE_TEXT + spaces_after
                    print(RAINBOW_COLORS[(i + j) % len(RAINBOW_COLORS)] +
                          rainbow_pattern +
                          RESET_COLOR)
                time.sleep(0.2)
    except KeyboardInterrupt:
        print('\nAnimation interrupted! Exiting...')


if __name__ == '__main__':
    main()
