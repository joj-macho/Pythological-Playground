import random

def main():
    '''
    
    '''
    
    print('''
Carrot in the Box Game. The rules are simple; To win, bluff until you have a box with a carrot in it.
    ''')

    player1 = input('Enter the name of player 1:\n> ')
    player2 = input('Enter the name of player 2:\n> ')
    # Display players
    players = player1[:11].center(11) + '    ' + player2[:11].center(11)
    # print(players)

    print()
    print('''HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    A    | /  |    B    | /
+---------+/   +---------+/''')

    print(players)
    print(f'\n{player1} you have BOX A in front of you.\n{player2} you have BOX B in front of you.\nREADY...?\n')
    print(f'{player1} look into your BOX.\n{player2} close your eyes.')
    print(f'Press Enter when {player2} closes their eyes.\n')
    input()
    print(f'Inside the BOX of {player1}:')

    if random.randint(1, 2) == 1:
        carrot_in_box1 = True
    else:
        carrot_in_box1 = False

    if carrot_in_box1:
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
    print(f'{player1} tell {player2} to open their eyes.')
    input('Press Enter to Continue...')

    print()
    print(f'{player2} do you want to swap boxes with {player1}, (y)es or (n)o?')
    # Enter valid yes or no
    while True:
        response = input('> ').lower()
        if not (response.startswith('y') or response.startswith('n')):
            print(f'Please Enter a Valid (y)es or (n)o.')
        else:
            break

    box1 = 'A '
    box2 = 'B'

    if response.startswith('y'):
        carrot_in_box1 = not carrot_in_box1
        box1, box2 = box2, box1

    print('''HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    {}    | /  |  {}    | /
+---------+/   +---------+/'''.format(box1, box2))

    print(players)
    input('Press Enter to Show the Winner.')
    print()

    if carrot_in_box1:
        print('''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   BOX   | |  |   BOX   | |
|    {}    | /  |  {}      | /
+---------+/   +---------+/'''.format(box1, box2))

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
+---------+/   +---------+/'''.format(box1, box2))

    print(players)

    if carrot_in_box1:
        print(f'{player1} is the winner.')
    else:
        print(f'{player2} is the winner.')

if __name__ == '__main__':
    main()
