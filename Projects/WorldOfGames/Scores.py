from Live import load_game
import io


difficulty = load_game()[1]

# The function will try to read the current score in scores.txt file.
# if it fails, it will create a new file and use it to save the current score.
def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    # read the score in scores.txt
    # sum up the values
    # if it fails to read the scores.txt, create a new one.