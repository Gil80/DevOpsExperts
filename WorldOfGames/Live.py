### World Of Games ###

def welcome(name):
    name = input("Please type in your name: \n")
    if len(name) < 30:
        return name
    else:
        print("ERROR!!!\nYou have typed more than 30 characters.\nIt's not likely you have such a long name. Please try again.")
        return welcome(name)

name = ""

print("\nHello " + welcome(name) +
      " and welcome to the World Of Games (WoG).\nHere you can find many cool games to play\n")

def load_game():
    print("Please choose a game to play:\n")
    game_num = input("1. Memory game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                     "2. Guess Game - guess a number and see if you choose like the computer\n"
                     "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")    
    if game_num.isdigit() and int(game_num) > 0 and int(game_num) <=3:
        while True:
            difficulty = input("Please choose game difficulty from 1 to 5:\n")
            if difficulty.isdigit() and int(difficulty) > 0 and int(difficulty) <= 5:
                return game_num, difficulty
            else:
                print("\nERROR! You have entered an invalid `difficulty` value. Please try again")           
    else:
        print("\nERROR! You have entered an invalid `game` selection. Please try again")
        return load_game()
        

# len(game_num) == 1 and int(game_num) <= 3 and int(game_num) != 0 and game_num.isdigit() and game_num == game_num.isnumeric()


game_num, difficulty = load_game()

      
#  print game selection
if int(game_num) == 1:
    print("Your game selection is: Memory Game")
elif int(game_num) == 2:
    print("Your game selection is: Guess Game")
else:
    print("Your game selection is: Currency Roulette")

#  print difficulty selection
for i in difficulty:
    print("Your difficulty level is: " + i)