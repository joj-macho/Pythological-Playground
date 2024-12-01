import random

POSITION_GUIDES = ['1 2 3', '4 5 6', '7 8 9']


def main():
    print('Tic Tac Toe Game.')

    scores = {'X': 0, 'O': 0}
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        print_board(board)

        players = ['X', 'O']
        current_player = random.choice(players)
        print(f'Player {current_player} will start.')

        game_over = False
        while not game_over:
            print(f'Player {current_player}\'s turn.')

            move = get_player_move(board)
            print(move)
            row, col = move

            board[row][col] = current_player  # Update board
            print_board(board)

            if check_winner(board, current_player):
                print(f'Player {current_player} wins!')
                scores[current_player] += 1
                game_over = True
            elif all(cell != ' ' for row in board for cell in row):
                print('The game is a draw!')
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'

        print(f'Scores: Player X: {scores.get("X")} | '
              f'Player O: {scores.get("O")}')

        if not play_again():
            print('Bye!')
            break


def print_board(board):
    print('\nCurrent board:')
    for i, row in enumerate(board):
        print(f' {row[0]} | {row[1]} | {row[2]}    {POSITION_GUIDES[i]}')
        if i < len(board) - 1:
            print('---+---+---')
    print()


def get_player_move(board):
    while True:
        try:
            move = int(input('Enter your move (1-9): '))
            if move < 1 or move > 9:
                print(
                    'Invalid move. Enter a number between 1 and 9.')
                continue

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] != ' ':
                print('Invalid move. The position is already taken.')
            else:
                return row, col
        except ValueError:
            print('Invalid input. Enter a number between 1 and 9.')


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def play_again():
    while True:
        response = input(
            'Do you want to play again? (yes or no): ').strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print('Invalid response. Enter (y)es or (n)o.')


if __name__ == '__main__':
    main()
