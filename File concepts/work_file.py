try:
	f = open("newfile1.txt")
	print(f.read())
	print(1/0)
except ZeroDivisionError:
	print("zero div error")
finally:
	f.close()

