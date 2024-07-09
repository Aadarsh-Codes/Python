"""
@file :- File_Write.py
@Brief :- Demonstration of File Handling Append mthod 
@Author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""


#opining the file "demo" in append mode
f = open("demo.txt","a")

#aapending a string in file
f.write("\nAdding new Line in the file")

#closing the sile
f.close()