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

#for looping through question and answer from file
for i in range(0, len(lines), 6):
    question = lines[i].strip()
    choices_a = lines[i+1].strip()
    choices_b = lines[i+2].strip()
    choices_c = lines[i+3].strip()
    choices_d = lines[i+4].strip()
    answer = lines[i+5].strip()
    
#while loop for starting a quiz
