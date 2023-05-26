import random

# A dictionary containing the ASCII characters of each dice face
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

# The height of each dice face in rows
DICE_HEIGHT = len(DICE_FACES[1])
# Maximum allowed dice
MAX_DICE = 6


def main():
    '''This is the main function. It prompts the user to input the number of dice to roll, generates random dice roll results, and displays the ASCII representation of the rolled dice faces.'''

    print('\nDice Rolling Simulator\n')

    while True:
        num_of_dice = get_num_of_dice()
        dice_roll_results = roll_dice(num_of_dice)

        print('RESULTS:')
        show_dice_face = generate_dice_face(dice_roll_results)
        print(show_dice_face)

        if not play_again():
            break


def get_num_of_dice():
    '''This function prompts user to choose the number of dice to roll.'''

    while True:
        try:
            response = int(input(f'How many dice do you want to roll (max {MAX_DICE} dice)?\n> '))
            if 0 < response <= MAX_DICE:
                return response
            print(f'Enter a valid number of dice to roll (1-{MAX_DICE})!')
        except ValueError:
            print('Enter a valid number!')


def roll_dice(num_of_dice):
    '''This function rolls the dice using the random module.'''

    return [random.randint(1, 6) for _ in range(num_of_dice)]


def generate_dice_face(dice_roll_results):
    '''This function returns the ASCII characters of a rolled die.'''

    try:
        dice_face = [DICE_FACES[face] for face in dice_roll_results]
    except KeyError:
        return 'Invalid dice face encountered.'

    dice_face_rows = [' '.join(die_row) for die_row in zip(*dice_face)]
    show_dice_face = '\n'.join(dice_face_rows)

    return show_dice_face


def play_again():
    '''This function prompts the user to play again.'''

    while True:
        response = input('Do you want to roll again? (y/n)\n> ').lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print('Enter either "y" or "n"!')


if __name__ == '__main__':
    main()