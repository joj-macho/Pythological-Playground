import sys

# A tuple of the player's pits:
PLAYER_1_PITS = ('A', 'B', 'C', 'D', 'E', 'F')
PLAYER_2_PITS = ('G', 'H', 'I', 'J', 'K', 'L')

# A dictionary whose keys are pits and values are opposite pit:
OPPOSITE_PIT = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K',
                   'F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D',
                   'K': 'E', 'L': 'F', '1': '2', '2': '1'}

# A dictionary whose keys are pits and values are the next pit in order:
NEXT_PIT = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1',
            '1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G',
            'G': '2', '2': 'A'}

# Every pit label, in counterclockwise order starting with A:
PIT_LABELS = 'ABCDEF1LKJIHG2'

# How many seeds are in each pit at the start of a new game:
STARTING_NUMBER_OF_SEEDS = 4

def main():
    '''Main function to start the Mancala game.'''
    pass


def generate_new_board():
    '''Generate a new Mancala board in the starting state.'''
    pass


def display_board(board):
    '''Display the game board as ASCII-art based on the board dictionary.'''

    pass


def ask_for_player_move(player_turn, board):
    '''Ask the player for their move and return the selected pit.'''
    pass


def make_move(board, player_turn, pit):
    '''Make a move on the board based on the selected pit.'''
    pass


def check_for_winner(board):
    '''Check if there is a winner or a tie on the board.'''
    pass


if __name__ == '__main__':
    main()
