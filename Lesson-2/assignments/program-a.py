x = input("Type in your first number: ")
y = input("Type in your second number: ")

if x.isdigit() and y.isdigit():
    x_int = int(x)
    y_int = int(y)
    if x > y:
        print("BIG")
    elif x < y:
        print("small")
else:
    print("You must type in a number. Start again.")
