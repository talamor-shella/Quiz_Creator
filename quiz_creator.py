#Assignment 9- Quiz Creator

"""
Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. 
Write the collected data to a text file. Ask another question until the user chose to exit.

"""

def quiz_creator():
    
    print("Welcome to Quiz Creator!")
    print("You can select any category for making a quiz.")

    #While loop until invalid
    while True:     
        
        #make a category to properly organize questions
        category = input("Enter a category for making a question (Math, English, Science, and History): ").lower()

        #create a text file for each category        
        filename = category + ".txt"

        #ask user input for a question
        question = input("Enter a question: ")

        #ask for 4 possible answers   
        choices_a = input("Option a: ")
        choices_b = input("Option b: ")
        choices_c = input("Option c: ")
        choices_d = input("Option d: ")
    
        #ask the correct answer
        correct_answer = input("Enter the correct answer (a/b/c/d): ")

        #to double check if the question and inputs are correct
        print(f"Question: {question}")
        print(f"a) {choices_a}")
        print(f"b) {choices_b}")
        print(f"c) {choices_c}")
        print(f"d) {choices_d}")

        confirm = input("Is the question and answer correct before adding to file? type yes or no: ").lower()
        #if statement for confirming
        if confirm == "yes":

            #creates a text file for each category, appends all the questions and answers
            with open (filename, "a") as file:

                file.write(f"\nQuestion: {question}\n")
                file.write(f"a) {choices_a}\n")
                file.write(f"b) {choices_b}\n")
                file.write(f"c) {choices_c}\n")
                file.write(f"d) {choices_d}\n")
                file.write(f"The correct answer is: {correct_answer}\n")

        #ask user if want to add more question
        add_question = input("Do you want to add more question? (yes or no): ").lower()

        #if statement to check if yes or no
        if add_question != "yes":
            print("Exits Quiz Creator!")
            break
quiz_creator()