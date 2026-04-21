"""Human player input handling."""

from board import available_moves, make_move


def human_move(board, symbol):
    """Prompt the human for a valid move and apply it."""
    valid = available_moves(board)
    while True:
        try:
            choice = int(input(f"Player {symbol}, enter your move (0-8): "))
        except ValueError:
            print("Please enter a number between 0 and 8.")
            continue
        if choice not in valid:
            print("That cell is taken or out of range. Try again.")
            continue
        make_move(board, choice, symbol)
        return choice
