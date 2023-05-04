import sys
import random

# Japanese number Constants
ENG_JAP_NUM = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

def main():
    print('''
Cho-han Game.
A dice game where players must guess if the resulting sum of the dice is even (cho) or odd (han).
    ''')

    money = 5000
    while True:
        print(f'You have ${money}.\n')
        # Prompt player for a valid bet
        while True:
            response = input('Enter you bet amount. Enter (q)uit to exit.\n> ')
            if response.startswith('q'):
                print('Bye!')
                sys.exit()
            elif not response.isdecimal():
                print('Enter a valid bet amount!')
            elif int(response) > money:
                print('You do not have enough money to make the bet!')
            else:
                betAmount = int(response)
                break

        # Roll the Dice
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print('\nDice Rolling...\n')
        
        while True:
            bet = input('Choose Cho (even) OR Han (odd)...\n> ').lower()
            if bet != 'cho' and bet != 'han':
                print('Choose Cho or Han!')
                continue
            else:
                break
        
        # Results
        print('DICE Results:')
        print(f'\t{ENG_JAP_NUM[dice1]} and {ENG_JAP_NUM[dice2]} ,({dice1} and {dice2})')

        if (dice1 + dice2) % 2 == 0:
            winningBet = 'cho'
        else:
            winningBet = 'han'

        playerWin = bet == winningBet
        if playerWin:
            print(f'You Won $ {betAmount}!')
            money += betAmount
        else:
            print(f'You lost $ {betAmount}!')
            money -= betAmount
        
        if money == 0:
            print('You have ran out of money. Bye Loser!')
            sys.exit()

if __name__ == '__main__':
    main()