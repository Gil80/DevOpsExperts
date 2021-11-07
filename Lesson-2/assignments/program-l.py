# READ ME!! # This was a very challenging exercise. It took me two days to figure out a better way to write the code.
# Please see program-l-v2.py
# This file is my 1st attempt.


# create a nested for loop to create X shape (width is 7, length is 7)

char = "#"
inside = 5 #  pulling the print to the left
outside = 0 #  pushing the print to the right
space = ' '


for i in range(0, 3): #  top half of the darwing
    print(outside*space + char + inside*space + char)
    inside -= 2
    outside +=1
    if inside < 0:
        inside = -1 #  reset the inside grid
        for c in range(0, 1):
            print(outside*space + char + inside*space)
            for ii in range(0, 3): #  ouside = 3, inside = 0 # bottom half of the drawing
                outside -= 1
                inside += 2
                print(outside*space + char + inside*space + char)