# Lab 7-3 The Dice Game
# Mat Bakarich
# October 18, 2024
# This program runs a dice game of craps for two players


# add libraries needed
import random
# the main function
def main():
    
    
    # initialize variables
    end_program = 'no'
    player_one = 'NONAME' 
    player_two = 'NONAME'

    # call to input_names
    player_one, player_two = input_names(player_one, player_two)
    # while loop to run program again
    while end_program == 'no':
        # populate variables
        winner_name = 'NONAME'
        p1_number = 0
        p2_number = 0
        # call to roll_dice
        winner_name = roll_dice(p1_number, p2_number, player_one, player_two, winner_name)
        
       
        # call to display_info
        display_info(winner_name)
        # call to keep_playing
        if keep_playing(end_program):
            end_program = 'yes'
        else: end_program = 'no'
          
    print("Program ended.")    
# get input from user to end or continue the program
def keep_playing(end_program):
    
        while True:
            
            end_program = input("Do you want to end the game? Please enter 'yes' or 'no'. ").lower()
            if end_program in ['yes','y']:
                return True
            if end_program in ['no','n']:
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
            

# this function gets the players names
def input_names(player_one, player_two):
    while True:
        player_one = input(str("Please enter player one's name."))
        if player_one:
            break
        else:print("Name cannot be blank. Try again.")
    while True:
        player_two = input(str("Please enter player two's name."))
        if player_two:
            break
        else:print("Name cannot be blank. Try again.")
    return player_one, player_two


# function to simulate rolling two dice and display the outcomes
# this function gets the players names
def roll_dice(p1_number, p2_number, player_one, player_two, winner_name): 
    p1_number = random.randint(1, 6)
    p2_number = random.randint(1, 6)
    if p1_number > p2_number:
        winner_name = {player_one}
    elif p2_number > p1_number:
        winner_name = {player_two}
    elif p1_number == p2_number: 
        winner_name = "TIE"
    # print the outcome of the die rolls
    print(f"Player One rolled ", p1_number,".",sep="")
    print(f"player Two rolled ", p2_number,".",sep="")
    return winner_name
    
# function to display the winner    
def display_info(winner_name):
    print(f"The winner is:",winner_name)


# call to main function
main()