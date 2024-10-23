# Conway's Game of Life

## Description

This program is an implementation of Conway's Game of Life, a cellular automaton. The Game of Life simulates the evolution of cells on a grid based on a set of simple rules.

## How it Works

- The program initializes a random grid of cells (each of which can be either alive (`'0'`) or dead (`' '`).) and continuously updates and prints the grid.
- The update rules of the grid are based on the number of alive neighbors:
    - Any live cell with fewer than two live neighbors dies (underpopulation).
    - Any live cell with two or three live neighbors lives on to the next generation.
    - Any live cell with more than three live neighbors dies (overpopulation).
    - Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

## Running the Program

```bash
# Navigate to the project directory
cd conway-game-of-life/

# Run the main script
python3 conway_game_of_life.py
```

## Program Input & Output

When you run `conway_game_of_life.py`, the output will look like this;

![Conway Game of Life Output](output/conway-results.gif)