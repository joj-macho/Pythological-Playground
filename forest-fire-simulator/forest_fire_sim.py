import random
import time
import bext

# Constants
WIDTH = 80
HEIGHT = 30

TREE = 'A'
FIRE = 'W'
EMPTY = ' '

TREE_DENSITY = 0.6
GROWTH_CHANCE = 0.05
FIRE_CHANCE = 0.06
PAUSE = 0.5


def main():
    '''This is the main function of the program. It initializes the forest, displays it on the screen, and runs the simulation.'''

    print('\nWelcome to the Forest Fire Simulation.\n')

    # Create Forest
    forest = create_forest()
    bext.clear()

    try:
        while True:
            display_forest(forest)
            # Single simulation step
            next_forest = {'width': forest['width'], 'height': forest['height']}

            for i in range(forest['width']):
                for k in range(forest['height']):
                    if (i, k) in next_forest:
                        # If we've already set next_forest[(i, k)] on a previous iteration, just do nothing here:
                        continue

                    if (forest[(i, k)] == EMPTY) and (random.random() <= GROWTH_CHANCE):
                        # Grow a tree in this empty space.
                        next_forest[(i, k)] = TREE
                    elif (forest[(i, k)] == TREE) and (random.random() <= FIRE_CHANCE):
                        # Lightning sets this tree on fire.
                        next_forest[(i, k)] = FIRE
                    elif forest[(i, k)] == FIRE:
                        # This tree is currently burning.
                        # Loop through all the neighboring spaces:
                        for p in range(-1, 2):
                            for q in range(-1, 2):
                                # Fire spreads to neighboring trees:
                                if forest.get((i + p, k + q)) == TREE:
                                    next_forest[(i + p, k + q)] = FIRE
                        # The tree has burned down now, so erase it:
                        next_forest[(i, k)] = EMPTY
                    else:
                        # Just copy the existing object:
                        next_forest[(i, k)] = forest[(i, k)]
            forest = next_forest

            time.sleep(PAUSE)

    except KeyboardInterrupt:
        print('\n\nSimulation stopped by user.')


def create_forest():
    '''This function creates a new forest data structure with randomly generated trees and empty spaces. Returns a dictionary representing the forest with keys as coordinates and values as the characters representing trees or empty spaces.'''

    forest = {'width': WIDTH, 'height': HEIGHT}
    for i in range(WIDTH):
        for k in range(HEIGHT):
            if (random.random() * 100) <= TREE_DENSITY:
                forest[(i, k)] = TREE  # Start as a tree.
            else:
                forest[(i, k)] = EMPTY  # Start as an empty space.
    return forest


def display_forest(forest):
    '''This function displays the forest data structure on the screen with trees, empty spaces, and fires represented by different characters and colors.'''
    
    bext.goto(0, 0)
    for k in range(forest['height']):
        for i in range(forest['width']):
            if forest[(i, k)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(i, k)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(i, k)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROWTH_CHANCE * 100), end='')
    print('Fire chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


if __name__ == '__main__':
    main()
