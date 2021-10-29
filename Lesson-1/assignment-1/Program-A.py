# Create a variable name first with value 7.
# Create a variable name second with value 44.3.
# Print result of adding first to second.
# Print result of multiplying first by second
# Print result of dividing second by first

import math

first = 7
second = 44.3

print("The sum of `first` and `second` is: " + str(first + second))

print("The multiplication of `first` and `second` is: " +
      str((round(float(first * second), 2))))
# I'm using the `round` function so the result value would be rounded off with 2 digits after the decimal.
# I'm using the 'float' because I'm telling Python to round a 'float' type.

print("The division of `first` and `second` is: " +
      str((round(float(first / second), 3))))
