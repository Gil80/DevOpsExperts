# create a nested for loop to create X shape (width is 7, length is 7)

char = "#"
inside = 5 #  pulling the print to the left
outside = 0 #  pushing the print to the right
top = 3 #  top half of the darwing
bottom = 3 #  bottom half of the drawing
space = ' '


for i in range(0, top):
    print(outside*space + char + inside*space + char)
    inside -= 2
    outside +=1
    if inside < 0:
        inside = -1 #  reset the inside grid
        for c in range(0, 1):
            print(outside*space + char + inside*space)
            for ii in range(0, bottom): #  ouside = 3, inside = 0
                outside -= 1
                inside += 2
                print(outside*space + char + inside*space + char)