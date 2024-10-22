import random

# ASCII art for dice faces
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

MAX_DICE = 7  # Fits 79 columns screen


def main():
    '''Do the roll thingy.'''
    print('Dice rolling simulator.\n')
    while True:
        num_of_dice = get_num_of_dice('Enter number of dice to roll or '
                                      '(q)uit to exit:\n> ')
        if num_of_dice is None:
            break

        # Roll the dice and display results
        roll_results = [random.randint(1, 6) for _ in range(num_of_dice)]
        print('\nRolling the dice...\n')
        display_dice_ascii(roll_results)
        print(f'\nDice face result: {roll_results}')
        print(f'Sum of dice faces: {sum(roll_results)}\n')


def get_num_of_dice(prompt):
    '''Prompts for number of dice to roll.'''
    while True:
        response = input(prompt).strip().lower()
        if response in ('q', 'quit'):
            print('Exiting program...Bye!')
            return None
        try:
            num_of_dice = int(response)
            if not 0 < num_of_dice <= MAX_DICE:
                raise ValueError(f'Enter # dice 1-{MAX_DICE}.')
            return num_of_dice
        except ValueError as e:
            print(f'Invalid Input: {e}\n')


def display_dice_ascii(roll_results):
    '''Displays ASCII art for the dice results.'''
    dice_lines = ['' for _ in range(5)]

    for result in roll_results:
        dice_face = DICE_FACES[result]
        for i, line in enumerate(dice_face):
            dice_lines[i] += line + ' '  # Add space between dice faces

    for line in dice_lines:
        print(line)


if __name__ == '__main__':
    main()
