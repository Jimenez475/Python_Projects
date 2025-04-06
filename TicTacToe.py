# TITLE : TicTacToe
#
# DESCRIPTION : Play a friend in TicTacToe!
#
# 03/29/25 - 03/30/25

import os

def game_start():
    global player_turn, prompt_sentence, winning_numbers, player_x_slots, player_o_slots, game_over, max_turns, checksum_list, player_grid_placements
    player_turn = 'x'
    prompt_sentence ='Enter a number from 1-9 : '
    winning_numbers = ["123", "456", "789", "159", "357", "147", "258", "369"]
    player_x_slots = ''
    player_o_slots = ''
    game_over = 0
    max_turns = 1
    checksum_list = ''
    player_grid_placements = list("0123456789")  #a list that holds what positions symbols are in.
    print_board()



def check_if_player_win():  #Checks if the player has tokens on winning combos
    global checksum, checksum_list, winning_numbers, game_over, max_turns

    if player_turn == 'x':
        checksum_list = sorted(str(player_x_slots))            #make a list of the players selected slots.            
        checksum = ''                                           
        
        for i in range(8):                                     #repeat the following 8 times (the length of the list winning_numbers).
            checksum = ''
            for j in range(len(checksum_list)):                 #repeat the following x times (the length of the players selected slot list).
                if checksum_list[j] in winning_numbers[i]:      #if x character in selected slot list is in the x group of winning numbers, appened it into checksum.
                    checksum += checksum_list[j]                #we are cycling through each digit in the players selected slot list and comparing it to each winning combo. If we spot a matching number we append it into checksum
                    if len(checksum) == 3:                      
                        if checksum == winning_numbers[i]:      #once checksum has reach the length of 3 we compare it to the x group of winning combo. If it isnt a match, we repeat.
                            game_over = 1
                            print_board()
    elif player_turn == 'o':
        checksum_list = sorted(str(player_o_slots))
        checksum = ''

        for i in range(8):
            checksum = ''
            for j in range(len(checksum_list)):
                if checksum_list[j] in winning_numbers[i]:
                    checksum += checksum_list[j]
                    if len(checksum) == 3:
                        if checksum == winning_numbers[i]:
                            game_over = 1
                            print_board()

    if max_turns == 9:      #This checls if the game ends in a tie. There is a limit of 9 turns before no players can make another. If it ends in a tie this will run. But if its the last move and a player wins on that last move, the code above this will trigger the win, overwriting the tie.
            game_over = 2
            print_board()
        


def print_board():  #Generates the board
    os.system('cls' if os.name == 'nt' else 'clear')   #clears the console
    print(f'   |   |   ')
    print(f' {player_grid_placements[1]} | {player_grid_placements[2]} | {player_grid_placements[3]} ')
    print(f'___|___|___')
    print(f'   |   |   ')
    print(f' {player_grid_placements[4]} | {player_grid_placements[5]} | {player_grid_placements[6]} ')   #create the board and enter x positions from a list that stores what symbols (x or o) are where.
    print(f'___|___|___')
    print(f'   |   |   ')
    print(f' {player_grid_placements[7]} | {player_grid_placements[8]} | {player_grid_placements[9]} ')
    print(f'   |   |   ')
    #print(max_turns)
    print('')
    if game_over == 1:
        print(f'Game over! Player {player_turn} wins!')
        print('')
        input('Press ENTER to player again!')
        game_start()
    elif game_over == 2:
        print(f'Game over! Tie!')
        print('')
        input('Press ENTER to player again!')
        game_start()
    else:
        print(f'Player {player_turn}\'s turn!')
        prompt()

def prompt():   #prompts the user for their input along with telling them what they could've done wrong.
    global player_turn, prompt_sentence, player_x_slots, player_o_slots, max_turns

    print('')

    if player_turn == 'x':
        placement = (input(f'{prompt_sentence}'))   

        if placement.isdigit():
            placement = int(placement)

            if placement != 0 and placement < 10:
                if player_grid_placements[placement] in '123456789':      #checks if the place in the grid list equal to the number you chose is in the following list.
                    player_grid_placements[int(placement)] = f'\33[31mx\33[0m'    #once youve chosen a number from 1-9 we will find the position of that number then replace the position in 'grid_placement' with an x. Also theyre red.
                    player_x_slots += str(placement)
                    
                    check_if_player_win()
                    if game_over == 1:
                        print_board()
                        return
                    prompt_sentence ='Enter a number from 1-9 : '                          #all of these are illegal moves, a slot thats taken, something that isnt a number, or a number out of the range 1-9.
                    player_turn = 'o'
                    max_turns += 1
                else:
                    prompt_sentence = 'That slot is taken! Enter a number from 1-9 : '
            else:
                prompt_sentence = f'Enter a number from \33[31m1-9!\33[0m : '
        else:
            prompt_sentence = "Enter a NUMBER from 1-9! : "
    elif player_turn == 'o':
        placement = (input(f'{prompt_sentence}'))

        if placement.isdigit():
            placement = int(placement)

            if placement < 10:
                if player_grid_placements[placement] in '123456789':
                    player_grid_placements[int(placement)] = f'\33[31mo\33[0m'
                    player_o_slots += str(placement)

                    check_if_player_win()
                    if game_over == 1:
                        print_board()
                        return
                    prompt_sentence ='Enter a number from 1-9 : '
                    player_turn = 'x'
                    max_turns += 1
                else:
                    prompt_sentence = 'That slot is taken! Enter a number from 1-9 : '
            else:
                prompt_sentence = "Enter a number from 1-9! : "
        else:
            prompt_sentence = 'Enter a NUMBER from 1-9! : '
    print_board()

game_start()