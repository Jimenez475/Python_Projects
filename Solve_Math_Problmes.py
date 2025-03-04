#TITLE : solve_math_problems
#
#DESCRIPTION : Solve a math problem from a pool of 300 unique problems!
#
#03/01/2025

import os
import random
import time


def generate_math():
    os.system('cls')
    x = int(random.randint(1,10))
    y = int(random.randint(1,10))       #assign x and y a random number from 1-10
    operator = int(random.randint(1,3)) #assign operator a random number from 1-3 , this will be used to determine the operator that the math problem will use
    answer_to_question = ''
    user_answer = ''
    question = ''

    def ask_question():
        nonlocal user_answer, answer_to_question,question #this makes sure these 2 variables are accessable from this def

        if operator == 1:
            answer_to_question = x + y                      #gets the solution
            question = f"what is {x} + {y}? : "           #prints the question                                  
        elif operator == 2:
            answer_to_question = x - y
            if x < y:                              #will check if x is greater than y, this way we wont get an answer that is a negative number
                generate_math()
            question = f"what is {x} - {y}? : "
        elif operator == 3:
            answer_to_question = x * y
            question = f"what is {x} * {y}? : "
        

        while True:
            print("Solve the math problem!")
            user_answer = input(question)          #this is taking the question generated and displaying/asking the user
            if user_answer.isdigit():                  #this is the checksum that will see if the users answer is a whole number
                    user_answer = int(user_answer)     
                    break
            else:
                 print("Invalid Input! Enter whole numbers only!")  #if user answer is not a whole number we will get an error and another question will be asked
                 time.sleep(2)
                 generate_math()
        
        check_math()
     
    
    def check_math():
        if answer_to_question == user_answer:    #comparing the user answer to the solution
                print("Correct!")
                time.sleep(2)
                generate_math()      #will pause for 2 seconds before reseting the script
        else:
            print("Incorrect!")
            time.sleep(2)
            generate_math()
       
    ask_question()
   
    
generate_math()
