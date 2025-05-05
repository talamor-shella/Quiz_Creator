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
#for looping through question and answer from file
#while loop for starting a quiz
