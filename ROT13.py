# TITLE : ROT13
#
# DESCRIPTION : Encode and Decode words with ROT13!
#
# 03/02/25

#dingo

import os

list_of_characters_1 = "abcdefghijklm" #our 2 lists of characters. As you can see, each character aligns with another in the opposite list
list_of_characters_2 = "nopqrstuvwxyz"
special_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def ROT13():
    os.system('cls')

    user_input = input("Enter the word you want to encode/decode with ROT13 : ")   #user input, the word we will be encoding/decoding

    word = user_input.lower()    #Lower case all the letters to make it work

    length_of_word = len(word)  #The length of the word we wanna encode. This will help us with letting us know what character we are looking at
    
    output = ''

    for i in range(length_of_word):
        if list_of_characters_1.rfind(word[i]) != -1:   #if letter x from 'word' is in this list, continue
            output += list_of_characters_2[int(list_of_characters_1.rfind(word[i]))]    #append this letters position from the opposite list
        elif list_of_characters_2.rfind(word[i]) != -1:
            output += list_of_characters_1[int(list_of_characters_2.rfind(word[i]))]
        elif word[i].isspace():     #if letter x from 'word' is a space, appened a space into the output
            output += ' '
        elif word[i].isdigit():     #if letter x from 'word' is a digit, appened the current letter (the digit) into the output
            output += str(word[i])
        elif word[i] in special_characters: #if letter x from 'word' is in the variable 'special_characters', appened the current letter (the special character) into the output
            output += str(word[i])
    
    print(f"Your string is now : {output}")
    print('')
    input('Press ENTER to finish')


ROT13()
