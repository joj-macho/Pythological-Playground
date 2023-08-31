import sys
import random

# Japanese number Constants
ENG_JAP_NUM = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

def main():
    '''Main function for the Cho-han game.'''

    print('''
Cho-han Game.
A dice game where players must guess if the resulting sum of the dice is even (cho) or odd (han).
    ''')

    funds = 5000
    while True:
        print(f'You have ${funds}.\n')

        # Prompt player for a valid bet
        while True:
            response = input('Enter you bet amount. Enter (q)uit to exit.\n> ')
            if response.startswith('q'):
                print('Bye!')
                sys.exit()
            elif not response.isdecimal():
                print('Enter a valid bet amount!')
            elif int(response) > funds:
                print('You do not have enough money to make the bet!')
            else:
                bet_amount = int(response)
                break

        # Roll the Dice
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print('\nDice Rolling...\n')

        # Prompt player to choose Cho (even) or Han (odd)
        while True:
            bet = input('Choose Cho (even) OR Han (odd)...\n> ').lower()
            if bet != 'cho' and bet != 'han':
                print('Choose Cho or Han!')
                continue
            else:
                break
        
        # Display dice roll results
        print('DICE Results:')
        print(f'\t{ENG_JAP_NUM[dice1]} and {ENG_JAP_NUM[dice2]} ,({dice1} and {dice2})')

        # Determine winning bet
        if (dice1 + dice2) % 2 == 0:
            winning_bet = 'cho'
        else:
            winning_bet = 'han'

        # Check if player's bet matches the winning bet
        player_win = bet == winning_bet
        if player_win:
            print(f'You Won $ {bet_amount}!')
            funds += bet_amount
        else:
            print(f'You lost $ {bet_amount}!')
            funds -= bet_amount

        # Check if player is out of money
        if funds == 0:
            print('You have ran out of money. Bye Loser!')
            sys.exit()

if __name__ == '__main__':
    main()