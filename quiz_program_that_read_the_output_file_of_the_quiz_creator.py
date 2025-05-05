#For Assignment 10: Quiz

"""
Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and 
check if the answer is correct.

"""

#import random
import random

#ask user input the category of the quiz
quiz_category = input("Enter the category of quiz you want (Math, English, Science, History): ").lower()

#concentenate the category and ".txt"
filename_category = quiz_category + ".txt"

#open the category file 
with open(filename_category, "r") as file:
    lines = file.readlines()

#empty list to store questions, choices, and answer
questions = []

#for looping through question, choices, and answer from file
for i in range(0, len(lines), 7):

    #try-except to avoid error in index
    try:
        question = lines[i+1].strip()
        choices_a = lines[i+2].strip()
        choices_b = lines[i+3].strip()
        choices_c = lines[i+4].strip()
        choices_d = lines[i+5].strip()
        answer = lines[i+6].strip().replace("The correct answer is: ","")

        #append the questions, choices and answers
        questions.append({
            "question": question, "choices": {"a": choices_a, "b": choices_b, "c": choices_c, "d": choices_d},
            "answer": answer
        })
    except IndexError:
        continue    

#while loop for starting a quiz
while questions:

    #randomly selecting a questions from the list
    current_question = random.choice(questions)

    #Display the current question
    print(current_question["question"])

    #loop through each choices and print
    for key, val in current_question["choices"].items():
        print(val)

    #ask user their answer
    user_answer = input("Enter your answer (a/b/c/d): ").lower()

    #checks if the answer is correct 
    if user_answer == current_question["answer"]:
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is {current_question['answer']}\n")

    #to avoid repeating questions
    questions.remove(current_question)
    