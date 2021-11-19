try:
   myfile = open("/tmp/read_my_content.txt", 'w+')
   extracontents = myfile.write("\nsome more text\n")
except BaseException as e:
   print("Oops something when wrong.\nError is: " + str(e.args[0]))
finally:
   print("Closing file descriptor")
   myfile.close()


