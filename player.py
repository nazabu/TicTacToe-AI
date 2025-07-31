def player_move(board, symbol):
    is_valid_input = False
    while not is_valid_input:
        cell = input("Enter row (R) and column (C) index (0-2) together like \"RC\": ")
        row = int(cell[0])
        col = int(cell[1])
        if board[row][col] == "-" and input_checker(cell):
            board[row][col] = symbol
            is_valid_input = True
        else:
            print("Invalid input. Try again.")

def input_checker(input):
    if len(input) != 2:
        return False

    index = ["0","1","2"]
    if input[0] not in index or input[1] not in index:
        return False

    return True