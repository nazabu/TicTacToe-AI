import math
import random
import time

# --- core game logic ---
def create_board():
    return [' ' for _ in range(9)]

def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def print_board_indices():
    idx_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
    for row in idx_board:
        print('| ' + ' | '.join(row) + ' |')

def available_moves(board):
    return [i for i, val in enumerate(board) if val == ' ']

def apply_move(board, square, letter):
    if board[square] == ' ':
        board[square] = letter
        return True
    return False

def check_winner(board, square, letter):
    row = square // 3
    col = square % 3
    if all(board[row * 3 + i] == letter for i in range(3)):
        return True
    if all(board[col + i * 3] == letter for i in range(3)):
        return True
    if square % 2 == 0:
        if all(board[i] == letter for i in [0, 4, 8]) or all(board[i] == letter for i in [2, 4, 6]):
            return True
    return False

def board_full(board):
    return ' ' not in board

# --- unbeatable AI ---
def minimax(board, current_letter, ai_letter):
    human_letter = 'O' if ai_letter == 'X' else 'X'

    if check_win_state(board, human_letter):
        return {'position': None, 'score': -1 * (len(available_moves(board)) + 1)}
    elif check_win_state(board, ai_letter):
        return {'position': None, 'score': 1 * (len(available_moves(board)) + 1)}
    elif board_full(board):
        return {'position': None, 'score': 0}

    if current_letter == ai_letter:
        best = {'position': None, 'score': -math.inf}
    else:
        best = {'position': None, 'score': math.inf}

    for move in available_moves(board):
        board[move] = current_letter
        sim_score = minimax(board, 'O' if current_letter == 'X' else 'X', ai_letter)
        board[move] = ' '
        sim_score['position'] = move

        if current_letter == ai_letter:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score

    return best

def check_win_state(board, letter):
    for i in range(3):
        if all(board[i * 3 + j] == letter for j in range(3)):
            return True
        if all(board[i + j * 3] == letter for j in range(3)):
            return True
    if all(board[i] == letter for i in [0, 4, 8]) or all(board[i] == letter for i in [2, 4, 6]):
        return True
    return False

# --- player control ---
def get_human_move(board):
    while True:
        try:
            move = int(input("Enter your move (0–8): "))
            if move in available_moves(board):
                return move
            else:
                print("Invalid move.")
        except ValueError:
            print("Please enter a number.")

def get_ai_move(board, ai_letter):
    if len(available_moves(board)) == 9:
        return random.choice(available_moves(board))
    else:
        return minimax(board, ai_letter, ai_letter)['position']

# --- main loop ---
def play():
    board = create_board()
    current_letter = 'X'
    ai_letter = 'O'
    human_letter = 'X'

    print_board_indices()
    while not board_full(board):
        if current_letter == human_letter:
            move = get_human_move(board)
        else:
            move = get_ai_move(board, ai_letter)

        if apply_move(board, move, current_letter):
            print(f"{current_letter} moves to {move}")
            print_board(board)
            print()

            if check_winner(board, move, current_letter):
                print(f"{current_letter} wins!")
                return
            current_letter = 'O' if current_letter == 'X' else 'X'

        time.sleep(0.8)

    print("It's a tie!")

if __name__ == '__main__':
    play()
