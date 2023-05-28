import sys

# Game Constants.
EMPTY_SPACE = '.'
PLAYER_X = 'X'
PLAYER_O = 'O'

# Update displayBoard() & COLUMN_LABELS if BOARD_WIDTH is changed.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')
assert len(COLUMN_LABELS) == BOARD_WIDTH


def main():
    '''This is the main function that runs the Four in a Row game.'''

    print('''\nFour in a Row,

Two players take turns dropping tiles into one of seven columns, trying to make four in a row horizontally, vertically, or diagonally.
''')

    # Set up a new game:
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
        elif is_full(game_board):
            display_board(game_board)
            print('There is a tie!')
            sys.exit()

        player_turn = switch_player_turn(player_turn)


def get_new_board():
    '''This function creates a new game board by returning a nested list that represents a Four in a Row board.'''

    return [[EMPTY_SPACE] * BOARD_HEIGHT for _ in range(BOARD_WIDTH)]


def display_board(board):
    '''This function displays the board and its tiles on the screen.'''

    print()
    print(' ' + ' '.join(COLUMN_LABELS))
    print('+ ' + '- ' * BOARD_WIDTH + '+')
    for row in range(BOARD_HEIGHT):
        print('|', end=' ')
        for col in range(BOARD_WIDTH):
            print(board[col][row], end=' ')
        print('|')
    print('+ ' + '- ' * BOARD_WIDTH + '+')


def ask_for_player_move(player_tile, board):
    '''This function asks the current player to make a move.'''

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

        # Starting from the bottom, find the first empty space.
        for row_index in range(BOARD_HEIGHT - 1, -1, -1):
            if board[column_index][row_index] == EMPTY_SPACE:
                return column_index, row_index


def update_board(column, player_tile, board):
    '''This function updates the game board with the player's move.'''

    col, row = column
    board[col][row] = player_tile


def is_full(board):
    '''This function returns True if the `board` has no empty spaces, otherwise
    returns False.'''

    for col in board:
        if EMPTY_SPACE in col:
            return False
    return True


def is_winner(player_tile, board):
    '''This function returns True if `player_tile` has four tiles in a row on `board`,
    otherwise returns False.'''

    for col in range(BOARD_WIDTH - 3):
        for row in range(BOARD_HEIGHT):
            if board[col][row] == board[col + 1][row] == board[col + 2][row] == board[col + 3][row] == player_tile:
                return True

    for col in range(BOARD_WIDTH):
        for row in range(BOARD_HEIGHT - 3):
            if board[col][row] == board[col][row + 1] == board[col][row + 2] == board[col][row + 3] == player_tile:
                return True

    for col in range(BOARD_WIDTH - 3):
        for row in range(BOARD_HEIGHT - 3):
            if board[col][row] == board[col + 1][row + 1] == board[col + 2][row + 2] == board[col + 3][row + 3] == player_tile:
                return True

            if board[col + 3][row] == board[col + 2][row + 1] == board[col + 1][row + 2] == board[col][row + 3] == player_tile:
                return True

    return False


def switch_player_turn(player_tile):
    '''This function switches the player's turn.'''

    return PLAYER_O if player_tile == PLAYER_X else PLAYER_X


if __name__ == '__main__':
    main()
