"""
@file :- Celcius_To_Fahrenite.py
@beief :- This Script write a function thayt will convert Celcius To Fahrenite
@auther :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""

# Function Defination

"""
*function : Function to convert celcius to fahrenite
*identifier : celcius_fahrenite_converter
*parameter : celcius()
*return : return a fahrenite
"""
# Define a function to convert Celsius to Fahrenheit
def celcius_fahrenite_converter(celcius):
    # Apply the formula to convert Celsius to Fahrenheit
    return (celcius * 9 / 5) + 32

# Prompt the user to enter a temperature in Celsius and convert it to an integer
ce = int(input("Enter Celsius: "))

# Call the conversion function and store the result in 'fahrenite'
fahrenite = celcius_fahrenite_converter(celcius=ce)

# Print the converted temperature in Fahrenheit using an f-string for formatting
print(f"{ce}° Celsius to Fahrenheit is {fahrenite}°F")
