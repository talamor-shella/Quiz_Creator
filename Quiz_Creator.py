#Assignment 9- Quiz Creator

"""
Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. 
Write the collected data to a text file. Ask another question until the user chose to exit.

"""

#While loop until invalid
while True:     

    #ask user input for a question
    question = input("Enter a question: ")

    #ask for 4 possible answers   
    a = input("Option a: ")
    b = input("Option b: ")
    c = input("Option c: ")
    d = input("Option d: ")
    
    #ask the correct answer
    correct_answer = input("Enter the correct answer (a/b/c/d): ")

    #arranged question and answers
    print(f"\nQuestion: {question}")
    print(f"a) {a}")
    print(f"b) {b}")
    print(f"c) {c}")
    print(f"d) {d}")
    print(f"The correct answer is: {correct_answer}\n")

    #ask user if want to add more question
    add_question = input("Do you want to add more question? (yes or no): ").lower()

    #if statement to check if yes or no
    if add_question != "yes":
        break