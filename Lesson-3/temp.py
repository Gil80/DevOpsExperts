try:
   myfile = open("/tmp/read_my_content.txt", 'w+')
   extracontents = myfile.write("\nsome more text\n")
except BaseException as e:
   print("Oops something when wrong.\nError is: " + str(e.args[0]))
finally:
   print("Closing file descriptor")
   myfile.close()

with open(file_name, "r") as f_read:
 line = f_read.readline()
 while line:
     print(f"Greeting {line}")
     line = f_read.readline()
