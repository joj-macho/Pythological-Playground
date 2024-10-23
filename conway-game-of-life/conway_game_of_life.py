import os
import time
import random

# Constants
WIDTH = 35
HEIGHT = 20
DENSITY = 0.5  # Init cell density


def main():
    '''Run Conway's Game of Life.'''
    # Create init grid
    grid = initialize_grid(WIDTH, HEIGHT, DENSITY)

    # Dispaly and update the grid state
    try:
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')  # Clear screen
            print('Conway\'s Game of Life.\n')
            display_grid(grid)
            grid = update_grid(grid)  # Updaed grid
            time.sleep(0.5)
    except KeyboardInterrupt:
        print('\nSimulation interrupted... Bye!')


def initialize_grid(width, height, density):
    '''Initialize grid with dead or alive cells.'''
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            if random.random() < density:
                row.append('0')  # Alive cell
            else:
                row.append(' ')  # Dead cell
        grid.append(row)
    return grid


def display_grid(grid):
    '''Shows the grid.'''
    for row in grid:
        print(' '.join(row))


def update_grid(grid):
    '''Updates the grid for next generation.'''
    new_grid = []
    for i in range(len(grid)):
        new_row = []
        for j in range(len(grid[i])):
            alive_neighbors = count_alive_neighbors(grid, i, j)
            # Live cell with < 2 neighbors dies,
            # Live cell with 2 or 3 neibors lives
            # Live cell with > 3 live neighbors dies
            # Dead cells with 3 live neighbors becomes new live cell
            if grid[i][j] == '0':
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_row.append(' ')
                else:
                    new_row.append('0')
            else:
                if alive_neighbors == 3:
                    new_row.append('0')
                else:
                    new_row.append(' ')
        new_grid.append(new_row)
    return new_grid


def count_alive_neighbors(grid, x, y):
    '''Counts the number of alive cells for acell.'''
    count = 0

    # Check all possible neighbors of a cell
    # all cells from (x-1, y-1) to (x+1, y+1)
    for i in range(max(0, x - 1), min(x + 2, len(grid))):
        for j in range(max(0, y - 1), min(y + 2, len(grid[0]))):
            # skip cell itself and count only alive neighbors
            if (i != x or j != y) and grid[i][j] == '0':
                count += 1
    return count


if __name__ == '__main__':
    main()
