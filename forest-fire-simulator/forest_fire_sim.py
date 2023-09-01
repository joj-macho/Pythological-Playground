import random
import time
import bext

# Constants
# Adjust screen size
WIDTH = 80
HEIGHT = 30

TREE = 'A'
FIRE = 'W'
EMPTY = ' '

# Initial parameters
TREE_DENSITY = 0.01  # Density of trees in the forest
GROWTH_CHANCE = 0.05  # Probability of a tree growing in an empty space
FIRE_CHANCE = 0.26  # Probability of a tree catching fire
PAUSE = 0.5  # Time interval between each simulation step

def main():
    '''Main function of the program.'''

    print('\nWelcome to the Forest Fire Simulation.\n')

    # Create an initial forest
    forest = create_forest()
    bext.clear()

    try:
        while True:
            display_forest(forest)
            # Perform a single simulation step
            forest = simulate_fire(forest)
            time.sleep(PAUSE)
    except KeyboardInterrupt:
        print('\n\nSimulation stopped by user.')

def create_forest():
    '''Create a new forest data structure.'''

    forest = {'width': WIDTH, 'height': HEIGHT}
    for i in range(WIDTH):
        for k in range(HEIGHT):
            # Randomly determine if a cell should contain a tree or be empty
            if (random.random() * 100) <= TREE_DENSITY:
                forest[(i, k)] = TREE  # Cell contains a tree
            else:
                forest[(i, k)] = EMPTY  # Cell is empty

    return forest

def display_forest(forest):
    '''Display the forest data structure on the screen.'''

    bext.goto(0, 0)
    for k in range(forest['height']):
        for i in range(forest['width']):
            if forest[(i, k)] == TREE:
                # Display a tree in green
                bext.fg('green')
                print(TREE, end='')
            elif forest[(i, k)] == FIRE:
                # Display fire in red
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(i, k)] == EMPTY:
                # Display empty space
                print(EMPTY, end='')
        print()

    bext.fg('reset')
    # Display growth chance
    print('Grow chance: {}%  '.format(GROWTH_CHANCE * 100), end='')
    # Display fire chance
    print('Fire chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')

def simulate_fire(forest):
    '''Simulate the forest fire.'''

    next_forest = {'width': forest['width'], 'height': forest['height']}

    for i in range(forest['width']):
        for k in range(forest['height']):
            if (i, k) in next_forest:
                continue
            
            if (forest[(i, k)] == EMPTY) and (random.random() <= GROWTH_CHANCE):
                # Empty space can grow a tree
                next_forest[(i, k)] = TREE
            elif (forest[(i, k)] == TREE) and (random.random() <= FIRE_CHANCE):
                # A tree can catch fire
                next_forest[(i, k)] = FIRE
            elif forest[(i, k)] == FIRE:
                # Spread fire to neighboring cells
                for p in range(-1, 2):
                    for q in range(-1, 2):
                        if forest.get((i + p, k + q)) == TREE:
                            next_forest[(i + p, k + q)] = FIRE
                # The tree burns down
                next_forest[(i, k)] = EMPTY
            else:
                # Copy existing state
                next_forest[(i, k)] = forest[(i, k)]

    return next_forest

if __name__ == '__main__':
    main()
