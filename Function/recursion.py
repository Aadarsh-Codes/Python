"""
@file :- recursion.py
@breif :- Demonstration of Recursion on python
@author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""

# Function Defination
"""
*function : Function to calculate factorial 
*identifier : facto()
*parameter : number 
*return : retruning a factorial number 
"""

def facto(number) :
    # it is our base condition which dosen't call by the function (base case )
    if number==1 or number==0 :
        return 1
    
    else :
        # Recursion Calling
        return number*facto(number-1) 
    
n = int(input("Enter Number :- "))

# calling the function and storing in the f 
f = facto(number=n)
print(f"the factorial number of {n} is {f}")