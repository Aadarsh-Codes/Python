"""

@file :- Pattern_Function.py
@Description :- This script write a function that is used to print the pattern of stars :
                                                                    * * *
                                                                    * *
                                                                    *
@author :-  Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""

# Function Defination

"""
*function :  Function to print pattern
*identifier : print_pattern()
*parameter : None
*return  : None
"""

# Define a function to print a pattern of asterisks
def print_pattern():
    # Set the number of lines for the pattern
    num_lines = 3
    
    # Loop from the number of lines down to 1
    for i in range(num_lines, 0, -1):
        # Print i asterisks followed by a space, repeated i times
        print("* " * i)

# Call the function to print the pattern
print_pattern()

	

