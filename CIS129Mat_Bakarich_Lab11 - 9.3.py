# Module 11 Lab 11
# Mat Bakarich
# November 12, 2024
# Deitel & Deitel Exercise 9.3

# Class Averages Stored as .csv

# import csv
import csv

# print variables to .csv ub tge following format:
# firstname,lastname,exam1grade,exam2grade,exam3grade


# define main function
def main():

    # initialize variables
    keep_going = ""
    first_name = ""
    last_name = ""
    exam_1_grade = 0
    exam_2_grade = 0
    exam_3_grade = 0
    # use this constant to set the highest acceptable number input for a grade.
    GRADE_CAP = 150

    # handle PermissionError exceptions
    try:
         
        # open 'grades.csv' or create it     
        with open('grades.csv', mode='w', newline='') as grades:
            writer = csv.writer(grades)
        
            # loop to get and validate inputs and store them as variables
            while keep_going != 'n':
                # get and validate user input 
                try: 
                    
                    # get and validate first_name
                    while True:
                        first_name = str(input("Please enter student first name."))
                        if first_name and not first_name.isspace():   
                            break 
                    
                    # get and validate last_name
                    while True:
                        last_name = str(input("Please enter student last name."))
                        if last_name and not last_name.isspace():
                            break  
                    
                    # get and validate exam_1_grade
                    while True:
                        exam_1_grade = int(input("Please enter Exam 1 grade."))
                        if exam_1_grade < 0 or exam_1_grade > GRADE_CAP:
                            print("Please enter a number between '0' and '150'")
                        if 0 <= exam_1_grade < GRADE_CAP:
                           break
                    
                    # get and validate exam_2_grade
                    while True:
                        exam_2_grade = int(input("Please enter Exam 2 grade."))
                        if exam_2_grade < 0 or exam_2_grade > GRADE_CAP:
                            print("Please enter a number between '0' and '150'")
                        if 0 <= exam_2_grade < GRADE_CAP:
                           break    

                    # get and validate exam_3_grade
                    while True:
                        exam_3_grade = int(input("Please enter Exam 3 grade."))
                        if exam_3_grade < 0 or exam_3_grade > GRADE_CAP:
                            print("Please enter a number between '0' and '150'")
                        if 0 <= exam_3_grade < GRADE_CAP:
                           break        
                    
                    # ask the user if they wish to continue entering data and validate the input
                    while True: 
                        keep_going = input("Enter more data? (y/n) ").lower()
                        if keep_going in ["yes", "y", "no", "n"]:
                            break
                        print("Invalid input. Please enter yes or no.")
                    # include 'no' as an acceptable response
                    if keep_going == 'n' or keep_going == 'no':
                     keep_going = 'n'
                    

               
                # validate input type
                except ValueError:
                    print("Value Error. Please enter names as strings and grades as integers.")
                # write the variables to the csv as a row
                else:
                    writer = csv.writer(grades)
                    writer.writerow([first_name, last_name, exam_1_grade, exam_2_grade, exam_3_grade,])

        # output to let the user know the program has terminated and saved the file.     
        print("Program ended, Grades saved to grades.csv.")
     
    # Handle PermissonError exceptions 
    except PermissionError:
        print("Permissions Error. Please check filepath and permissions and try again.")

 

# call main
main()
