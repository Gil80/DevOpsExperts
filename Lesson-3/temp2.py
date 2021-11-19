# Example on how to open a file, write to it, append new information and close the file.

file_name = "/home/gil/Projects/DevOpsExperts/Lesson-3/test4.txt"
with open(file_name, "a") as myfile:
    f_name = input("Your first name:")
    l_name = input("Your last name:")
    myfile.writelines(f"{f_name} {l_name}\n")

with open(file_name, "r") as f_read:
 line = f_read.readline()
 while line:
     print(f"Greeting {line}")
     line = f_read.readline()