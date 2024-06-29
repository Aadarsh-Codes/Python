"""
@ file :- String.py
@ Description :- Studying About String / String Slicing 
@ Author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)

"""
str = "Hello"     # String With Duble Quote
print(str)

str1 = 'Gyus'    # String With Single Quote
print(str1)

str2  = """ My Name is Aadarsh Nanaware 
We are Writing our Python Script 
for Strings
"""
print(str2)


# Accesing character of String

str3 = "Good"
print(str3[2])


# looping through the String

name = "Gapnapti"

for i in name:
    print(i)


#String Slincing 

string = "hello, World"
print(string[0:5])          # From Index 0 TO 5-1
print(string[:4])           # Also From Index 0 to 4-1
print(string[7:])           # From Index 7 To length of the string

# Negative Indexing 
print(string[0:-3])
