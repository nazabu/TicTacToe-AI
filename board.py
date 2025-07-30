def create_board():
    board = [["-"]*3]*3
    return board

def display_board(board):
    for row in board:
        print(f"{row[0]} | {row[1]} | {row[2]}")

def check_winner(board):
    has_won = check_rows(board)
    if has_won:
        return winner_symbol

    has_won = check_columns(board)
    if has_won:
        return winner_symbol

    has_won = check_diagonal(board)
    if has_won:
        return winner_symbol

    return None

winner_symbol = ""

def check_rows(board):
    for row in board:
        string_row = row[0] + row[1] + row[2]
        if string_row == "xxx" or "ooo":
            global winner_symbol
            winner_symbol += string_row[0]
            return True

    return False

def check_columns(board):
    for i in range(3):
        string_column = ""
        for j in range(3):
            string_column += board[j][i]

        if string_column == "xxx" or "ooo":
            global winner_symbol
            winner_symbol += string_column[0]
            return True

    return False

def check_diagonal(board):
    string_arr_diagonal = [board[0][0] + board[1][1] + board[2][2], board[0][2] + board[1][1] + board[2][0]]
    for string_diagonal in string_arr_diagonal:
        if string_diagonal == "xxx" or "ooo":
            global winner_symbol
            winner_symbol += string_diagonal[0]
            return True

    return False


def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                return False

    return True

