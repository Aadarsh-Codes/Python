"""
@file :- factorial.py
@brief :- This program will print the factorial of a number Enterd by user 
@auther :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""

number =  int(input("Enter The Number :-"))
prime_number = 1   # Setting a default value as 1 


for i in range(1,number+1) : # loop will start from 1 and End till number +1
      #Loop Body
    prime_number = prime_number * i  # Multipling a prime Number with loop varible i to find Prime Number
print(f"the prime Number of Number {number} is {prime_number}")

