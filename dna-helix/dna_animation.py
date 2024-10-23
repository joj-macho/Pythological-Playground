import random
import time

# DNA Strand template
STRAND = [
    '         ##',
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#'
]

# DNA Base pairs
BASE_PAIRS = [('A', 'T'), ('T', 'A'), ('C', 'G'), ('G', 'C')]

# ANSI color codes
COLOR_MAP = {
    'A': '\033[91m',  # Red
    'T': '\033[92m',  # Green
    'C': '\033[94m',  # Blue
    'G': '\033[93m',  # Yellow
    'RESET': '\033[0m'  # Reset color
}


def main():
    '''Animate the DNA double-helix.'''
    print('DNA Double-Helix Animation.\n')
    strand_length = len(STRAND)
    try:
        # Increment row by row
        strand_row = 0
        while True:
            strand_row += 1
            if strand_row == strand_length:
                strand_row = 0

            if '{}' in STRAND[strand_row]:
                # Generate random nucleotide base pairs
                pair = random.choice(BASE_PAIRS)
                colored_pair = (colorize_base(pair[0]), colorize_base(pair[1]))
                print(STRAND[strand_row].format(
                    colored_pair[0],
                    colored_pair[1])
                )
            else:
                print(STRAND[strand_row])
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('\nAnimation interrupted... Bye!')


def colorize_base(base):
    '''Returns the colored string for a nucleotide base.'''
    return f"{COLOR_MAP[base]}{base}{COLOR_MAP['RESET']}"


if __name__ == '__main__':
    main()
