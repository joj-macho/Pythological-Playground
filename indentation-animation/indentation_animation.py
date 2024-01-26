import time
import sys

def main():
    '''Main function to animate an indentation effect with asterisks.'''
    print('\nIndentation Animation.\n')
    
    indent = 0  # Spaces to indent.
    is_indent_increasing = True  
    sleep_duration = 0.1  

    try:
        while True:  
            print(' ' * indent, end='')
            print('********')
            time.sleep(sleep_duration)

            if is_indent_increasing:
                # Increase the number of spaces:
                indent += 1
                if indent == 20:
                    # Reverse direction:
                    is_indent_increasing = False
            else:
                # Decrease the number of spaces:
                indent -= 1
                if indent == 0:
                    # Reverse direction:
                    is_indent_increasing = True

    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
