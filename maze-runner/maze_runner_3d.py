import copy
import sys
import os


# Constants and Configuration
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617) 
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'


def wall_str_to_wall_dict(wall_string):
    '''Takes a string representation of a wall drawing (like those in ALL_OPEN or CLOSED) and returns a representation in a dictionary with (x, y) tuples as keys and single-character strings of the character to draw at that x, y location.'''
    pass


def display_wall_dict(wall_dict):
    '''Display a wall dictionary, as returned by wall_str_to_wall_dict(), on the screen.'''
    pass


def paste_wall_dict(src_wall_dict, dst_wall_dict, left, top):
    '''Copy the wall representation dictionary in src_wall_dict on top of the one in
    dst_wall_dict, offset to the position given by left, top.'''
    pass


def make_wall_dict(maze, player_X, player_Y, player_direction, exit_X, exit_Y):
    '''From the player's position and direction in the maze (which has an exit at exit_X, exit_Y), create the wall representation dictionary by pasting wall dictionaries on top of ALL_OPEN, then return it.'''

    pass


def load_maze_file(filename):
    '''Load the maze from a file and return the maze dictionary, player's starting position, exit position, and maze dimensions.'''

    pass


def get_user_move():
    '''Get user input for the next move and return the move.'''

    pass


def move_player(move):
    '''Move the player according to the specified move.'''

    pass


def play_game():
    '''Start and play the Maze Runner game.'''

    pass


def main():
    '''Main function of the program.'''

    pass


if __name__ == '__main__':
    main()
