"""
@file :-greatest.py
@brief :- A function that find a greatest from 3 numbers
@auther :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""

# Function Defination
"""
*function : Function that check from the three Number which Number is Gratater
*identifier :greatest()
*paramters : a, b, c
*return  : None
"""
# Define a function to find the greatest number among three inputs
def greatest(a, b, c):
    # Check which number is the greatest using conditional statements
    if a > b and a > c:
        print(f"{a} is the greatest number")
    elif b > a and b > c:
        print(f"{b} is the greatest number")
    else:
        print(f"{c} is the greatest number")

# Calling the function with specific arguments to find the greatest number
greatest(10, 20, 2)

