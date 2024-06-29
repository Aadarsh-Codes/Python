"""
@ file :- List_Methods.py
@ Description :- Studying About List Methods
@ Author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)

"""

# crating List
a = list()


print(a.extend([10,40,20,30,40,'hello',12.4])) # Extending list 

#appending a string in list
a.append('aaddarsh')
print(a)

# poping elemnt form the list
a.pop()
print(a)

#poping a elemnt from sepecified index
a.pop(0)
print(a)

# removing a mentioned string from lisr
a.remove('hello')
print(a)

# reversing a list 
a.reverse()
print(a)

# sorting a list
a.sort()
print(a)

#print index of 30
print(a.index(30))

#print total count of number
print(a.count(40))

# clearing list 
a.clear()
print(a)