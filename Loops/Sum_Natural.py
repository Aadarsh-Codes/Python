"""
@file :- Sum_Natural.py
@Brief :- Demonstration of While loop
@Author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""




# Prompt the user to enter a number and convert it to an integer
n = int(input("Enter the Number :-"))

# Initialize the sum variable to 0
sum = 0

# a while loop is goes until n >= )
while n >= 0:
    # Add the current value of n to the sum
    sum += n
    # Decrement n by 1 in each iteration
    n = n - 1

# Print the final sum using an f-string for formatting
print(f"sum = {sum}")
