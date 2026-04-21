"""
Unbeatable Tic-Tac-Toe AI using Minimax with Alpha-Beta Pruning.

The algorithm exhaustively evaluates every reachable game state. It assigns
a score to terminal positions (win, loss, draw) adjusted by depth so the AI
prefers the fastest win and the slowest loss. Alpha-beta pruning cuts branches
that cannot influence the final decision, reducing the search space
dramatically while producing the exact same result as plain minimax.

With optimal play from both sides, Tic-Tac-Toe always ends in a draw.
This AI plays optimally, so it guarantees at least a tie — and wins if the
opponent makes a mistake.
"""

import math
from board import available_moves, make_move, undo_move, check_winner, is_board_full

# Scores: positive favours the AI, negative favours the human.
# Adding depth makes the AI prefer faster wins and slower losses.
WIN_SCORE = 100
LOSS_SCORE = -100
DRAW_SCORE = 0


def ai_move(board, ai_symbol):
    """Choose and play the optimal move for the AI."""
    human_symbol = 'O' if ai_symbol == 'X' else 'X'

    moves = available_moves(board)

    # First move: take centre if free, else a corner — no need to search.
    if len(moves) == 9:
        make_move(board, 4, ai_symbol)
        return 4
    if len(moves) == 8 and board[4] == ' ':
        make_move(board, 4, ai_symbol)
        return 4

    best_score = -math.inf
    best_pos = moves[0]

    for pos in moves:
        make_move(board, pos, ai_symbol)
        score = _minimax(board, 0, False, ai_symbol, human_symbol, -math.inf, math.inf)
        undo_move(board, pos)
        if score > best_score:
            best_score = score
            best_pos = pos

    make_move(board, best_pos, ai_symbol)
    return best_pos


def _minimax(board, depth, is_maximising, ai_symbol, human_symbol, alpha, beta):
    """
    Recursively score a board position.

    Parameters
    ----------
    board           : current game state
    depth           : how many moves deep we are (used to adjust scores)
    is_maximising   : True when it is the AI's turn
    ai_symbol       : 'X' or 'O' (whichever the AI plays)
    human_symbol    : the opponent's symbol
    alpha           : best score the maximiser can guarantee so far
    beta            : best score the minimiser can guarantee so far

    Returns
    -------
    int : the minimax value of this position
    """
    winner = check_winner(board)
    if winner == ai_symbol:
        return WIN_SCORE - depth        # prefer faster wins
    if winner == human_symbol:
        return LOSS_SCORE + depth       # prefer slower losses
    if is_board_full(board):
        return DRAW_SCORE

    if is_maximising:
        max_eval = -math.inf
        for pos in available_moves(board):
            make_move(board, pos, ai_symbol)
            eval_score = _minimax(board, depth + 1, False, ai_symbol, human_symbol, alpha, beta)
            undo_move(board, pos)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break                   # beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for pos in available_moves(board):
            make_move(board, pos, human_symbol)
            eval_score = _minimax(board, depth + 1, True, ai_symbol, human_symbol, alpha, beta)
            undo_move(board, pos)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break                   # alpha cutoff
        return min_eval
