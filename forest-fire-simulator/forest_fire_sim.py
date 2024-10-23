import os
import time
import random
import copy

# Constants
WIDTH = 70
HEIGHT = 30
TREE = 'T'
FIRE = '#'
EMPTY = ' '
DENSITY = 0.2  # Initial tree density
FIRE_SPREAD_PROB = 0.31415  # Probability of fire spreading to adjacent trees
GROWTH_CHANCE = 0.042  # Probability of trees growing in empty spaces
FIRE_CHANCE = 0.01  # Probability of spontaneous fire starting

# ANSI escape codes for colors
TREE_COLOR = '\033[32m'  # Green for trees
FIRE_COLOR = '\033[31m'  # Red for fire
RESET_COLOR = '\033[0m'  # Reset to default color


def main():
    '''Run the forest fire simulation.'''
    grid = initialize_grid(WIDTH, HEIGHT, DENSITY)
    generation = 0

    try:
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f'Forst Fire Simulation - Generation {generation}\n')
            display_grid(grid)
            grid = update_grid(grid)
            print(f'Fire Spread Chance: {FIRE_SPREAD_PROB*100}%', end=' | ')
            print(f'Tree Growth Chance: {GROWTH_CHANCE*100}%', end=' | ')
            print(f'Lightning Chance: {FIRE_CHANCE*100}%')
            generation += 1
            time.sleep(0.5)
    except KeyboardInterrupt:
        print('\nProgram interrupted... Bye!')


def initialize_grid(width, height, density):
    '''Initialize the grid with trees and a random fire.'''
    grid = [[TREE if random.random() < density else EMPTY
             for _ in range(WIDTH)] for _ in range(HEIGHT)]
    # Set a single fire starting point
    fire_x, fire_y = random.randint(
        0, WIDTH - 1), random.randint(0, HEIGHT - 1)
    grid[fire_y][fire_x] = FIRE
    return grid


def display_grid(grid):
    '''Show the grid with colored trees and fire.'''
    for row in grid:
        for cell in row:
            if cell == TREE:
                print(f'{TREE_COLOR}{TREE}{RESET_COLOR}', end='')
            elif cell == FIRE:
                print(f'{FIRE_COLOR}{FIRE}{RESET_COLOR}', end='')
            else:
                print(EMPTY, end='')
        print()
    print()


def get_neighbors(x, y):
    '''Get the coordinates of the neighboring cells.'''
    neighbors = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                neighbors.append((nx, ny))
    return neighbors


def update_grid(grid):
    '''Update the grid based on the fire spreading and tree growth rules.'''
    # new_grid = [row[:] for row in grid]
    new_grid = copy.deepcopy(grid)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x] == FIRE:
                # Turn the burning tree into an empty space
                new_grid[y][x] = EMPTY
                # Spread fire to neighboring trees
                for nx, ny in get_neighbors(x, y):
                    if grid[ny][nx] == TREE and random.random(
                    ) < FIRE_SPREAD_PROB:
                        new_grid[ny][nx] = FIRE
            elif grid[y][x] == TREE:
                # Chance for tree to spontaneously catch fire
                if random.random() < FIRE_CHANCE:
                    new_grid[y][x] = FIRE
            elif grid[y][x] == EMPTY:
                # Chance for a new tree to grow
                if random.random() < GROWTH_CHANCE:
                    new_grid[y][x] = TREE

    return new_grid


if __name__ == '__main__':
    main()
