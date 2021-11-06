# write a program with the following:
# 1. method that receives two numbers, add them and return the sum
# 2. method that receives two strings, add space between them, and return one spaced string

def num():
    num1 = int(input("Type number 1: "))
    num2 = int(input("Type number 2: "))
    return num1 + num2
    
num_result = num()
   
print("The sum is: " + str(num_result))




def space_string():
    str1 = input("Type in a word: ")
    str2 = input("Type in another word: ")
    return str1 + " " + str2 

print(space_string())

