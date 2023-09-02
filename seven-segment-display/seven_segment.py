def main():
    '''Main function for the Seven-Segment Number Display program.'''

    print('\nSeven-Segment Number Display\n')
    
    # Check to see if valid number entered.
    while True:
        response = input('Enter number to show:\n> ')
        if not response.isdecimal():
            continue
        else:
            response = int(response)
            break

    print(generate_seven_segments(response))
    print()


def generate_seven_segments(number, minWidth=0):
    '''Generate a seven-segment display for a given number.'''

    # Convert number to a string and apply zero-padding if necessary
    number = str(number).zfill(minWidth)

    # Initialize the three rows of the seven-segment display
    rows = ['', '', '']

    # Iterate through each numeral in the input number
    for i, numeral in enumerate(number):
        # Handle decimal points
        if numeral == '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue

        # Define the seven-segment patterns for each numeral
        # For simplicity, we represent the segments with spaces, underscores, and vertical bars
        # 0, 2, 3, 5, 6, 7, 8, and 9 use different segments, while 1 and 4 use fewer segments
        # Adjusted individual segments to create the appropriate numeral
        elif numeral == '-':
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        # Add space between numerals unless the next numeral has a decimal point
        if i != len(number) - 1 and number[i + 1] != '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    # Combine the three rows to create the final display
    return '\n'.join(rows)


if __name__ == '__main__':
    main()
