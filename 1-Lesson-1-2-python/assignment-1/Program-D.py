# What is the issue with the code below?

# my_number = 5+5
# print("result is: "+my_number)

### Answer ###
# 1. The variable holds an integer value type.
# 2. The program tries to print in a single line, both a string and an integer. This is not possible.
# 3. We need to perform casting to `my_number` and format it to string in order to print the output.
# 4. Furthermore, the Pyhon convention of spaces is ignored.

### The suggested edit ###

my_number = 5 + 5

print("Result is: " + str(my_number))
