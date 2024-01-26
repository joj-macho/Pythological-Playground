import random
import time
import sys

# Constants
DRAW_DELAY_MIN = 0.5
DRAW_DELAY_MAX = 1.5
DELAY_BEFORE_RESULTS = 1.0
ROUND_LIMIT = 5

def main():
    '''Main function to run the fast draw game.'''
    print('''
Welcome to Fast Draw Game!
Let us see if you are the fastest draw in the west.

When you see "Draw", you have 0.3 seconds to press Enter.
You lose if you press Enter before the word "Draw" appears
    ''')

    input('Press Enter To Continue ...')

    wins = 0
    losses = 0

    for round_num in range(1, ROUND_LIMIT + 1):
        print(f'\nRound {round_num}:')
        print('Ready ....')
        
        # Pause for a random interval between 0.5 and 1.5 seconds
        time.sleep(random.uniform(DRAW_DELAY_MIN, DRAW_DELAY_MAX))
        print('DRAW!')
        
        draw_time = time.time()
        input()
        time_elapsed = time.time() - draw_time

        if time_elapsed < 0.01:
            print('You drew before "DRAW" appeared. You lose!')
            losses += 1
        elif time_elapsed > 0.3:
            time_elapsed = round(time_elapsed, 3)
            print(f'You took {time_elapsed} seconds to Draw. Too Slow')
            losses += 1
        else:
            time_elapsed = round(time_elapsed, 2)
            print(f'You took {time_elapsed} seconds to Draw.')
            print('You are the fastest draw in the West!')
            wins += 1

        print(f'Score: Wins = {wins}, Losses = {losses}')

        if round_num == ROUND_LIMIT:
            print('\nGame Over!')
            print(f'Final Score: Wins = {wins}, Losses = {losses}')
            break

        # Play Again?
        play_again = input('Press Enter to Play again, or enter (q)uit to exit.\n> ').lower()
        while play_again not in ('', 'q', 'quit'):
            play_again = input('Invalid input. Press Enter to Play again, or enter (q)uit to quit.\n> ').lower()

        if play_again.startswith('q'):
            print('Bye!')
            sys.exit()

        time.sleep(DELAY_BEFORE_RESULTS)

if __name__ == '__main__':
    main()
