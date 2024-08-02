import random
import sys
import time

# DNA Strand
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
    '        #{}-{}#']


def main():
    '''Main function to run the DNA animation.'''
    print('\nDNA Animation\n')

    try:
        input('Press Enter To Continue...')

        strand_i = 0
        while True:
            # Row increment
            strand_i += 1
            if strand_i == len(STRAND):
                strand_i = 0
            # Indexes 0 and 9 have no nucleotides
            if strand_i == 0 or strand_i == 9:
                print(STRAND[strand_i])
                continue

            # Random Nucleotide pairs
            nucleotide_pairs = [('A', 'T'), ('T', 'A'), ('C', 'G'), ('G', 'C')]
            left_nucleotide, right_nucleotide = random.choice(nucleotide_pairs)

            # Rows
            print(STRAND[strand_i].format(left_nucleotide, right_nucleotide))
            time.sleep(0.15)

    except KeyboardInterrupt:
        print('Goodbye')
        sys.exit()

if __name__ == '__main__':
    main()
