import random
import sys
import time

def main():
    '''Main function to display an animated deep cave tunnel.'''
    print('\nDeep Cave Tunnel Animation. \nPress Ctrl-C to stop.\n')

    # Pause for 2 seconds before starting animation.
    time.sleep(2)

    left_width = 20
    gap_width = 10

    try:
        while True:
            display_tunnel_segment(left_width, gap_width)
            time.sleep(0.05)  # Pause for a short time to create animation effect.

            adjust_tunnel_width = random.randint(1, 6)
            if adjust_tunnel_width == 1 and left_width > 1:
                left_width -= 1  # Decrease left side width.
            elif adjust_tunnel_width == 2 and left_width + gap_width < 69:
                left_width += 1  # Increase left side width.

    except KeyboardInterrupt:
        print('\nExiting the program...')

def display_tunnel_segment(left_width, gap_width):
    '''Display a segment of the deep cave tunnel.'''
    tunnel_width = 70
    right_width = tunnel_width - gap_width - left_width
    print('#' * left_width + ' ' * gap_width + '#' * right_width)

if __name__ == '__main__':
    main()

