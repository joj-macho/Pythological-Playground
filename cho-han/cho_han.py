import random

# ASCII art for each dice face
DICE_FACES = {
    1: (
        '+-------+',
        '|       |',
        '|   O   |',
        '|       |',
        '+-------+'
    ),
    2: (
        '+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'
    ),
    3: (
        '+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'
    ),
    4: (
        '+-------+',
        '| O   O |',
        '|       |',
        '| O   O |',
        '+-------+'
    ),
    5: (
        '+-------+',
        '| O   O |',
        '|   O   |',
        '| O   O |',
        '+-------+'
    ),
    6: (
        '+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'
    )
}

# Numbers dict
NUMBERS = {
    1: 'ICHI', 2: 'NI', 3: 'SAN',
    4: 'SHI', 5: 'GO', 6: 'ROKU'
}


def main():
    '''Play the Cho-Han Game.'''

    print('Cho-Han Dice Game.\n')
    print('Guess the sum of dice roll, cho (even) or han (odd).\n')

    player_cash = 100

    while True:
        print(f'You have {player_cash} in your pockets.\n')

        # Get player bet
        bet_amount = get_bet(player_cash)
        if bet_amount is None:
            break

        print(f'\nYour bet is {bet_amount}\n')

        # Roll the dice
        print('Rolling the dice...\n')
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        # print(f'RESULTS: {dice_1} and {dice_2}')  # SEE RESULT

        # Get player's guess
        player_guess = get_player_guess()
        if player_guess is None:
            break

        # Results
        dice_result = 'cho' if (dice_1 + dice_2) % 2 == 0 else 'han'

        print('\nDice Results:')
        # print_dice_results(dice_1, dice_2)
        dice_faces = [DICE_FACES[die] for die in (dice_1, dice_2)]
        for rows in zip(*dice_faces):
            print('  '.join(rows))

        print(f'{NUMBERS[dice_1]:^9} '
              f'& {NUMBERS[dice_2]:^9}')

        player_win = player_guess == dice_result

        # Adjust player cash based on the results
        if player_win:
            print(f'\nCongratulations! You won {bet_amount}\n')
            player_cash += bet_amount
        else:
            print(f'\nSorry, you lost ${bet_amount}\n')
            player_cash -= bet_amount

        # Check if the player still has cash
        if player_cash == 0:
            print('You have run out of money...Bye!')
            break


def get_bet(funds):
    '''Prompts for a valid bet amount.'''
    while True:
        response = input('Enter your bet amount or (q)uit to exit:\n> ')
        if response in ('q', 'quit'):
            print('Bye!')
            return None
        try:
            bet_amount = float(response)
            if bet_amount <= 0:
                raise ValueError('Enter positive bet amount.')
            if bet_amount > funds:
                raise ValueError(f'Enter bet less than {funds}.')
            return bet_amount
        except ValueError as e:
            print(f'Invalid bet: {e}\n')


def get_player_guess():
    '''Prompts the player for a guess, cho or han.'''
    while True:
        guess = input('Choose Cho (even) or Han (odd):\n> ').lower()
        if guess in ('q', 'quit'):
            print('Bye!')
            return None

        if guess not in ('cho', 'han'):
            print('Invalid guess! Guess Cho or Han.\n')
        else:
            return guess


if __name__ == '__main__':
    main()
