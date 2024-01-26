import random
import time
import sys

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

OPTIONS = {'r': ('Rock', ROCK), 'p': ('Paper', PAPER), 's': ('Scissors', SCISSORS)}

def main():
    '''This is the main game program'''

    print('''
Rock Paper Scissors Game. The rules of the game are simple;
    - Rock smashes Scissors
    - Paper Covers Rock
    - Scissors Cut Paper
''')

    # Track score
    wins, losses, ties = 0, 0, 0

    while True:
        while True:
            print(f'{wins} Wins     {losses} Losses     {ties} Ties')
            response = input(
                'Enter (r)ock, (p)aper, or (s)cissors. Enter (q)uit to exit.\n> ').lower()
            if response.startswith('q'):
                print('Bye!')
                sys.exit()
            if response in OPTIONS:
                player_move = OPTIONS[response]
                break
            else:
                print('Type Valid (r), (p), (s), or (q) to exit!')

        # Player Move
        print(f'\n{player_move[0]} {player_move[1]} vs.', end='', flush=True)

        # Computer Move
        computer_move = random.choice(list(OPTIONS.values()))
        time.sleep(1)
        print(f'\n{computer_move[0]} {computer_move[1]}')
        time.sleep(0.5)

        # Display game results
        if player_move == computer_move:
            print('A tie!\n')
            ties += 1

        elif (player_move[0] == 'Rock' and computer_move[0] == 'Scissors') or (player_move[0] == 'Scissors' and computer_move[0] == 'Paper') or (player_move[0] == 'Paper' and computer_move[0] == 'Rock'):
            print('You Win!\n')
            wins += 1

        elif (player_move[0] == 'Scissors' and computer_move[0] == 'Rock') or (player_move[0] == 'Paper' and computer_move[0] == 'Scissors') or (player_move[0] == 'Rock' and computer_move[0] == 'Paper'):
            print('You Lose!\n')
            losses += 1

if __name__ == '__main__':
    main()