"""
@file :- Quiz.py
@breif :- Making our 1st project in python
@author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""

#             Concepts That are used in this project 
#        1) List 
#        2)for Loop
#        3)Enumerate Function 
#        4)f String 
#        5)if - esle statement


# Define the list of questions with their options and correct answers
Quations = [
    ["What language is this code written in?", "python", "java", "c", "c++", 1],
    ["Which language is used to make Facebook?", "c#", "javascript", "php", "go", 3],
    ["What is the value of the following expression: (8^5 - 12 + (6 // 3))?", "34", "30", "28", "26", 2],
    ["In HTML, which tag is used to create a hyperlink?", "<link>", "<a>", "<herf>", "<url>", 2],
    ["Which SQL command is used to retrieve data from a database?", "GET", "FETCH", "SELECT", "RETRIEVE", 3],
    ["Which data structure operates on a Last In First Out (LIFO) basis?", "queue", "stack", "heap", "list", 2],
    ["What is the output of '2' + '3' in Python?", "5", "'23'", "TypeError", "None of the above", 2],
    ["Which programming language is often used for data analysis and scientific computing?", "Java", "R", "C++", "Swift", 2],
    ["What does CSS stand for in web development?", "Cascading Style Sheets", "Computer Style Sheets", "Creative Style Sheets", "Colorful Style Sheets", 1],
    ["What is the capital of France?", "Paris", "Berlin", "London", "Madrid", 1]
]

# Iterate each quation and enumerate for inexing 
for index, i in enumerate(range(0, len(Quations))):
    # Initializing a quation of Quations of i
    quation = Quations[i]
    
    #printing a Quation
    print(f"{index+1} {quation[0]}")
    print("\n")
    
    #printing a Options  of a quation 
    print(f"a) {quation[1]}     b) {quation[2]}")
    print(f"c) {quation[3]}     d) {quation[4]}")


    # taking user input for the answer 
    answer = int(input("Enter your Answer: "))

    # condition to check for write answer
    if answer == quation[-1]:
        print("Correct Answer") # If yes then print Correct Answer
    else:
        print("Your Answer is Wrong") # rather than your answer is Wrong 
        # and breaking the loop
        break
