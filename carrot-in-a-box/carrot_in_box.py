import random
import os


def main():
    '''Play the Carrot in the Box game.'''

    print('Carrot in the Box Game.\n')
    print('Bluff until you have a box with a carrot in it.\n')

    player_1 = get_player_name('Player 1')
    player_2 = get_player_name('Player 2')

    while True:
        # Show initial boxes and player names
        print()
        print('''HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    A    | /  |    B    | /
+---------+/   +---------+/''')

        players = player_1[:11].center(11) + '      ' + \
            player_2[:11].center(11)
        print(players)
        print()
        print(f'{player_1}, you have BOX A in front of you.')
        print(f'{player_2}, you have BOX B in front of you.')
        print('READY...?\n')
        print(f'{player_1}, look into your BOX.')
        print(f'{player_2}, close your eyes.')
        input(f'Press Enter when {player_2} closes their eyes.\n')
        print(f'Inside the BOX of {player_1}:')

        carrot_in_box_1 = random.choice([True, False])

        if carrot_in_box_1:
            print('''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    A    | /  |    B    | /
+---------+/   +---------+/
 (carrot!)''')
        else:
            print('''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    A    | /  |    B    | /
+---------+/   +---------+/
(no carrot!)''')

        print(players)

        input('Press Enter to Continue...')
        # Clear screen
        # print('\n'*100)
        os.system('clear' if os.name == 'posix' else 'cls')

        print(f'{player_1}, tell {player_2} to open their eyes.')
        input('Press Enter to Continue...')

        print()
        print(f'{player_2}, do you want to swap boxes with {player_1}? '
              '(y)es or (n)o')
        response = get_valid_response(('y', 'yes', 'n', 'no'))

        box_1 = 'A '
        box_2 = 'B '

        if response in ('y', 'yes'):
            carrot_in_box_1 = not carrot_in_box_1
            box_1, box_2 = box_2, box_1

        print('''HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    {}   | /  |    {}   | /
+---------+/   +---------+/'''.format(box_1, box_2))

        print(players)
        input('\nPress Enter to Show the Winner.')
        print()

        if carrot_in_box_1:
            print('''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    {}   | /  |    {}   | /
+---------+/   +---------+/
 (carrot!)'''.format(box_1, box_2))
        else:
            print('''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    {}   | /  |    {}   | /
+---------+/   +---------+/
(no carrot!)'''.format(box_1, box_2))

        print(players)

        if carrot_in_box_1:
            print(f'\n{player_1} is the winner.')
        else:
            print(f'\n{player_2} is the winner.')

        # Play again?
        play_again = input('\nDo you want to play again? (y)es or (n)o\n> ')
        if play_again.lower() in ('n', 'no'):
            print('Bye!')
            break


def get_player_name(player_number):
    '''Prompts for player 1 and player 2 names.'''
    while True:
        player_name = input(f'Enter the name of {player_number}:\n> ')
        if len(player_name) > 10:
            print('Player name should not exceed 10 characters.')
        else:
            return player_name


def get_valid_response(valid_responses):
    '''Gets a valid response from the user.'''
    while True:
        response = input('> ').lower()
        if response not in valid_responses:
            print('Please enter a valid (y)es or (n)o response.')
        else:
            return response


if __name__ == '__main__':
    main()
