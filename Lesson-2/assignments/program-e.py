# Write a program with variables holding the following:
#     your age
#     first letter of your last name
#     current shekels-dollar currency
#     did you fly abroad (true/False)
#     your apartment number
# print all variables
# add the currency to your age and check the result


age = input("What is your age? ")
age_f = float(age)

last_name = input("What's your last name? ")
last_name_first_letter = last_name[:1]

currency = input("Current ILS-USD currency? ")
currency_f = float(currency)


fly = input("Did you fly overseas? (Yes/No) ")


apt_number = input("What's your apartment number?")
apt_number_int = int(apt_number)

if fly.lower() == "yes":
    fly_true_false = "True" 
else:
    fly_true_false = "False"

my_dict = {"age":age, "last name first letter":last_name_first_letter, "The currency is": currency, "Flew overseas?": fly_true_false, "Apartment number": apt_number}

for key, value in my_dict.items():
    print(key + ": " + value)
    
print(f"The sum of age and currency is:  {age_f + currency_f}")