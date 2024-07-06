"""
@File   :- For_Loop.py
@brief  :- Demonstartioon of For Loops
@Author :- Aadarsh Nanaware(nanawareaadarsh333@gmal.com)

"""

# Define a string variable
name = "aadarsh"

# Loop through each character in the string 'name'
for i in name:
    # Print each character followed by a comma, without moving to the next line
    print(i, end=",")
print("\n")  # Print a newline character to move to the next line after the loop ends

# Loop through a range of numbers from 1 to 20 
for i in range(1, 21):
    # Print each number on a new line
    print(i, end="\n")
print("\n")  # Print a newline character to move to the next line after the loop ends

# Loop through a range of even numbers from 2 to 20
for a in range(2, 21, 2):
    # Print each even number (variable 'a') on a new line
    print(a)
