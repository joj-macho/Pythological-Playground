# Constants
ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '

# Dictionary of winning combinations
WINNING_COMBINATIONS = {
    'across_top': ['1', '2', '3'],
    'across_middle': ['4', '5', '6'],
    'across_bottom': ['7', '8', '9'],
    'down_left': ['1', '4', '7'],
    'down_middle': ['2', '5', '8'],
    'down_right': ['3', '6', '9'],
    'diagonal': ['3', '5', '7'],
    'anti_diagonal': ['1', '5', '9']
}

def main():
    '''Play a game of Tic-Tac-Toe.'''

    print('\nWelcome to Tic-Tac-Toe.\n')

    board = generate_new_board()
    current_player = X

    while True:
        print(generate_board_string(board))
        move = None

        # Ask player for a valid move
        while True:
            move = input(f'What is your move {current_player}? > ')

            if not move:
                print('Please enter a valid move.')
                continue

            if not move.isdigit():
                print('Invalid input. Please enter a number.')
                continue

            if not is_valid_space(board, move):
                print('Invalid move. Please select an empty space.')
                continue

            break

        update_board(board, move, current_player)

        if is_winner(board, current_player):
            print(generate_board_string(board))
            print(f'{current_player} won the game.')
            break
        elif is_board_full(board):
            print(generate_board_string(board))
            print('The game is a tie.')
            break

        current_player = switch_player(current_player)

    print('Bye.')

def generate_new_board():
    '''Generate a new blank tic-tac-toe board.'''

    return {space: BLANK for space in ALL_SPACES}

def generate_board_string(board):
    '''Generate a string representation of the board.'''

    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(*board.values())

def is_valid_space(board, space):
    '''Check if a space on the board is valid and blank.'''

    return space in ALL_SPACES and board[space] == BLANK

def is_winner(board, player):
    '''Check if the current player is the winner.'''

    for combination in WINNING_COMBINATIONS.values():
        if all(board[space] == player for space in combination):
            return True
    return False

def is_board_full(board):
    '''Check if the board is full.'''

    return all(board[space] != BLANK for space in ALL_SPACES)

def update_board(board, space, mark):
    '''Update the board by setting a space to the current player's mark.'''

    board[space] = mark

def switch_player(player):
    '''Switch the current player between X and O.'''

    return O if player == X else X



if __name__ == '__main__':
    main()
