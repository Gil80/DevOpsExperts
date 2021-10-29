x = input("Please enter your age: ")
newAge = int(x) + 5
#print(f"In five years your age will be: {newAge}")
# the 'f' is for Formatting the output of 'newAge' as string

print("In five years your age will be: %s" % (newAge))
# the '%s' is looking for the 1st instance of % and
