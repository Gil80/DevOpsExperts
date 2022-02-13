# Is there a difference between the two lines below? Why?

name1 = "john"
name2 = 'john'
# name3 = 'John's number'
name4 = 'John\'s number'
print("name1: " + name1, "name2: " + name2, "name4 :"+ name4)

### Answer ###
# if holding a single word string, it doesn't make a difference, however, in a multiple word string (name3)
# a single quote means an end of a string and this would produce an error if you don't escape it. See `name4` with escaping.