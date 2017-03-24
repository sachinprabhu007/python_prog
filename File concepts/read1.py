file = open("input.txt","r")

#to print in one line 
print(len(open("input.txt").readlines()))
print(file.readlines())

"""#to print in multiple lines
for line in file:
	print(line)
"""

file.close()



