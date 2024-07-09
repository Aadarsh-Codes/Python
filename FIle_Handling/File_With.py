"""
@file :- File_Close.py
@Brief :- Demonstration of File Handling how to close file  
@Author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""

# Normally :-
#            variable_Name.colse()


# 'with' keyword


# opening a file demo.txt  

# While opening the file if we not specifing the type of mode of the opening the file ,
#  the file is automatically open in reading mode

with open ("demo.txt") as f :
	data = f.read()
	print(data)


"""

while using 'with' keyword we dont have to close a file manually

"""