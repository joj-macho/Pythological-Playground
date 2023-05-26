import shutil
import sys


# Set up the constants for line characters:
UP_DOWN_CHAR = chr(9474)  # Character 9474 is '│'
LEFT_RIGHT_CHAR = chr(9472)  # Character 9472 is '─'
DOWN_RIGHT_CHAR = chr(9484)  # Character 9484 is '┌'
DOWN_LEFT_CHAR = chr(9488)  # Character 9488 is '┐'
UP_RIGHT_CHAR = chr(9492)  # Character 9492 is '└'
UP_LEFT_CHAR = chr(9496)  # Character 9496 is '┘'
UP_DOWN_RIGHT_CHAR = chr(9500)  # Character 9500 is '├'
UP_DOWN_LEFT_CHAR = chr(9508)  # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR = chr(9524)  # Character 9524 is '┴'
CROSS_CHAR = chr(9532)  # Character 9532 is '┼'

# Get the size of the terminal window:
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH -= 1
CANVAS_HEIGHT -= 5

"""The keys for canvas will be (x, y) integer tuples for the coordinate,
and the value is a set of letters W, A, S, D that tell what kind of line
should be drawn."""
canvas = {}
cursor_x = 0
cursor_y = 0


def main():
    # canvas = {}
    cursor_x = 0
    cursor_y = 0
    moves = []
    while True:  # Main program loop.
        # Draw the lines based on the data in canvas:
        print(generate_canvas_string(canvas, cursor_x, cursor_y))

        print(
            "WASD keys to move, H for help, C to clear, "
            + "F to save, L to load, or QUIT."
        )
        response = input("> ").upper()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()  # Quit the program.
        elif response == "H":
            print_help()
            continue
        elif response == "C":
            clear_canvas()
            moves.append("C")  # Record this move.
        elif response == "F":
            print("Enter filename to save to:")
            filename = input("> ")

            # Make sure the filename ends with .txt:
            if not filename.endswith(".txt"):
                filename += ".txt"
            save_canvas(filename)
        elif response == "L":
            print("Enter filename to load:")
            filename = input("> ")
            load_canvas(filename)
        else:
            for command in response:
                if command not in ("W", "A", "S", "D"):
                    continue  # Ignore this letter and continue to the next one.
                moves.append(command)  # Record this move.

                # The first line we add needs to form a full line:
                if canvas == {}:
                    if command in ("W", "S"):
                        # Make the first line a horizontal one:
                        canvas[(cursor_x, cursor_y)] = {"W", "S"}
                    elif command in ("A", "D"):
                        # Make the first line a vertical one:
                        canvas[(cursor_x, cursor_y)] = {"A", "D"}

                # Update x and y:
                if command == "W" and cursor_y > 0:
                    canvas[(cursor_x, cursor_y)].add(command)
                    cursor_y = cursor_y - 1
                elif command == "S" and cursor_y < CANVAS_HEIGHT - 1:
                    canvas[(cursor_x, cursor_y)].add(command)
                    cursor_y = cursor_y + 1
                elif command == "A" and cursor_x > 0:
                    canvas[(cursor_x, cursor_y)].add(command)
                    cursor_x = cursor_x - 1
                elif command == "D" and cursor_x < CANVAS_WIDTH - 1:
                    canvas[(cursor_x, cursor_y)].add(command)
                    cursor_x = cursor_x + 1
                else:
                    # If the cursor doesn't move because it would have moved off
                    # the edge of the canvas, then don't change the set at
                    # canvas[(cursor_x, cursor_y)].
                    continue

                # If there's no set for (cursor_x, cursor_y), add an empty set:
                if (cursor_x, cursor_y) not in canvas:
                    canvas[(cursor_x, cursor_y)] = set()

                # Add the direction string to this xy point's set:
                if command == "W":
                    canvas[(cursor_x, cursor_y)].add("S")
                elif command == "S":
                    canvas[(cursor_x, cursor_y)].add("W")
                elif command == "A":
                    canvas[(cursor_x, cursor_y)].add("D")
                elif command == "D":
                    canvas[(cursor_x, cursor_y)].add("A")



def generate_canvas_string(canvas_data, c_x, c_y):
    """Returns a multiline string of the line drawn in canvas_data."""
    canvas_string = ''

    """canvas_data is a dictionary with (x, y) tuple keys and values that
    are sets of 'W', 'A', 'S', and/or 'D' strings to show which
    directions the lines are drawn at each xy point."""
    for row_number in range(CANVAS_HEIGHT):
        for column_number in range(CANVAS_WIDTH):
            if column_number == c_x and row_number == c_y:
                canvas_string += '#'
                continue

            # Add the line character for this point to canvas_string.
            cell = canvas_data.get((column_number, row_number))
            if cell in ({"W", "S"}, {"W"}, {"S"}):
                canvas_string += UP_DOWN_CHAR
            elif cell in ({"A", "D"}, {"A"}, {"D"}):
                canvas_string += LEFT_RIGHT_CHAR
            elif cell == {"S", "D"}:
                canvas_string += DOWN_RIGHT_CHAR
            elif cell == {"A", "S"}:
                canvas_string += DOWN_LEFT_CHAR
            elif cell == {"W", "D"}:
                canvas_string += UP_RIGHT_CHAR
            elif cell == {"W", "A"}:
                canvas_string += UP_LEFT_CHAR
            elif cell == {"W", "S", "D"}:
                canvas_string += UP_DOWN_RIGHT_CHAR
            elif cell == {"W", "S", "A"}:
                canvas_string += UP_DOWN_LEFT_CHAR
            elif cell == {"A", "S", "D"}:
                canvas_string += DOWN_LEFT_RIGHT_CHAR
            elif cell == {"W", "A", "D"}:
                canvas_string += UP_LEFT_RIGHT_CHAR
            elif cell == {"W", "A", "S", "D"}:
                canvas_string += CROSS_CHAR
            elif cell is None:
                canvas_string += " "
        canvas_string += "\n"  # Add a newline at the end of each row.
    return canvas_string


def clear_canvas():
    """Clears the canvas data."""
    global canvas
    canvas = {}


def save_canvas(filename):
    """Saves the canvas data to a text file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("".join(moves) + "\n")
            file.write(generate_canvas_string(canvas, None, None))
        print("Canvas saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the canvas: {e}")


def load_canvas(filename):
    """Loads the canvas data from a text file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            moves.extend(list(lines[0].strip()))
            canvas_str = "".join(lines[1:])
            load_canvas_data(canvas_str)
        print("Canvas loaded successfully.")
    except Exception as e:
        print(f"An error occurred while loading the canvas: {e}")


def load_canvas_data(canvas_str):
    """Loads the canvas data from a string."""
    global canvas
    clear_canvas()
    for y, line in enumerate(canvas_str.splitlines()):
        for x, char in enumerate(line):
            if char != " ":
                if x == cursor_x and y == cursor_y:
                    # Update the cursor position if it's in the canvas data.
                    canvas[(x, y)] = set()
                else:
                    canvas[(x, y)] = {char}


def print_help():
    """Prints the help information."""
    print("Enter W, A, S, and D characters to move the cursor and")
    print("draw a line behind it as it moves. For example, 'ddd'")
    print("draws a line going right, and 'sssdddwwwaaa' draws a box.")
    print()
    print("Commands:")
    print("WASD - Move the cursor and draw lines")
    print("H - Help")
    print("C - Clear the canvas")
    print("F - Save the canvas")
    print("L - Load a saved canvas")
    print("QUIT - Quit the program")
    input("Press Enter to return to the program...")




if __name__ == "__main__":
    main()
