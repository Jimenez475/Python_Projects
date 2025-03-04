#TITLE : Password Generator
#
#DESCRIPTION : Generate a password!
# 
# 03/01/25

import random
import string
import time
import os

def prompt():
    os.system('cls')
    while True:
        length_of_password = input("Enter the length of your password : ")  #prompts for length of password
        if length_of_password.isdigit():                                    #checksum to see if the input is a digit                
            length_of_password = int(length_of_password)                    #if it is a digit, it will change the variable to a integer so the generator can correctly interpret
            break
        else:
            print('Invalid Input! Enter whole numbers only')
            time.sleep(2)
            prompt()

    characters = string.ascii_letters + string.digits + string.punctuation #combines all lowercase, uppercase, digits and special characters into one variable

    password = ''.join(random.choice(characters) for _ in range(length_of_password)) #joins an empty space with a random character from the 'character' variable, 'length_of_password' times
    #                                                                                 the _ is a throwaway variable telling the loops counter is not used within the loops body
    
    print(f'Here is your password! : {password}') #prints the password   
    print('')
    input('Press ENTER to finish')
    
prompt()