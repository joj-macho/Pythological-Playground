import random
import time

# Constants
BAR = chr(9608)  # Unicode character for a solid block
DOWNLOAD_SIZE = 4096*6  # Total size of the download in arbitrary units

def main():
    '''Simulate a progress bar for a download process.'''
    print('\nProgress Bar Simulation.')

    downloaded = 0
    total_size = DOWNLOAD_SIZE

    while downloaded < total_size:
        # Simulate downloading by adding a random amount to 'downloaded'
        downloaded += random.randint(10, 1000)

        bar_string = generate_progress_bar(downloaded, total_size)

        # Display the progress bar without a newline (so it overwrites)
        print(bar_string, end='', flush=True)
        time.sleep(0.2)
        # Use backspaces to clear the previous progress bar
        print('\b' * len(bar_string), end='', flush=True)

    print('\nDownload completed.')

def generate_progress_bar(progress, total, bar_width=40):
    '''Return a string representing a progress bar.'''
    progress_bar = '['

    # Ensure that progress and total are within valid bounds
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # Calculate the number of bars to represent the progress
    number_of_bars = int((progress / total) * bar_width)
    progress_bar += BAR * number_of_bars
    # Fill the rest with spaces
    progress_bar += ' ' * (bar_width - number_of_bars)
    # Close the progress bar
    progress_bar += ']'

    # Calculate and add the percentage and the current progress/total size
    completed = round(progress / total * 100, 1)
    progress_bar += f' {completed}%'
    progress_bar += f' {progress}/{total}'

    return progress_bar

if __name__ == '__main__':
    main()
