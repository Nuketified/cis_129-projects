# Module 8 Lab 8
# Mat Bakarich
# October 23, 2024

# This program takes an input from a user and checks to see if that input is a palindrome

# import RegEx
import re 

# define function
def is_palindrome():
    
    # declare variables
    popped_element ="" # store elements popped from list
    test_list = [] # list to store each character from palindrome
    test_string = "" # string to be tested
    compare_string ="" # string to be compared to test string
    
    # get and validate an input from user to test
    while True:
        test_string = str(input("Please enter a potential palindrome to test.")).lower()
        if not test_string:
            print("No input received.")
        else:
            break

    # remove spaces and punctuation using RegEx
    test_string = re.sub('[^A-Za-z0-9]+', '', test_string)

   

    # add each character from string to list
    for char in test_string: test_list.append(char)
    
    # display a list of the characters stored in the test list to the user
    print(test_list)

    # loop to pop each item from list and add them to a string
    while test_list: 
        popped_element=test_list.pop
        compare_string+=popped_element() 
    


    # print outcome
    if compare_string == test_string:
        print("The string is a palindrome.")
    else: print("The string is NOT a palindrome.")
    



# call function
is_palindrome()
