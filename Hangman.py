# TITLE : Hangman
#
# DESCRIPTION : Guess a word from a list of hundreds! (be sure to download the wordlist associated with this script)
#
# 04/04/25

import random, os, time 


def chose_word_and_set(cont):
    global chosen_word, hidden_word, attempts, list_of_correct_letters, score, list_of_incorrect_letters, i
    list_of_correct_letters = ""
    list_of_incorrect_letters = ""
    hidden_word = ""
 
    if cont == "no":
        score = "0"
        attempts = "6"
    elif cont == "yes":
        score = int(score)+1


    script_directory = os.path.dirname(os.path.abspath(__file__))    #will grab the absolute path of the current directory that the file is in
    file_path = os.path.join(script_directory, "Hangman_wordlist.txt") #will add the wordlist to the abspath

    try:
        with open(file_path, "r") as file: #opens the file External\Hangman_wordlist.txt and randomly choses a line as the word that we will be using
            lines = file.readlines()
    except FileNotFoundError:              #if the wordlist isnt in the same file, an error will occur
        print("Error! Hangman_wordlist.txt not found! Make sure it is in the same folder as Hangman.py!")
        print("")
        input("Press ENTER to close!")
        exit()
        
    chosen_word = random.choice(lines).strip()

    while True:
        for i in range(len(str(chosen_word))):    #sets the hidden word to a bunch of _. The amount of _ will match the length of the chosen word
            hidden_word += "_"        
        break
    
    prompt()



def update_hidden_word():
    global list_of_correct_letters, hidden_word, attempts, chosen_letter                    
        
    for i in range(len(chosen_word)):               #This will check if the players guessed letter is in the chosen word by going through each letter in the chosen word and comparing it with the players chosen letter.
        if chosen_letter == chosen_word[i]:         #it will repeat this until a match is found. That matched letter will then be placed into a list of correctly guessed letters.
            list_of_correct_letters += chosen_letter
            break
    
    hidden_word = ""                                #This will generate the new hidden word by going through each letter of the chosen word and checking to see if that letter is in the list of correctly chosen letters.
    while True:                                     #If it is, that letter will be appened into the hidden word. If its not, an _ will be appened.
        for i in range(len(str(chosen_word))):
            if chosen_word[i] in list_of_correct_letters:
                hidden_word += chosen_word[i]
            else:
                hidden_word += "_"
        break
        
    
    prompt() 



def generate_hangman():
    global attempts

    print("       _________ ")
    print("        |     |  ")
    if int(attempts) < 6:
        print("        |     O  ")
    else:
        print("        |        ")
    if int(attempts) == 4:
        print("        |     |   ")
    elif int(attempts) == 3:
        print("        |    /|  ")
    elif int(attempts) < 3:
        print("        |    /|\ ")
    else:
        print("        |        ")
    if int(attempts) == 1:
        print("        |    /   ")
    elif int(attempts) < 1:
        print("        |    / \ ")
    else:
        print("        |        ")
    print("        |        ")
    print("        |        ")
    print("_________________")



def prompt():
    global chosen_letter, chosen_word, hidden_word, list_of_correct_letters, attempts,list_of_incorrect_letters

    os.system("cls")
    print(f"Attempts left : {attempts} | Score : {score}")
    print("")
    generate_hangman()
    print("")
    #print(chosen_word)
    #print(streak) 
    for char in hidden_word:
        print(char.upper(), end = ' ')
    print("")
    print(f"Letters tried : {list_of_incorrect_letters}")
    print("")
    

    if hidden_word == chosen_word:
        attempts = int(attempts)+1
        print(f"You found it! The word was {((chosen_word).upper())}!")
        time.sleep(2)
        print("")
        input("Press ENTER to continue!")
        chose_word_and_set("yes")

    if attempts != 0 :
        chosen_letter = input("Chose a letter : ")
        if isinstance(chosen_letter, (str)) and chosen_letter.lower() in "abcdefghijklmnopqrstuvwxyz":   #This checks if the chosen letter isnt anything but a letter
            chosen_letter = chosen_letter.lower()
            if chosen_letter in chosen_word:
                update_hidden_word()
            else:
                if chosen_letter not in list_of_incorrect_letters:
                    attempts = int(attempts)-1
                    list_of_incorrect_letters += chosen_letter
                prompt()
        else:
            prompt()
    else:
        print(f"Game Over! The word was {(chosen_word.upper())}!")
        time.sleep(3)
        print("")
        input("Press ENTER to play again!")
        chose_word_and_set("no")


chose_word_and_set("no")
