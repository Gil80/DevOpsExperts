from Live import load_game
from GuessGame import play
game_num, difficulty = load_game()

if int(game_num) == 2:
    play(difficulty)