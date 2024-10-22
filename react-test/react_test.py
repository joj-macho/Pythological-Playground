import random
import time

# Constants
MIN_DELAY = 0.5
MAX_DELAY = 1.5
ROUND_LIMIT = 5


def main():
    '''Test your reaction speed.'''
    print('''Fast Draw Game!

When you see "Draw", you have 0.3 seconds to press Enter.
You lose if you press Enter before the word "Draw" appears
    ''')

    input('Press Enter To Continue ...')

    for round_num in range(1, ROUND_LIMIT + 1):
        print(f'\nRound {round_num}:')
        print('Ready ....')

        # Pause for a random interval between 0.5 and 1.5 seconds
        time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
        print('DRAW!')

        draw_time = time.time()
        input()
        time_elapsed = time.time() - draw_time

        if time_elapsed < 0.01:
            print('You drew before "DRAW" appeared. You lose!')
        elif time_elapsed > 0.3:
            time_elapsed = round(time_elapsed, 3)
            print(f'You took {time_elapsed} seconds to Draw. Too Slow')
        else:
            time_elapsed = round(time_elapsed, 2)
            print(f'You took {time_elapsed} seconds to Draw.')
            print('You are the fastest draw in the West!')

        if round_num == ROUND_LIMIT:
            print('\nGame Over!')
            break

        # Play Again?
        play_again = input('Press Enter to Play again, or enter (q)uit '
                           'to exit.\n> ').lower()
        while play_again not in ('', 'q', 'quit'):
            play_again = input('Invalid input. Press Enter to Play again, '
                               'or enter (q)uit to quit.\n> ').lower()

        if play_again.startswith('q'):
            print('Bye!')
            break

        time.sleep(1)


if __name__ == '__main__':
    main()
