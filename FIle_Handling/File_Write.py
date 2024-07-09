"""
@file :- File_Write.py
@Brief :- Demonstration of File Handling Write mthod 
@Author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""

#opining the file "demo" in writing mode
f = open("demo.txt","w")

#writing a single line in file
f.write("This File Was Created by using Write method")

#writing   a multiple lines into a file 
f.writelines("\nHello Guyes,\n Welcome to python Programing \n We Writing Script for File Handling")

#checking if file is able to wirte or not if yes then return true
print(f.writable())

#closing the file 
f.close()



