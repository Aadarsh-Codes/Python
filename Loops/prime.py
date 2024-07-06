"""
@file :- prime.py
@brief :- This program will find the if the given number is prime or not
@author :- Aadarsh Nanaware (nanawareaadarsh333@gmail.com)
"""


# Loop will start from 1 and end till 30 
for i in range(1,30) :
    #Loop Body
    count = 0    # Initializing a count to store the count of the Number
    for j in range(1,i+1) : # This loop will start from  1 and end till i+1
            #Loop Body
        #  Checking if a i is divisible by j without remainder
        if i%j==0 : 
            count = count + 1 # If condition is true the increment count by 1 
    #writing a condition for prime Numbwer
    if count == 2 : 
        print(f"the prime Number is {i}")
   