
"""
@file :- Set_Methods.py
@brief :- Demonstration of common methods Set Methods
@Author :- Aadarsh Nanaware (nanawareaadarshh7@gmail.com)
@Date :- 14/06/2024
"""

S = set() # crating Empty Set

print(type(S))

s = {12,14,89,'aadarsh'}

s.add('welcom')
print(s)

s.pop()
print(s)

s.remove(89)
print(s)

s.discard(14)
print(s)

s.update({36,39})
print(s)

s.clear()
print(s)




s1 = {1,2,3,4,5,6}
s2 = {6,3,7,8}


print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
