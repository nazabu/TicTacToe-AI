from utils import *
from board import display_board, check_winner, is_board_full
from player import player_move
from ai import ai_move

board, current_turn, game_mode, symbols = initialize_game()

while True:
    break
    display_board(board)

    if game_mode == "AI":
        if current_turn == "Player":
            player_move(board, symbols['player'])
        else:
            ai_move(board, symbols['ai'], symbols['player'])
    else:
        player_move(board, symbols[current_turn])

    winner = check_winner(board)
    if winner is not None:
        display_board(board)
        print(f"{current_turn} won!")
        break

    if is_board_full(board):
        display_board(board)
        print("It's a tie!")
        break

    current_turn = switch_turn(current_turn, game_mode)