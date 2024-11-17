# Module 11 Lab 11
# Mat Bakarich
# November 12, 2024
# Deitel & Deitel Exercise 9.2


# define main function
def main():
    # intialize variables
    
    # running total of grades
    total = 0    
    # count the number of grade entries
    count= 0
    # intialize the average grade to 0
    average = 0

    # try block for exception handling
    try:        
        # open file for reading   
        with open('grades.txt', mode='r') as grades:
            
            # print each grade on a new line
            print("\nThe grades from file are:\n")
            for line in grades:
                try:
                    # convert grades to integers for calculations
                    number = int(line.strip())
                    # print each grade
                    print(number)
                    # add the grade to the total
                    total+= number
                    # add one to the count of number of grades
                    count+=1
                # print an empty line instead of returning an error at the end of the file. Grade inputs validated by the write program.
                except ValueError:
                    print("")  

        try:
            # calculate the average grade
            average = total/count 
        except ZeroDivisionError:
            print("Error ocurred. Total number of grades cannot be zero.")
        
        # print the total number of grades.
        print(f"\nThe total number of grades is: {count}.")

        # print the total of the grades.
        print(f"The total of the grades is: {total}.")

        # print the average grade.
        print(f"The average grade is: {average:.2f}.\n")
    # handle exceptions    
    except FileNotFoundError:
        print("No such file found, please double check that grades.txt is in the correct directory and try again.")   
    except PermissionError:
        print("Permissions error ocurred, unable to open file.")         

# call the main function
main()       
