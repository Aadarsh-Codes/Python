"""
@file :- File_Write.py
@Brief :- Demonstration of File Handling mthods 
@Author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""
# opining the file "demo" in reading mode
f = open("demo.txt","r")

#Reading the file
t = f.read()
print(t)

#reading file till specific bites

t1 = f.read(5)
print(t1)

#reading multiple lines on the file 
while True :
	line =f.readlines()
	if not line :
		break
		print(line)


#Cheking the file is readable or not if yes return true
t2 = f.readable()
print(t2 )

# changing our cursor to specified position
Jump_TO = f.seek(10)
print(Jump_TO)

# giving the current position of our cursor
Current_position = f.tell()
print(Current_position)