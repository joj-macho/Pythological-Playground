import shutil
import sys
import os

# Set the working directory to the script's directory
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

# Set up constants for terminal dimensions and characters
UP_DOWN_CHAR = chr(9474)         # │
LEFT_RIGHT_CHAR = chr(9472)      # ─
DOWN_RIGHT_CHAR = chr(9484)      # ┌
DOWN_LEFT_CHAR = chr(9488)       # ┐
UP_RIGHT_CHAR = chr(9492)        # └
UP_LEFT_CHAR = chr(9496)         # ┘
UP_DOWN_RIGHT_CHAR = chr(9500)   # ├
UP_DOWN_LEFT_CHAR = chr(9508)    # ┤
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # ┬
UP_LEFT_RIGHT_CHAR = chr(9524)   # ┴
CROSS_CHAR = chr(9532)           # ┼

CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH -= 1
CANVAS_HEIGHT -= 5

canvas = {}
cursor_x, cursor_y = 0, 0
moves = []


def main():
    '''Draw stuff on screen.'''
    while True:
        print(generate_canvas_string(canvas, cursor_x, cursor_y))

        print('Use WASD keys to move, (H)elp screen, (C)lear canvas, '
              '(E)xport to save, or (Q)UIT to exit.')

        response = input('> ').upper()

        if response == 'QUIT' or response == 'Q':
            print('Thanks for playing!')
            sys.exit()
        elif response == 'HELP' or response == 'H':
            print_help()
        elif response == 'CLEAR' or response == 'C':
            clear_canvas()
            moves.append('C')
        elif response == 'EXPORT' or response == 'E':
            save_canvas()
        else:
            process_moves(response)


def process_moves(moves_str):
    '''Processes the movement commands.'''
    for command in moves_str:
        if command in ('W', 'A', 'S', 'D'):
            record_move(command)
        else:
            continue


def record_move(command):
    '''Records the move and updates the canvas.'''
    moves.append(command)
    if not canvas:
        initialize_canvas(command)

    move_cursor(command)
    update_canvas(command)


def initialize_canvas(command):
    '''Initializes the canvas based on the first move.'''
    if command in ('W', 'S'):
        canvas[(cursor_x, cursor_y)] = {'W', 'S'}
    elif command in ('A', 'D'):
        canvas[(cursor_x, cursor_y)] = {'A', 'D'}


def move_cursor(command):
    '''Moves the cursor position.'''
    global cursor_x, cursor_y
    if command == 'W' and cursor_y > 0:
        canvas[(cursor_x, cursor_y)].add(command)
        cursor_y -= 1
    elif command == 'S' and cursor_y < CANVAS_HEIGHT - 1:
        canvas[(cursor_x, cursor_y)].add(command)
        cursor_y += 1
    elif command == 'A' and cursor_x > 0:
        canvas[(cursor_x, cursor_y)].add(command)
        cursor_x -= 1
    elif command == 'D' and cursor_x < CANVAS_WIDTH - 1:
        canvas[(cursor_x, cursor_y)].add(command)
        cursor_x += 1
    else:
        return


def update_canvas(command):
    '''Updates the canvas data based on the move.'''
    if (cursor_x, cursor_y) not in canvas:
        canvas[(cursor_x, cursor_y)] = set()

    if command == 'W':
        canvas[(cursor_x, cursor_y)].add('S')  # Vertical line below cursor
    elif command == 'S':
        canvas[(cursor_x, cursor_y)].add('W')  # Vertical line above cursor
    elif command == 'A':
        canvas[(cursor_x, cursor_y)].add('D')  # Horizon line to the right
    elif command == 'D':
        canvas[(cursor_x, cursor_y)].add('A')  # Horizontal line to the left


def clear_canvas():
    '''Clears the canvas data.'''
    global canvas
    canvas = {}


def save_canvas():
    '''Saves the canvas data to a text file.'''
    try:
        print('Enter filename to save to:')
        filename = input('> ')

        if not filename.endswith('.txt'):
            filename += '.txt'

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(''.join(moves) + '\n')
            file.write(generate_canvas_string(canvas, None, None))

        print('Canvas saved successfully.')
    except Exception as e:
        print(f'An error occurred while saving the canvas: {e}')


def print_help():
    '''Prints the help information.'''
    print('Welcome to the Etch-A-Sketch Simulator!')
    print('Use the following commands to draw and interact with the canvas:')
    print('---------------------------------------------------------------')
    print('WASD - Move the cursor and draw lines:')
    print('  W - Move Up   (Draws a vertical line below the cursor)')
    print('  A - Move Left (Draws a horizontal line to the left of the cursor)')
    print('  S - Move Down (Draws a vertical line above the cursor)')
    print('  D - Move Right (Draws a horizontal line to the right of the cursor)')
    print('---------------------------------------------------------------')
    print('H - Help: Display these instructions')
    print('C - Clear the canvas: Erase all drawings')
    print('E - Export the canvas: Save your masterpiece to a text file')
    print('Q - Quit the program: Exit the Etch-A-Sketch Simulator')
    print('---------------------------------------------------------------')
    print('Example: Drawing a Hilbert Curve Fractal')
    print('  To draw a Hilbert Curve fractal, you can use the following keys:')
    print('  SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW')
    print('  This sequence will create a beautiful Hilbert Curve fractal!')
    input('Press Enter to return to the program...')


def generate_canvas_string(canvas_data, c_x, c_y):
    '''Generates a multiline string of the canvas.'''
    canvas_string = ''

    for row_number in range(CANVAS_HEIGHT):
        for column_number in range(CANVAS_WIDTH):
            if column_number == c_x and row_number == c_y:
                canvas_string += 'X'  # Display cursor position
                continue

            cell = canvas_data.get((column_number, row_number))

            # Add characters based on the lines at each xy point
            if cell in ({'W', 'S'}, {'W'}, {'S'}):
                canvas_string += UP_DOWN_CHAR
            elif cell in ({'A', 'D'}, {'A'}, {'D'}):
                canvas_string += LEFT_RIGHT_CHAR
            elif cell == {'S', 'D'}:
                canvas_string += DOWN_RIGHT_CHAR
            elif cell == {'A', 'S'}:
                canvas_string += DOWN_LEFT_CHAR
            elif cell == {'W', 'D'}:
                canvas_string += UP_RIGHT_CHAR
            elif cell == {'W', 'A'}:
                canvas_string += UP_LEFT_CHAR
            elif cell == {'W', 'S', 'D'}:
                canvas_string += UP_DOWN_RIGHT_CHAR
            elif cell == {'W', 'S', 'A'}:
                canvas_string += UP_DOWN_LEFT_CHAR
            elif cell == {'A', 'S', 'D'}:
                canvas_string += DOWN_LEFT_RIGHT_CHAR
            elif cell == {'W', 'A', 'D'}:
                canvas_string += UP_LEFT_RIGHT_CHAR
            elif cell == {'W', 'A', 'S', 'D'}:
                canvas_string += CROSS_CHAR
            elif cell is None:
                canvas_string += ' '
        canvas_string += '\n'

    return canvas_string


if __name__ == '__main__':
    main()
