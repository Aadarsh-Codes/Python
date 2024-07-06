"""
@file :- pattern_02.py
@brief :- this code will print this pattern :- *
                                              ***
                                             *****
@auther :- Aadarsh Nanaware (nanawareaadarsh333@gmail.com)
"""



n = 3  # Initializing a row 
row = 0 # Initializing a row counter 
  
# a while loop will goes until row < n
while row < n:
    # Print leading spaces
    
    spaces = n - row - 1 # Initializing a Space
    
    # a while loop will goes untill spces > 0 
    while spaces > 0:
        print(' ', end='')
        spaces -= 1  # decrementing space by 1 
    
    # Print asterisks
    stars = 2 * row + 1  # Initializing a stars 
    # a while loop will be goes untill stars > 0
    while stars > 0:
        print('*', end='')
        stars -= 1
    
    print()
    row += 1 # Incrementing a row by 1