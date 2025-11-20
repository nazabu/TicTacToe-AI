import math
from board import check_winner, is_board_full

AI = "X"
HUMAN = "O"

def ai_move(board, ai_symbol, human_symbol):
    """
    Finds and makes the best move for the AI on a 2D board.
    """
    _, best_row, best_col = minimax(board, ai_symbol, human_symbol, is_ai_turn=True)
    board[best_row][best_col] = ai_symbol


def minimax(board, ai_symbol, human_symbol, is_ai_turn):
    winner = check_winner(board)
    if winner == ai_symbol:
        return 10, None, None
    elif winner == human_symbol:
        return -10, None, None
    elif is_board_full(board):
        return 0, None, None

    best_score = -math.inf if is_ai_turn else math.inf
    best_move = (None, None)

    for row in range(3):
        for col in range(3):
            if board[row][col] == "-":
                # Simulate move
                board[row][col] = ai_symbol if is_ai_turn else human_symbol

                score, _, _ = minimax(board, ai_symbol, human_symbol, not is_ai_turn)

                # Undo move
                board[row][col] = "-"

                # Choose best move based on turn
                if is_ai_turn:
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
                else:
                    if score < best_score:
                        best_score = score
                        best_move = (row, col)

    return best_score, best_move[0], best_move[1]
