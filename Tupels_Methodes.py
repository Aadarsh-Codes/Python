"""
@file :- Tupels_Methodes.py
@brief :- Demonstration of Tuple motheds in python
@author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""

#1 Indexing 
t1 = (1, 2, 3,'Hello','World')
print(t1[4])  # Output: Worl

#2 Slicing 
t2 = (1, 2, 3, 4, 5)
print(t2[2:4])  # Output: ( 3 , 4)

#3 Concat
t3 = (1, 2)
t4 = (3, 4)
t5 = t3 + t4
print(t5)  # Output: (1, 2, 3, 4)

#4 Repation 
t = (1, 2 , 3)
print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)

#5 Length 
t6 = (12, 56, 78, 52)
print(len(t6))   # Output: 3

#6 Membership
t7 = (12, 10, 18, 'abc')
print('abc' in t7)   # Output: True

#7 Unpacking 
t8 = (21, 12, 36)
v1, v2, v3 = t8 
print(v1, v2, v3) # Output: 21, 12, 36

#8 Count 
t9 = (1, 2, 3, 1, 6, 7)
print(t9.count(1)) # Output: 2

#9 Index 
t10 = (1, 2, 3, 1, 6, 7)
print(t10.index(1)) # Output: 0
