file = open("newfile.txt","r")

print("reading initial contents")
print(file.read())
print("finished")
file.close()


file = open("newfile.txt","w")
file.write("Text has been replaced")
file.close()

file = open("newfile.txt","r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()