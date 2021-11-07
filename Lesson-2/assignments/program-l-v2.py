x = 7 #  x axis

for row in range(0, x):
    for column in range(0, x):
        if ((column == row) or (column == x - 1 - row)):
            print("#", end = "") #  `end` means do not break line, i.e., print in the same line.
        else:
            print(end = " ")
    print()
