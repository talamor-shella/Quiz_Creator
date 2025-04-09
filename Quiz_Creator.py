#Assignment 9- Quiz Creator

"""
Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. 
Write the collected data to a text file. Ask another question until the user chose to exit.

"""

print("Quiz Checker")

#While loop until invalid
while True: 

    #ask user input for a question
    question = input("Enter a question: ")

    #ask for 4 possible answers   
    a = input("option a: ")
    b = input("option b: ")
    c = input("option c: ")
    d = input("option d: ")
    
    #ask the correct answer
    correct_answer = input("enter the correct answer: ")