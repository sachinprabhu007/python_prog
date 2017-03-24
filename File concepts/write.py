file = open("file_write.txt","w")
file.write("this has been written to a file ")
file.close()

file = open("file_write.txt","r")
print(file.read())
file.close()