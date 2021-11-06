# write a program with the following:
# 1. method that receives your name and prints it
# 2. method that receives a number, divide it by 2, and prints the result

def name():
    name = input("What's your name? ")
    print(name)
    
name()

def math():
    x = float(input("Type in a number: "))
    x /= 2
    print(f"The number divided by 2 is: {x}")
    
math()