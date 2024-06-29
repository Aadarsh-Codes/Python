"""
@ file :- List_Methods.py
@ Description :- Studying About List Methods
@ Author :- Aadarsh Nanaware(nanawareaadarsh7@gmail.com)

"""


a = list()
print(type(a))
print(a.extend([10,40,20,30,40,'hello',12.4])) # Extending list 
a.append('aaddarsh')
print(a)

a.pop()
print(a)

a.pop(0)
print(a
	)
a.remove('hello')
print(a)

a.reverse()
print(a)

a.sort()
print(a)

print(a.index(30))

print(a.count(40))

a.clear()
print(a)