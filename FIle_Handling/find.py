"""
@file :- find.py
@brief :- writing a program that check if the twinkle word is present in file or not
@author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""

# Opening the file poem.txt  in reading mode 
with open("poem.txt","r") as f :
    
    # reading the data from the file using  readline() method
    data = f.readline()
    
    #Condition that check that if word is in file or not 
    if "twinkle" in data :
        print("The Word twinkle is present in file")  # if true then print this
    else :
        print("The Word twinkle is not present in file") # else print this