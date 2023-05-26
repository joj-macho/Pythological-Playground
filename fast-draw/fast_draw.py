import random
import time
import sys

DRAW_DELAY_MIN = 0.5
DRAW_DELAY_MAX = 1.5
DELAY_BEFORE_RESULTS = 1.0
ROUND_LIMIT = 10

def main():
    '''This function represents the main logic of the Fast Draw game. It prompts the user to press Enter when the word "Draw" appears on the screen and measures the time it takes for the user to respond. Based on the response time, it determines whether the user wins or loses the round. The function keeps track of the score and offers the option to play again or quit. It provides a user-friendly experience with clear instructions and feedback.'''

    # Introduction and instructions for the game
    print('\nFast Draw!\nLet us see if you are the fastest draw in the west. \n\nWhen you see "Draw", you have 0.3 seconds to press Enter. You lose if you press Enter before the word "Draw" appears')
    input('Press Enter To Continue ...')
        

    # Initialize score counters
    wins = 0
    losses = 0

    for round_num in range(1, ROUND_LIMIT + 1):
        print(f'\nRound {round_num}:')
        print('Ready ....')
        # Pause for a random interval between 0.5 and 1.5 seconds
        time.sleep(random.uniform(DRAW_DELAY_MIN, DRAW_DELAY_MAX))
        print('DRAW!')
        # Record the current time
        draw_time = time.time()
        # Wait for user input (Enter key press)
        input()
        time_elapsed = time.time() - draw_time

        # Determine the outcome based on the response time
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

        # Display the current score
        print(f'Score: Wins = {wins}, Losses = {losses}')

        # Check if round limit is reached
        if round_num == ROUND_LIMIT:
            print('\nGame Over!')
            print(f'Final Score: Wins = {wins}, Losses = {losses}')
            break

        # Ask to play again
        response = input('Press Enter to Play again, or enter (q)uit to quit.\n> ').lower()
        while response not in ['', 'q', 'quit']:
            response = input('Invalid input. Press Enter to Play again, or enter (q)uit to quit.\n> ').lower()

        if response == 'q' or response == 'quit':
            print('Bye!')
            sys.exit()

        # Delay before displaying results for the next round
        time.sleep(DELAY_BEFORE_RESULTS)

if __name__ == '__main__':
    main()
