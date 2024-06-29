"""
@ file :- String_Methods.py
@ Description :- Studying About String Methods
@ Author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)

"""

Str1 = " aadarsh "
Str2 = "hello World"

print(Str1.endswith("sh"))  # Return True if String ends with sh either it give false

print(Str1.capitalize()) # Capitalize 1st character

print(Str1.replace("aadarsh","Karan")) # repalce the character / Word 

print(Str1.find("a")) # return the 1st index of 1st  Occurence 

print(Str1.count("a")) # count the occuerence of the substr from the string

print(Str1.upper()) # convert String into Upper Case 

print(Str1.lower()) # Convert String into Lower Case 

print(Str1.strip()) # Remove Space between String

print(Str1.lstrip()) # Remove Left Side Space

print(Str1.rstrip()) # Remove Right Side Space

print(Str2.split('--')) # Seprated With ,

print(Str1.startswith("a")) # Return True if String Start with  a 

print(Str1.isalpha()) # Return True if all Character in the String 

print(Str1.isdigit()) # Return True if all Numbeers are in the string

print(Str1.isalnum()) # Return True if String Consist number and Character 