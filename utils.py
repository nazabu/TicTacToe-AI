from board import create_board

def initialize_game():
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
        symbols = {"Player1": 'o', "ai": 'x'}
        current_turn = "AI"

