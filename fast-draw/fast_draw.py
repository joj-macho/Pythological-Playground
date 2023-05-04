import random
import time
import sys

def main():
    '''This is the main function'''

    print('\nFast Draw!\nLet us see if you are the fastest draw in the west. \n\nWhen you see "Draw", you have 0.3 seconds to press Enter. You lose if you press Enter before the word "Draw" appears')
    input('Press Enter To Continue ...')

    # Initialize score counters
    wins = 0
    losses = 0

    while True:
        print('Ready ....')
        time.sleep(random.uniform(0.5, 1.5))
        print('DRAW!')
        draw_time = time.time()
        input()
        time_elapsed = time.time() - draw_time

        if time_elapsed < 0.01:
            print('You drew before "DRAW" appeared. You lose!')
            losses += 1

        elif time_elapsed > 0.3:
            time_elapsed = round(time_elapsed, 4)
            print(f'You took {time_elapsed} seconds to Draw. Too Slow')
            losses += 1
            
        else:
            time_elapsed = round(time_elapsed, 4)
            print(f'You took {time_elapsed} seconds to Draw. \nYou are the fastest draw in the West!')
            wins += 1

        # Display score
        print(f'\nScore: Wins = {wins}, Losses = {losses}')

        # Ask to play again
        response = input('Press Enter to Play again, or enter (q)uit to quit.\n> ').lower()
        if response == 'q' or response == 'quit':
            print('Bye!')
            sys.exit()

if __name__ == '__main__':
    main()
