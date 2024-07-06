"""

@file :- IF_Else.py
@Description :- Finding the grateest number fromt the 4 numbers enter by user 
@author :-  Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""

a = int(input("Ente First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Entr Third Number :"))
d = int(input("Enter Fourth Nubmer :"))


if a > b and a > c and a > d :
    print(f"the Number {a} is grater ")

elif b > a and b > c and b > d :
    print(f"the Number {b} is grater")

elif c > a and c > b and c > d :
    print(f"the  Number {c} is grater")

else :
    print(f"the Number {d} is grater")
