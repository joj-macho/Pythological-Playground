import random
import sys


def main():
    '''This is the main function.'''

    print('''\nSliding Tile Puzzle

Use the WASD keys to move the tiles
back into their original order:
        1  2  3  4
        5  6  7  8
        9  10 11 12
        13 14 15 
''')

    input('Press Enter to begin...')

    game_board = generate_new_puzzle()

    while True:
        display_board(game_board)
        player_move = ask_for_player_move(game_board)
        make_move(game_board, player_move)

        if check_win(game_board):
            print('You won!')
            sys.exit()


def generate_new_board():
    '''Return a list of lists that represents a new tile puzzle.'''

    return [['1', '5', '9', '13'], ['2', '6', '10', '14'],
            ['3', '7', '11', '15'], ['4', '8', '12', '']]


def display_board(board):
    '''Display the given board on the screen.'''

    board_to_draw = '''
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
'''.format(*sum(board, []))
    print(board_to_draw)


def find_blank_space(board):
    '''Return an (x, y) tuple of the blank space's location.'''

    for x in range(4):
        for y in range(4):
            if board[x][y] == '':
                return x, y


def ask_for_player_move(board):
    '''Let the player select a tile to slide.'''

    blank_x, blank_y = find_blank_space(board)
    valid_moves = []
    if blank_y != 3:
        valid_moves.append('W')
    if blank_x != 3:
        valid_moves.append('A')
    if blank_y != 0:
        valid_moves.append('S')
    if blank_x != 0:
        valid_moves.append('D')

    while True:
        print(f'                          ({valid_moves[0]})')
        print(f'Enter WASD (or QUIT): ({valid_moves[1]}) ({valid_moves[2]}) ({valid_moves[3]})')

        response = input('> ').upper()
        if response == 'QUIT':
            sys.exit()
        if response in valid_moves:
            return response
        else:
            print('Invalid move. Try again.')


def make_move(board, move):
    '''Carry out the given move on the given board.'''

    blank_x, blank_y = find_blank_space(board)

    if move == 'W':
        board[blank_x][blank_y], board[blank_x][blank_y + 1] = board[blank_x][blank_y + 1], board[blank_x][blank_y]
    elif move == 'A':
        board[blank_x][blank_y], board[blank_x + 1][blank_y] = board[blank_x + 1][blank_y], board[blank_x][blank_y]
    elif move == 'S':
        board[blank_x][blank_y], board[blank_x][blank_y - 1] = board[blank_x][blank_y - 1], board[blank_x][blank_y]
    elif move == 'D':
        board[blank_x][blank_y], board[blank_x - 1][blank_y] = board[blank_x - 1][blank_y], board[blank_x][blank_y]


def make_random_move(board):
    '''Perform a slide in a random direction.'''

    blank_x, blank_y = find_blank_space(board)
    valid_moves = []
    if blank_y != 3:
        valid_moves.append('W')
    if blank_x != 3:
        valid_moves.append('A')
    if blank_y != 0:
        valid_moves.append('S')
    if blank_x != 0:
        valid_moves.append('D')

    make_move(board, random.choice(valid_moves))


def generate_new_puzzle(moves=200):
    '''Get a new puzzle by making random slides from a solved state.'''
    
    board = generate_new_board()

    for _ in range(moves):
        make_random_move(board)
    return board


def check_win(board):
    '''Check if the given board is in the solved state.'''

    solved_board = generate_new_board()
    return board == solved_board


if __name__ == '__main__':
    main()
