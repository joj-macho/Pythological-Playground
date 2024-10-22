import random
import time

WIDTH = 70
GAP_SIZE = 15


def main():
    '''Animate cave descent.'''
    print('Cave Descent Animation.\n')
    input('Press Enter to start...\n')

    left_gap_position = WIDTH // 2 - GAP_SIZE // 2

    try:
        while True:
            for _ in range(10):
                # Adjust the gap position slightly
                left_gap_position += random.choice([-1, 0, 1])
                # Keep gap within bounds
                left_gap_position = max(
                    0, min(WIDTH - GAP_SIZE - 2, left_gap_position))

                segment = generate_tunnel_segment(left_gap_position)
                print(segment)

            time.sleep(0.1)
    except KeyboardInterrupt:
        print('\nProgram interrupted! Exiting...')


def generate_tunnel_segment(left_gap_position):
    '''Generates a tunnel segment.'''
    left_side = '.' * left_gap_position + '\\'
    right_side = '\\' + '.' * (WIDTH - left_gap_position - GAP_SIZE - 2)
    middle = ' ' * GAP_SIZE
    return left_side + middle + right_side


if __name__ == '__main__':
    main()
