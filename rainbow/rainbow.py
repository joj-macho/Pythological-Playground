import time
import bext

INDENT_LIMIT = 60

def main():
    '''Simulate a colorful rainbow animation with increasing and decreasing indentation.'''

    print('\nWelcome to The Rainbow Simulation.\n')
    input('Press enter to Continue ...')

    indent = 0
    indent_increase = True

    print("Press Ctrl+C to exit.")

    try:
        while True:
            print(' ' * indent, end='')

            # Print colored blocks to represent the rainbow
            bext.fg('red')
            print('##', end='')

            bext.fg('yellow')
            print('##', end='')

            bext.fg('green')
            print('##', end='')

            bext.fg('blue')
            print('##', end='')

            bext.fg('cyan')
            print('##', end='')

            bext.fg('purple')
            print('##')

            if indent_increase:
                # Increase the number of spaces:
                indent += 1
                if indent == INDENT_LIMIT:
                    indent_increase = False
            else:
                # Decrease the number of spaces:
                indent -= 1
                if indent == 0:
                    indent_increase = True

            time.sleep(0.02)

    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\nExiting...')


if __name__ == '__main__':
    main()
