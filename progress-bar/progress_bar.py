import sys
import time

# Animation constants
PROGRESS_BAR_LENGTH = 50
BAR = '\u2588'  # Block █ charcter
EMPTY_BAR = ' '
TOTAL_SIZE = 4096 * 8  # Total size of the download

# Colors
COLOR_GREEN = '\033[92m'
COLOR_RESET = '\033[0m'


def main():
    '''Simulates a download with a progress bar.'''
    print('Progress Bar Animation.\n')
    start_time = time.time()
    try:
        # Simulate a donwload
        for current_size in range(
                0, TOTAL_SIZE + 1, max(512, TOTAL_SIZE // 50)):
            display_progress_bar(current_size)
            time.sleep(0.1)  # download delay

        # Ensure the final display shows 100% completion
        display_progress_bar(TOTAL_SIZE)
        elapsed_time = time.time() - start_time
        print(f'\nDownload completed in {elapsed_time:.2f} seconds.')
    except KeyboardInterrupt:
        elapsed_time = time.time() - start_time
        print(f'\nDownload interrupted after {elapsed_time:.2f} seconds.')
        sys.exit(1)


def display_progress_bar(current_size, total_size=TOTAL_SIZE):
    '''Displays a progress bar with the current progress and percentage.'''
    progress_ratio = current_size / total_size
    progress_percentage = progress_ratio * 100
    filled_length = int(PROGRESS_BAR_LENGTH * progress_ratio)

    progress_bar = (COLOR_GREEN + BAR * filled_length + COLOR_RESET +
                    EMPTY_BAR * (PROGRESS_BAR_LENGTH - filled_length))

    # Display the progress bar with percentage and sizes
    sys.stdout.write(f'\r[{progress_bar}] {progress_percentage:5.1f}% '
                     f'{current_size}/{total_size}')
    sys.stdout.flush()


if __name__ == '__main__':
    main()
