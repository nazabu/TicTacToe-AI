from board import check_winner, is_board_full

def ai_move(board, ai_symbol, human_symbol):
    _, row, col = minimax(board, True, ai_symbol, human_symbol)
    board[row][col] = ai_symbol

def minimax(board, is_ai_turn, ai_symbol, human_symbol):
    winner = check_winner(board)
    if winner == ai_symbol:
        return 1, None, None
    elif winner == human_symbol:
        return -1, None, None
    elif is_board_full(board):
        return 0, None, None

    if is_ai_turn:
        best_score = float('-inf')
    else:
        best_score = float('inf')

    best_move = (None, None)

    for row in range(3):
        for col in range(3):
            if board[row][col] == "-":
                board[row][col] = ai_symbol if is_ai_turn else human_symbol

                score, _, _ = minimax(board, not is_ai_turn, ai_symbol, human_symbol)

                board[row][col] = '-'

                if is_ai_turn and score > best_score:
                    best_score = score
                    best_move = (row, col)
                elif not is_ai_turn and score < best_score:
                    best_score = score
                    best_move = (row, col)

    return best_score, best_move[0], best_move[1]