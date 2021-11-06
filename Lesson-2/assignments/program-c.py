# create a variable and initialize it with a number 1-4
# create 4 conditions (if-elif) which will check the variable
# print the season name accordingly: 1 = summer, 2 = winter, 3 = fall, 4 = spring

var = range(1,5)

for i in var:
    if i == var[0]:
        print(f"{i} - summer")
    elif i == var[1]:
        print(f"{i} = winter")
    elif i == var[2]:
        print(f"{i} = fall")
    elif i == var[3]:
        print(f"{i} = spring")    

