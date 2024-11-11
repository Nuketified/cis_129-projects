# Module 10 Lab 10
# Mat Bakarich
# November 5, 2024

####################
# Check Protection #
####################
# This program takes an input in dollars and converts it to a check-protected value.
# 

# import RegEx for input validation
import re 

# define main function
def main():
    
    # declare variables
    check_amount = 0


    # function to validate user input
    def validate_input(check_amount):
       
        # set check amount to string
        check_amount = str(check_amount)

        # pattern to search for with regex
        pattern = r"^[0-9.]+$"
        if bool(re.match(pattern, (check_amount))):
            return True
        # ensure there are no more than 1 "." in input
        elif (check_amount).count(".") > 1:
            return False
        
        
    

    # get user input and validate input for check amount
    def get_input(check_amount):
        while True:
            try:
                # get the unser input as a decimal
                check_amount = float(input("Please enter the check amount as a decimal."))
            except ValueError:
                continue
                # call function to validate input
            if validate_input(check_amount) == True:
               return check_amount
            else:
                continue



        
    
    # function convert user input into check-protected format.
    def format_check(check_amount):
        # convert to a float
        check_amount = float(check_amount)
        # format check_amount to be right-aligned in a field of 10 characters and filled by "*"
        check_amount = f'${check_amount:*>10,.2f}'
        # print the Check-Protected output
        print(check_amount)


    # call get_input
    check_amount = get_input(check_amount)
    
    # call format_check
    format_check(check_amount)
    

# call main
main()    