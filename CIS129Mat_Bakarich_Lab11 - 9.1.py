# Module 11 Lab 11
# Mat Bakarich
# November 12, 2024
# Deitel & Deitel Exercise 9.1

# define main function
def main():
    
    # initialize variables
    user_input =""
    try:
        # open or create file for writing
        with open('grades.txt', mode='w') as grades:
            # loop to get and validate user input
            while user_input != "-1":
                # get user input
                try: 
                    user_input=(input("Please enter a grade, -1 to quit."))
            
                except ValueError:
                    print("Please enter grades as integers.")
                # ensures input is digits only and not the sentinel
                if user_input.isdigit() == False and user_input != "-1":
                   print("Please enter only whole numbers.") 
                # case for no user input
                if user_input == "":
                    print("No grade entered.")
                # writes the grade to the folder 
                if  user_input != "-1" and user_input != "" and user_input.isdigit() == True: 
                    print(user_input, file=grades)
    
    except PermissionError:
        print("Permission Error. Please check filepath and permissions and try again.")
    # prints confirmation that the program has ended.
    print("Program ended.")


# call main function
main()
