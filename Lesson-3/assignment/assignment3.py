# 1 - Write the following code: a = 1/0;
# 2 - build try/except block to avoid exception

try:
    a = 1/0

except ZeroDivisionError:
    print("Error! Division by zero")

# 3 - is the following code legal?
# Answer - Yes it's legal. It will simply print `finally` and assign the argument 1 to x.
try:
    x = 1
finally:
    print("finally")
    
# 4 - What exception types can be caught by the following handler: exception:
# it will catch standard exceptions:	
Exception
StopIteration
SystemExit
StandardError
ArithmeticError
OverflowError
FloatingPointError
ZeroDivisionError
AssertionError
AttributeError
EOFError
ImportError
KeyboardInterrupt
LookupError
IndexError
KeyError
NameError
UnboundLocalError
EnvironmentError
IOError
OSError
SyntaxError
IndentationError
SystemError
SystemExit
TypeError
ValueError
RuntimeError
NotImplementedError

# 6 - What exceptions can be caught by the following handlers?
except IOError
# When working with Input and Output Operations in Python, if we encounter an error related to file,
# the code will throw the IOError. When we attempt to open a file and if it does not exist, the IOError will be encountered

excpt ZeroDivisionError
# When zero shows up in the denominator of a division operation, a ZeroDivisionError is raised.

