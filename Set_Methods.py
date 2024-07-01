
"""
@file :- Set_Methods.py
@brief :- Demonstration of common methods Set Methods
@Author :- Aadarsh Nanaware (nanawareaadarshh333@gmail.com)
"""

S = set() # crating Empty Set

#1 creating a set with values
s = {12,14,89,'aadarsh'}

#2 aadaing a Element in set
s.add('welcom')
print(s)      # Output: {12, 14, 'welcom', 89, 'aadarsh'}

#3 Poping a element from set
s.pop()
print(s)     # Output: {14, 'welcom', 89, 'aadarsh'}


#4 removing a specified element from the set
s.remove(89)
print(s)     # Output:  {14, 'aadarsh', 89}

#5 discarding a element from the set
s.discard(14)
print(s)     # Output: {'welcom', 'aadarsh'}

#6 updating a set 
s.update({36,39})
print(s)     # Output: {36, 39, 'welcom', 'aadarsh'}


#7 clearing a whole set
s.clear()
print(s)    # Output: set()



s1 = {1,2,3,4,5,6}
s2 = {6,3,7,8}

# 8 Union opearation on set
print(s1.union(s2))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

#9 Intersection operation on set
print(s1.intersection(s2))    # Output: {3, 6}

#10 Difference operation on set
print(s1.difference(s2))    # Output: {1, 2, 4, 5



# Note :- Except union,intersection and difference the Output of the set operation will be not same