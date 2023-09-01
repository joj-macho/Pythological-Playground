import sys

# Game Constants.
EMPTY_SPACE = '.'
PLAYER_X = 'X'
PLAYER_O = 'O'

# Define the dimensions of the game board.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')
assert len(COLUMN_LABELS) == BOARD_WIDTH


def main():
    '''Main function for the Four in a Row game.'''

    print('''
Four in a Row Game.

Two players take turns dropping tiles into one of seven columns, trying to make four in a row horizontally, vertically, or diagonally.
''')

    # Initialize a new game
    game_board = get_new_board()
    player_turn = PLAYER_X

    while True:
        display_board(game_board)
        player_move = ask_for_player_move(player_turn, game_board)
        update_board(player_move, player_turn, game_board)

        # Check for a win or tie:
        if is_winner(player_turn, game_board):
            display_board(game_board)
            print('Player ' + player_turn + ' has won!')
            sys.exit()
        elif is_board_full(game_board):
            display_board(game_board)
            print('There is a tie!')
            sys.exit()

        player_turn = switch_player_turn(player_turn)


def get_new_board():
    '''Create a new game board with empty spaces.'''

    # Initialize the board with empty spaces.
    return [[EMPTY_SPACE] * BOARD_HEIGHT for _ in range(BOARD_WIDTH)]


def display_board(board):
    '''Display the game board and its tiles.'''

    # Print an empty line to separate the board from previous content.
    print()
    # Print the column labels at the top of the board.
    print(' ' + ' '.join(COLUMN_LABELS))
    # Print the top border of the board.
    print('+ ' + '- ' * BOARD_WIDTH + '+')
    # Iterate over each row of the board.
    for row in range(BOARD_HEIGHT):
        print('|', end=' ')
        # Iterate over each column of the board in the current row.
        for col in range(BOARD_WIDTH):
            print(board[col][row], end=' ')
        print('|')
    # Print the bottom border of the board.
    print('+ ' + '- ' * BOARD_WIDTH + '+')


def ask_for_player_move(player_tile, board):
    '''Ask the current player to make a move and return the selected column and row.'''

    while True:
        print('Player {}, enter a column or (q)uit:'.format(player_tile))
        response = input('> ').upper().strip()

        if response.startswith('Q'):
            print('Thanks for playing!')
            sys.exit()

        if response not in COLUMN_LABELS:
            print('Enter a number from 1 to {}.'.format(BOARD_WIDTH))
            continue

        column_index = int(response) - 1 

        if board[column_index][0] != EMPTY_SPACE:
            print('That column is full, select another one.')
            continue

        # Find the first empty space from the bottom in the selected column:
        for row_index in range(BOARD_HEIGHT - 1, -1, -1):
            if board[column_index][row_index] == EMPTY_SPACE:
                return column_index, row_index


def update_board(column, player_tile, board):
    '''Update the game board with the player's move.'''

    # Extract the column and row indices from the provided 'column' tuple.
    col, row = column
    # Set the tile in the specified column and row to the player's tile ('X' or 'O').
    board[col][row] = player_tile


def is_board_full(board):
    '''Check if the game board is full.'''

    for col in board:
        # If any column contains an empty space '.', the board is not full.
        if EMPTY_SPACE in col:
            return False
    # If all columns are full, the board is considered full.
    return True


def is_winner(player_tile, board):
    '''Check if a player has won by forming four consecutive tiles in a row.'''

    # Check for horizontal wins.
    for col in range(BOARD_WIDTH - 3):
        for row in range(BOARD_HEIGHT):
            if board[col][row] == board[col + 1][row] == board[col + 2][row] == board[col + 3][row] == player_tile:
                return True

    # Check for vertical wins.
    for col in range(BOARD_WIDTH):
        for row in range(BOARD_HEIGHT - 3):
            if board[col][row] == board[col][row + 1] == board[col][row + 2] == board[col][row + 3] == player_tile:
                return True

    # Check for diagonal wins.
    for col in range(BOARD_WIDTH - 3):
        for row in range(BOARD_HEIGHT - 3):
            if board[col][row] == board[col + 1][row + 1] == board[col + 2][row + 2] == board[col + 3][row + 3] == player_tile:
                return True

            if board[col + 3][row] == board[col + 2][row + 1] == board[col + 1][row + 2] == board[col][row + 3] == player_tile:
                return True

    # If no winning condition is met, return False.
    return False


def switch_player_turn(player_tile):
    '''Switch the player's turn.'''

    return PLAYER_O if player_tile == PLAYER_X else PLAYER_X


if __name__ == '__main__':
    main()
