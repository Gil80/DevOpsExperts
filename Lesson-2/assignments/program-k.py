# create a nested for loop to create a pyramid shape:
#
##
###
####
#####

x = "#"
y = 5

for i in range(0, y+1):
    text = ""
    for c in range(0, i):
        text += x
    print(text)
                    
