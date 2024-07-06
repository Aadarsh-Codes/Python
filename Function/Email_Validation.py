"""
@file :- Email_Validation.py
@brief :- This Script write a function that will check if the user entered Correct email or not
@author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""


# importing the regular expression 
import re 


# Fuction defination 

"""
*function :Function that check email is valid or not
*identifier : Email_Validator()
*parameters : Email
*returns    : if true then Email is Valid else Email is not valid
"""

def Email_Validator(Email):
    # Define a regular expression pattern for a valid email address
    expression = "[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    
    # Use re.match to check if the email matches the pattern
    if re.match(expression, Email):
        # If the email matches the pattern, return a success message
        return f"The Entered {Email} is a valid Email"
    else:
        # If the email does not match the pattern, return a failure message
        return f"The Entered {Email} is not a valid Email"

# Prompt the user to enter an email address
Email = input('Enter the Email: ')

# Call the Function and print the output 
print(Email_Validator(Email))