import random

def main():
    '''Main function for the Carrot in the Box game.'''

    print('''
Carrot in the Box Game. The rules are simple: To win, bluff until you have a box with a carrot in it.
    ''')

    player_1 = input('Enter the name of player 1:\n> ')
    player_2 = input('Enter the name of player 2:\n> ')

    while True:
        play_game(player_1, player_2)

        response = input('Do you want to play again? (y)es or (n)o\n> ')
        if not response.startswith('y'):
            break

def play_game(player_1, player_2):
    '''This function handles the logic for a single round of the game.'''

    # Display initial boxes setup
    print()
    print('''HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    A    | /  |    B    | /
+---------+/   +---------+/''')

    players = player_1[:11].center(11) + '    ' + player_2[:11].center(11)
    print(players)
    print(f'\n{player_1}, you have BOX A in front of you.\n{player_2}, you have BOX B in front of you.\nREADY...?\n')
    print(f'{player_1}, look into your BOX.\n{player_2}, close your eyes.')
    input(f'Press Enter when {player_2} closes their eyes.\n')
    print(f'Inside the BOX of {player_1}:')

    # Randomly determine if the carrot is in Box A
    if random.randint(1, 2) == 1:
        carrot_in_box_1 = True
    else:
        carrot_in_box_1 = False

    # Display the content of the box with or without the carrot
    if carrot_in_box_1:
        # Box A contains the carrot
        print('''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    A    | /  |    B    | /
+---------+/   +---------+/
 (carrot!)''')
        print(players)
    else:
        # Box A doesn't contain the carrot
        print('''
   _________
  |         |
  |         |
  |_________|    __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    A    | /  |    B    | /
+---------+/   +---------+/
(no carrot!)''')
        print(players)

    input('Press Enter to Continue...')

    # Clear screen
    print('\n'*100)
    print(f'{player_1}, tell {player_2} to open their eyes.')
    input('Press Enter to Continue...')

    print()
    print(f'{player_2}, do you want to swap boxes with {player_1}? (y)es or (n)o')
    while True:
        response = input('> ').lower()
        if not (response.startswith('y') or response.startswith('n')):
            print('Please enter a valid (y)es or (n)o.')
        else:
            break

    # Swap boxes if desired and display the result
    box_1 = 'A '
    box_2 = 'B'

    if response.startswith('y'):
        carrot_in_box_1 = not carrot_in_box_1
        box_1, box_2 = box_2, box_1

    print('''HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    {}    | /  |  {}    | /
+---------+/   +---------+/'''.format(box_1, box_2))

    print(players)
    input('Press Enter to Show the Winner.')
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
|    {}    | /  |  {}      | /
+---------+/   +---------+/'''.format(box_1, box_2))
    else:
        print('''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|   {}     | /  |  {}      | /
+---------+/   +---------+/'''.format(box_1, box_2))

    print(players)

    # Determine and display the winner
    if carrot_in_box_1:
        print(f'{player_1} is the winner.')
    else:
        print(f'{player_2} is the winner.')

if __name__ == '__main__':
    main()
