import random
import time

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

OPTIONS = {'r': ('Rock', ROCK), 'p': ('Paper', PAPER),
           's': ('Scissors', SCISSORS)}


def main():
    '''Play Rock Paper Scissors Game.'''
    print('''Rock Paper Scissors Game.

Game Rules;
    - Rock smashes Scissors
    - Paper covers Rock
    - Scissors cut Paper
''')
    wins, losses, ties = 0, 0, 0

    while True:
        player_move = get_player_move()
        if player_move is None:
            break

        # Player Move
        print(f'\nPlayer Move: {player_move[0]} {player_move[1]} '
              f'\nVS.', end='', flush=True)

        # Computer Move
        computer_move = random.choice(list(OPTIONS.values()))
        time.sleep(.75)
        print(f'\n\nComputer Move: {computer_move[0]} {computer_move[1]}')
        time.sleep(0.5)

        # Display game results
        if player_move == computer_move:
            print('A tie!\n')
            ties += 1

        elif (player_move[0] == 'Rock' and computer_move[0] == 'Scissors') or\
            (player_move[0] == 'Scissors' and computer_move[0] == 'Paper') \
                or (player_move[0] == 'Paper' and computer_move[0] == 'Rock'):
            print('You Win!\n')
            wins += 1

        elif (player_move[0] == 'Scissors' and computer_move[0] == 'Rock') or\
            (player_move[0] == 'Paper' and computer_move[0] == 'Scissors') or\
                (player_move[0] == 'Rock' and computer_move[0] == 'Paper'):
            print('You Lose!\n')
            losses += 1

        # Scores
        print(f'{wins} Wins | {losses} Losses | {ties} Ties')
        print()


def get_player_move():
    '''Prompts player for a r, p, s move.'''
    while True:
        print('Enter (r)ock, (p)aper, or (s)cissors. Enter (q)uit to exit.')
        response = input('> ').strip().lower()

        if response in ('q', 'quit'):
            print('Exiting game...Bye!')
            return None

        if response in ('r', 'rock', 'p', 'paper', 's', 'scissors'):
            move = OPTIONS[response[0]]
            return move
        else:
            continue


if __name__ == '__main__':
    main()
