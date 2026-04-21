"""
Tic-Tac-Toe with an unbeatable AI.

Modes
-----
1. Human vs AI   — play against the minimax bot (you will never win).
2. Human vs Human — two players on the same keyboard.
"""

import time
from board import create_board, display_board, display_positions, check_winner, is_board_full
from player import human_move
from ai import ai_move


def choose_mode():
    while True:
        mode = input("Choose mode — [1] vs AI  [2] vs Human: ").strip()
        if mode in ('1', '2'):
            return int(mode)
        print("Enter 1 or 2.")


def choose_symbol():
    while True:
        choice = input("Do you want to be X or O? (X goes first): ").strip().upper()
        if choice in ('X', 'O'):
            return choice
        print("Enter X or O.")


def play_vs_ai():
    board = create_board()
    human_symbol = choose_symbol()
    ai_symbol = 'O' if human_symbol == 'X' else 'X'
    current = 'X'  # X always goes first

    print("\nBoard positions:")
    display_positions()

    while True:
        if current == human_symbol:
            display_board(board)
            human_move(board, human_symbol)
        else:
            print(f"\nAI ({ai_symbol}) is thinking...")
            time.sleep(0.4)
            pos = ai_move(board, ai_symbol)
            print(f"AI plays position {pos}\n")

        winner = check_winner(board)
        if winner:
            display_board(board)
            if winner == human_symbol:
                print("You win! (this shouldn't happen...)")
            else:
                print("AI wins!")
            return

        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            return

        current = 'O' if current == 'X' else 'X'


def play_vs_human():
    board = create_board()
    current = 'X'

    print("\nBoard positions:")
    display_positions()

    while True:
        display_board(board)
        human_move(board, current)

        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            return

        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            return

        current = 'O' if current == 'X' else 'X'


def main():
    print("=" * 30)
    print("    TIC-TAC-TOE")
    print("=" * 30)

    while True:
        mode = choose_mode()
        print()
        if mode == 1:
            play_vs_ai()
        else:
            play_vs_human()

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break
        print()


if __name__ == '__main__':
    main()
