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


def main():
    '''
    The main driver code
    '''
    print('Dice Rolling Simulator\n')

    # Prompt user to choose number of dice to roll
    while True:
        response = input('How many dice do you want to roll (max 6 dice)?\n> ')
        
        if response.isdigit() and 0 < int(response) <= 6:
            num_of_dice = int(response)
            break
        else:
            print('Enter a valid number of dice to roll!')
    
    # Roll the dice using the random module.
    dice_roll_results = [random.randint(1, 6) for _ in range(num_of_dice)]

    # Display Dice Faces
    show_dice_face = generate_dice_face(dice_roll_results)
    print('RESULTS:')
    print(show_dice_face)


def generate_dice_face(dice_roll_results):
    '''
    This function returns the ASCII characters of a rolled die.
    It takes a list of dice roll results as a parameter.
    '''
    # List of dice face characters
    dice_face = [DICE_FACES[face] for face in dice_roll_results]
    # print(diceFace)
    
    # List of dice face rows
    dice_face_rows = []
    for row in range(DICE_HEIGHT):
        row_item = []
        for die in dice_face:
            row_item.append(die[row])
        row_text = ' '.join(row_item)
        dice_face_rows.append(row_text)

    show_dice_face = '\n'.join(dice_face_rows)

    return show_dice_face


if __name__ == '__main__':
    main()