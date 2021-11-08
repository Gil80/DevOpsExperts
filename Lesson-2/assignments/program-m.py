# Write a program with the following:
# 1. method that gets a number from a user (using input)
# 2. method that receives the number from the first method, and computes the sum of the digits the integer (e.g. 25 = 7, 2+5 = 7)

def user_input():
    num = input("Please type double digitis number: ")
    if len(num) == 2 and num.isdigit():
        return num
    else:
        return user_input()


def compute_sum(num):
    sum =0 
    for i in range(len(num)):
        sum += int(num[i])
    return(sum)

num = user_input() #  initializing the variable and calling the function
print(compute_sum(num))

