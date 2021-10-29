# What will be the values of a, b and c at the end?

a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8

print("The value of `a` is: " + str(a))
print("The value of `b` is: " + str(b))
print("The value of `c` is: " + str(c))

# Answer: Python runs the scrip one line at a time, therefore, it will execute each line at a time.
# This means that the last input variable will take the last value.
# In our example, for the variable `a` the last value to store is 9.
# b will take the last value which is 8.
# c will hole the value of the sum of `a + b` or `9 + 6`. Since there is only one instance of the variable `c` it will output 15. 