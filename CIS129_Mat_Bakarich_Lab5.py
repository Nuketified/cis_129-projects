# Module 5 Lab-5 
# Mat Bakarich 
# October 4, 2024
# This program calculates and stores a running total of bottles collected over 7 days, then asks the user if they want to input data for another week, then prints the total number of bottles collected and the amount paid out for the week.
#
#
# Lab 5 The Bottle Return Program
#
# Step 1: Declare variables below
#
total_bottles = 0  
counter = 1 # this variable will control the loop 
today_bottles = 0 # this variable will store the nummber of bottles returned on a day 
total_payout = 0 # this variable will store the calculated value of totalBottles times .10 
# call to get_total_bottles (get_total = get_total_bottles())
# call to get_today_bottles (get_today = get_today_bottles())

def main():    
    keep_going = True # this variable will be used to run the program again
    
    # Step 2: Loop to run program again
    while keep_going == True: # this loop runs the whole program as long as keep_going is True
    
        total_bottles = 0   # this variable will store the accumulated bottle values
        counter = 1         # this variable will control the loop
        today_bottles = 0   # this variable will store the nummber of bottles returned on a day
        total_payout = 0    # this variable will store the calculated value of totalBottles times .10
        
        while counter <= 7: # this loop runs until inputs have been collected for 7 days worth of bottles
            today_bottles = today_bottles + int(input(f"What is the number of bottles for day {counter}?")) #asks the user for input during each iteration of the loop
            counter += 1 # increases the value of the loop counter by 1 each iteration of the loop
            total_bottles = today_bottles #sets the running total of bottles from each day to the value for total bottles for the week
        
        # code to print the number of total bottles 
        print('\nTotal bottles collected for the week:', total_bottles) # prints the total number of bottles collected in a week
        # code to print the number of total paid out for the week
        # PAYOUT_PER_BOTTLE = .10
        total_payout = total_bottles * .10 # calculates the amount paid out for bottles in a week in dollars.
        total_payout =  str(format(total_payout, ".2f")) # formats total_payout to display 2 decimal points including .00 for prices.
        print('\nTotal payout for bottles collected this week:'' ''$',total_payout)  # prints the total amount paid out for returned bottles for the week 
    
        keep_going = prompt_for_continue() #calls the function prompt_for_continue and sets the output the variable keep_going
    
     
   
       
      
# Step 3: Code to set value of variables 
def prompt_for_continue():
        answer = str(input("Do you want to enter another week’s worth of data?\n(Enter 'y' or 'n')")) # asks for user input
        if answer == "y": return True # returns True if user input is "y"
        else: return False # returns False otherwise
    
# code to set value of variable today_bottles  
def get_today_bottles(): 
        today_bottles = (int(input('How many bottles collected today?')))
        return today_bottles

# code to set value of variable total_bottles
def get_total_bottles(): 
        total_bottles = int(total_bottles) + int(today_bottles)
        return total_bottles
    
# code to set value of variable totalPayout 
def get_total_payout(): total_payout = total_bottles * .1 
        

main() # calls the main function


      	
