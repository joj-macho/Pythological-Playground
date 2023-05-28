# Forest Fire Simulator

## Description

The Forest Fire Simulation program is a grid-based simulation that models the spread of fire in a forest over time. The program represents the forest as a grid, where each cell can be either a tree, fire, or empty space. The simulation follows a cellular automaton approach, simulating the growth and burning of trees in the forest.

## How it Works

- The program begins by importing the `random`, `time`, and `bext` module.
    - The `random` module is used to generate random numbers. It is used to determine the probabilities of tree growth and fire spread in the simulation.
    - The `time` module is used to introduce delays between simulation steps.
    - The `bext` module provides functionality to control text and colors in the terminal.Here, this module is used to print the forest to the console with colored characters. The color green is used for trees, red for fire, and the default color for empty spaces. 
    

- The program then defines various constants such as the width and height of the forest grid, characters to represent trees and fire, and probabilities for tree growth and fire spread. It also sets the pause duration between simulation steps.

- The `main()` function starts by printing a welcome message and then creates the initial forest grid using `create_forest()`. It then enters an infinite loop where it repeatedly updates the state of the forest according to a set of rules. The rules are as follows:
    - For each empty cell, with a probability GROWTH_CHANCE, a tree is grown.
    - For each tree cell, with a probability FIRE_CHANCE, it catches fire.
    - For each fire cell, it spreads to neighboring trees and burns down the original tree.

- In each iteration of the loop, the program goes through each cell of the forest grid and determines the state of the cell in the next iteration based on the current state and the probabilities for tree growth and fire spread. If a cell is empty and the random chance is met, a tree grows in that cell. If a cell contains a tree and the random chance is met, the tree catches fire. If a cell is on fire, the fire may spread to its neighboring trees. After updating all the cells, the new forest grid becomes the current grid for the next iteration.

- The `create_forest()` function initializes the forest grid by randomly placing trees and empty spaces based on a predefined tree density.

- The `display_forest()` function displays the current state of the forest on the screen, with trees represented by green characters, fire represented by red characters, and empty spaces represented by spaces. It also shows the probabilities for tree growth and lightning-induced fire.

- The simulation continues until it is interrupted by a keyboard interrupt (Ctrl-C), at which point it displays a message indicating that the simulation has been stopped by the user.

## Program Input & Output

When you run the program `forest_fire_sim.py`, the output will look like this;

![Forest Fire Simulation Results](output/forest-fire-results.gif)
