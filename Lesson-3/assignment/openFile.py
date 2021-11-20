# create a text file 'words.txt"
# write your name into the file
# read your file content and print it
# write hebrew content into your text file and print its contents

with open('words.txt', 'a', encoding = 'utf-8' ) as w_file: #  utf-8 encoding allows for hebrew writing
    f_name = input("Your first name: ")
    l_name = input("Your last name: ")
    w_file.write(f"{f_name} {l_name}\n" )
    
with open('words.txt', 'r', encoding = 'utf-8') as r_file:
    line = r_file.read()
    # reads the lines and print them
    while line:
        print(line)
        line = r_file.read()
        
    
