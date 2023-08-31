import random
import sys
import time


def main():
    '''This is the main function. It displays an animated deep cave tunnel.'''
    
    print('\nDeep Cave Tunnel Animation. \nPress Ctrl-C to stop.\n')

    # # Pause for 2 seconds before starting animation.
    time.sleep(2)

    left_width = 20
    gap_width = 10

    try:
        while True:
            display_tunnel_segment(left_width, gap_width)
            time.sleep(0.05)  # Pause for a short time (0.05 seconds) to create animation effect.

            dice_roll = random.randint(1, 6)
            if dice_roll == 1 and left_width > 1:
                left_width -= 1  # Decrease left side width.
            elif dice_roll == 2 and left_width + gap_width < 69:
                left_width += 1  # Increase left side width.

    except KeyboardInterrupt:
        print('\nExiting the program...')


def display_tunnel_segment(left_width, gap_width):
    '''This function displays a segment of the deep cave tunnel.'''

    tunnel_width = 70
    right_width = tunnel_width - gap_width - left_width
    print('#' * left_width + ' ' * gap_width + '#' * right_width)



if __name__ == '__main__':
    main()

