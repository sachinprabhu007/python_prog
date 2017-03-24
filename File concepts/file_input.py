"""file = open("input.txt","r")
for i in range(21):
	print("line no:",i,file.read(4))
file.close()"""

"""file = open("newfile.txt","w")
file.close()"""

msg = "Hello world! hi there"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
file = open("newfile.txt", "r")

print(file.read())
print(amount_written)
file.close()

"""in python 3.x write function has return len(string_written_in_file)
and in python 2.x write doesn't have return."""
