from forex_python.converter import CurrencyRates
from random import randint


# online currency conversion and interval calculation
def get_money_interval(random_number, difficulty):
    c = CurrencyRates()
    currency = c.get_rate('ILS', 'USD')  # convert USD to ILS is not working. I'm forced to convert ILS to USD.
    currency = round(1 / currency, 2)  # reversing the conversion to show from USD to ILS.
    print(f"Currency = {currency}")
    total = int(random_number * currency)  # casting to integer for simplicity
    interval = total - (5 - difficulty), total + (5 - difficulty)
    return interval


# generate a random number from 1 to 100 inclusive
def generate_number():
    random_number = randint(1, 100)
    return random_number


# prompts the user to guess a number
def get_guess_from_user():
    try:
        user_guess = int(input("Guess a number between 1 to 350:\n"))
        if user_guess <= 0 or user_guess > 350:
            print("Number is out of range. Try again.")
            return get_guess_from_user()
        else:
            return user_guess
    except ValueError:
        print("You didn't type a valid number. Try again.")
        return get_guess_from_user()


def play(difficulty):
    random_number = generate_number()
    interval = get_money_interval(random_number, difficulty)
    user_guess = get_guess_from_user()
    min_range = interval[0]
    max_range = interval[1]
    if min_range <= user_guess <= max_range:
        print("You WIN!")
    else:
        print("You LOOSE!")
    print(f"The computer generated interval = {interval}")


