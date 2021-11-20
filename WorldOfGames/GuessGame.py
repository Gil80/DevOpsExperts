# start a new game
# cast a new number from 1 to a var called difficulty
# properties: 1 - difficulty. 2 - secret number

from random import randint


def generate_number(difficulty_input):  # needs to input difficulty
    secret_number = randint(1, difficulty_input)
    return secret_number


def get_guess_from_user():
    user_guess = int(input("Guess a number: "))
    return user_guess


def compare_results(secret_number, user_guess):
    return secret_number == user_guess  # will return True or False


def play(difficulty_input):
    secret_number = generate_number(difficulty_input)
    user_guess = get_guess_from_user()
    print(f"secret number = {secret_number}")  # comment in to test the code
    print(f"Your guess = {user_guess}")
    result = compare_results(secret_number, user_guess)
    print(f"The comparison is: {result}")
    return result
