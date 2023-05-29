import random
import time

BAR = chr(9608)
DOWNLOAD_SIZE = 4096*6


def main():
    '''Simulate a progress bar for a download process.'''

    print('\nProgress Bar Simulation.')

    downloaded = 0
    total_size = DOWNLOAD_SIZE

    while downloaded < total_size:
        # Download speed
        downloaded += random.randint(10, 1000)
        # Progress bar
        bar_string = generate_progress_bar(downloaded, total_size)

        print(bar_string, end='', flush=True)
        time.sleep(0.2)
        # Backspaces
        print('\b' * len(bar_string), end='', flush=True)

    print('\nDownload completed.')


def generate_progress_bar(progress, total, bar_width=40):
    '''Return a string representing a progress bar.'''

    progress_bar = '['

    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    number_of_bars = int((progress / total) * bar_width)
    progress_bar += BAR * number_of_bars
    progress_bar += ' ' * (bar_width - number_of_bars)
    progress_bar += ']'

    completed = round(progress / total * 100, 1)
    progress_bar += f' {completed}%'
    progress_bar += f' {progress}/{total}'

    return progress_bar


if __name__ == '__main__':
    main()
