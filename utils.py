from board import create_board

def initialize_game():
    board = create_board()
    game_mode = input("Who would you like to play against (AI or P): ")
    if game_mode == "AI":
        player_first = input("Does player go first? (Y/N): ")
        if player_first == "Y":
            symbols = {"player": 'x', "ai": 'o'}
            current_turn = "Player"
        else:
            symbols = {"player": 'o', "ai": 'x'}
            current_turn = "AI"
    else:
        symbols = {"Player1": 'x', "Player2": 'o'}
        current_turn = "Player1"

    return board, current_turn, game_mode, symbols

def switch_turn(current_turn, game_mode):
    if game_mode == "AI":
        return 'Player' if current_turn == 'AI' else 'AI'
    else:
        return 'Player2' if current_turn == 'Player1' else "Player1"