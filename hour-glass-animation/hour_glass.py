import random
import sys
import time
import bext

# Set up the constants:
PAUSE_LENGTH = 0.2
WIDE_FALL_CHANCE = 50

# Set up the walls of the hourglass:
HOURGLASS = set()  # Has (x, y) tuples for where hourglass walls are.

def initialize_hourglass():
    global HOURGLASS

    for i in range(18, 37):
        HOURGLASS.add((i, 1))  # Add walls for the top cap of the hourglass.
        HOURGLASS.add((i, 23))  # Add walls for the bottom cap.
    for i in range(1, 5):
        HOURGLASS.add((18, i))  # Add walls for the top left straight wall.
        HOURGLASS.add((36, i))  # Add walls for the top right straight wall.
        HOURGLASS.add((18, i + 19))  # Add walls for the bottom left.
        HOURGLASS.add((36, i + 19))  # Add walls for the bottom right.
    for i in range(8):
        HOURGLASS.add((19 + i, 5 + i))  # Add the top left slanted wall.
        HOURGLASS.add((35 - i, 5 + i))  # Add the top right slanted wall.
        HOURGLASS.add((25 - i, 13 + i))  # Add the bottom left slanted wall.
        HOURGLASS.add((29 + i, 13 + i))  # Add the bottom right slanted wall.

# Set up the initial sand at the top of the hourglass:
INITIAL_SAND = set()

def initialize_sand():
    global INITIAL_SAND

    for y in range(8):
        for x in range(19 + y, 36 - y):
            INITIAL_SAND.add((x, y + 4))

# Set up the screen dimensions:
SCREEN_WIDTH = 79
SCREEN_HEIGHT = 25

# Set up the characters for drawing:
X = 0
Y = 1
SAND = chr(9617)
WALL = chr(9608)

def draw_walls():
    for wall in HOURGLASS:
        bext.goto(wall[X], wall[Y])
        print(WALL, end='')

def draw_sand(sand):
    for pos in sand:
        bext.goto(pos[X], pos[Y])
        print(SAND, end='')

def simulate_hourglass():
    allSand = list(INITIAL_SAND)

    while True:  # Main simulation loop.
        random.shuffle(allSand)  # Random order of grain simulation.

        sandMovedOnThisStep = False
        for i, sand in enumerate(allSand):
            if sand[Y] == SCREEN_HEIGHT - 1:
                # Sand is on the very bottom, so it won't move:
                continue

            # If nothing is under this sand, move it down:
            noSandBelow = (sand[X], sand[Y] + 1) not in allSand
            noWallBelow = (sand[X], sand[Y] + 1) not in HOURGLASS
            canFallDown = noSandBelow and noWallBelow

            if canFallDown:
                # Draw the sand in its new position down one space:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')  # Clear the old position.
                bext.goto(sand[X], sand[Y] + 1)
                print(SAND, end='')

                # Set the sand in its new position down one space:
                allSand[i] = (sand[X], sand[Y] + 1)
                sandMovedOnThisStep = True
            else:
                # Check if the sand can fall to the left:
                belowLeft = (sand[X] - 1, sand[Y] + 1)
                noSandBelowLeft = belowLeft not in allSand
                noWallBelowLeft = belowLeft not in HOURGLASS
                left = (sand[X] - 1, sand[Y])
                noWallLeft = left not in HOURGLASS
                notOnLeftEdge = sand[X] > 0
                canFallLeft = (
                    noSandBelowLeft and noWallBelowLeft
                    and noWallLeft and notOnLeftEdge
                )

                # Check if the sand can fall to the right:
                belowRight = (sand[X] + 1, sand[Y] + 1)
                noSandBelowRight = belowRight not in allSand
                noWallBelowRight = belowRight not in HOURGLASS
                right = (sand[X] + 1, sand[Y])
                noWallRight = right not in HOURGLASS
                notOnRightEdge = sand[X] < SCREEN_WIDTH - 1
                canFallRight = (
                    noSandBelowRight and noWallBelowRight
                    and noWallRight and notOnRightEdge
                )

                # Set the falling direction:
                fallingDirection = None
                if canFallLeft and not canFallRight:
                    fallingDirection = -1  # Set the sand to fall left.
                elif not canFallLeft and canFallRight:
                    fallingDirection = 1  # Set the sand to fall right.
                elif canFallLeft and canFallRight:
                    # Both are possible, so randomly set it:
                    fallingDirection = random.choice((-1, 1))

                # Check if the sand can "far" fall two spaces to
                # the left or right instead of just one space:
                if random.random() * 100 <= WIDE_FALL_CHANCE:
                    belowTwoLeft = (sand[X] - 2, sand[Y] + 1)
                    noSandBelowTwoLeft = belowTwoLeft not in allSand
                    noWallBelowTwoLeft = belowTwoLeft not in HOURGLASS
                    notOnSecondToLeftEdge = sand[X] > 1
                    canFallTwoLeft = (
                        canFallLeft and noSandBelowTwoLeft
                        and noWallBelowTwoLeft and notOnSecondToLeftEdge
                    )

                    belowTwoRight = (sand[X] + 2, sand[Y] + 1)
                    noSandBelowTwoRight = belowTwoRight not in allSand
                    noWallBelowTwoRight = belowTwoRight not in HOURGLASS
                    notOnSecondToRightEdge = sand[X] < SCREEN_WIDTH - 2
                    canFallTwoRight = (
                        canFallRight and noSandBelowTwoRight
                        and noWallBelowTwoRight and notOnSecondToRightEdge
                    )

                    if canFallTwoLeft and not canFallTwoRight:
                        fallingDirection = -2
                    elif not canFallTwoLeft and canFallTwoRight:
                        fallingDirection = 2
                    elif canFallTwoLeft and canFallTwoRight:
                        fallingDirection = random.choice((-2, 2))

                if fallingDirection is None:
                    # This sand can't fall, so move on.
                    continue

                # Draw the sand in its new position:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')  # Erase old sand.
                bext.goto(sand[X] + fallingDirection, sand[Y] + 1)
                print(SAND, end='')

                # Set the sand in its new position:
                allSand[i] = (sand[X] + fallingDirection, sand[Y] + 1)
                sandMovedOnThisStep = True

        if not sandMovedOnThisStep:
            # No sand moved on this step, so the hourglass is full.
            return

        # Pause and draw the hourglass:
        time.sleep(PAUSE_LENGTH)
        bext.clear()
        draw_walls()
        draw_sand(allSand)


def main():
    bext.clear()
    initialize_hourglass()
    initialize_sand()
    draw_walls()
    draw_sand(INITIAL_SAND)
    simulate_hourglass()
    bext.goto(0, SCREEN_HEIGHT)
    sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
