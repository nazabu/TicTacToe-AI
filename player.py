def player_move(board, symbol):
    is_valid_input = False
    while not is_valid_input:
        cell = input("Enter row (R) and column (C) index (0-2) together like \"RC\": ")
        if input_checker(cell):
            if board[int(cell[0])][int(cell[1])] == "-":
                board[int(cell[0])][int(cell[1])] = symbol
                is_valid_input = True
            else:
                print("Invalid input. Try again.")
        else:
            print("Invalid input. Try again.")

def input_checker(input):
    if len(input) != 2:
        return False

    index = ["0","1","2"]
    if input[0] not in index or input[1] not in index:
        return False

    return True