"""
Board representation and game-state logic for Tic-Tac-Toe.

The board is a flat list of 9 cells (indices 0-8) laid out as:

    0 | 1 | 2
   -----------
    3 | 4 | 5
   -----------
    6 | 7 | 8

Each cell is ' ' (empty), 'X', or 'O'.
"""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]


def create_board():
    return [' '] * 9


def display_board(board):
    for i in range(3):
        row = board[i * 3:(i + 1) * 3]
        print(' ' + ' | '.join(row))
        if i < 2:
            print('-----------')
    print()


def display_positions():
    """Show the index of each cell so the player knows what to type."""
    for i in range(3):
        row = [str(i * 3 + j) for j in range(3)]
        print(' ' + ' | '.join(row))
        if i < 2:
            print('-----------')
    print()


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == ' ']


def make_move(board, position, symbol):
    board[position] = symbol


def undo_move(board, position):
    board[position] = ' '


def check_winner(board):
    """Return 'X', 'O', or None."""
    for a, b, c in WIN_LINES:
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_board_full(board):
    return ' ' not in board


def is_game_over(board):
    return check_winner(board) is not None or is_board_full(board)
