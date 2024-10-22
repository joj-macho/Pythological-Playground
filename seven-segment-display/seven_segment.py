def main():
    '''Display digits using seven-segments.'''
    print('The Seven-Segment Display Simulator!\n')
    print('Enter digit(s) (0-9) to display, or (q)uit to exit.')

    while True:
        response = input('> ').lower()
        if response.startswith('q'):
            print('Bye!')
            break

        try:
            number = response
            if not number.isnumeric():
                raise ValueError
            print(seven_segment_display(number))
            print()
        except ValueError:
            print('Enter a valid positive integer (0-9)!\n')


def seven_segment_display(number):
    '''
    Generates a seven-segment display for a given number.

    Parameters:
        number (str): The number to display as a string.

    Returns:
        str: A string representation of the seven-segment display.
    '''
    segment_map = {
        '0': ' _ \n| |\n|_|\n',
        '1': '   \n  |\n  |\n',
        '2': ' _ \n _|\n|_ \n',
        '3': ' _ \n _|\n _|\n',
        '4': '   \n|_|\n  |\n',
        '5': ' _ \n|_ \n _|\n',
        '6': ' _ \n|_ \n|_|\n',
        '7': ' _ \n  |\n  |\n',
        '8': ' _ \n|_|\n|_|\n',
        '9': ' _ \n|_|\n _|\n'
    }

    lines = ['', '', '']
    for char in number:
        display = segment_map.get(char, 'Invalid')
        if display == 'Invalid':
            lines[0] += 'Invalid '
            lines[1] += 'Invalid '
            lines[2] += 'Invalid '
        else:
            segments = display.split('\n')
            lines[0] += segments[0] + ' '
            lines[1] += segments[1] + ' '
            lines[2] += segments[2] + ' '

    return '\n'.join(lines)


if __name__ == '__main__':
    main()
