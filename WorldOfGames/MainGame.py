from Live import load_game
from GuessGame import play as gg
from MemoryGame import play as mg
game_num, difficulty = load_game()

if game_num == 1:
    mg(difficulty)
elif game_num == 2:
    gg(difficulty)

