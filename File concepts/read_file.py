with open("newfile.txt") as f:
	print(f.read())

"""
file = open("newfile.txt","r")
print(file.read())
file.close()
"""

"""
An alternative way of doing this is using with statements. 
This creates a temporary variable (often called f),
 which is only accessible in the indented block of the with statement.

 with open("filename.txt") as f:
   print(f.read())


The file is automatically 
closed at the end of the with statement, even if exceptions occur within it."""