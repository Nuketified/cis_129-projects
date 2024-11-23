# Module 12 Lab 12
# Mat Bakarich
# November 20, 2024

################################################################################
##                         Pet Class Client Program                           ##
################################################################################
## this program initializes an object of the "Pet" class, stores user input,  ##
## then uses Pet methods to update and display the pet's information.         ##
################################################################################


# import pet class from pet.py module
from pet import Pet


# define main function
def main():

    # declare input variables
    
    # initialize input_name string
    input_name = ""
    # initialize input_type string
    input_type = ""
    # initialize input_age integer 
    input_age = 0


    # class variable to hold a pet
    # declare Pet Animal 
    Animal = ""
    # create a Pet object
    # set Animal = new Pet() 
    Animal = Pet(input_name,input_type,input_age)
    
    
    
    # get values for a pet. 
    

    # get and validate "name" input.
    while True:
        try:
            # display “Enter a pet name:”
            input_name =str(input("Please enter pet name.\n"))

        # validate input. 
        except ValueError:
            print("Pet name must be a string.\n")
        if input_name == "" or input_name.isspace() :
            print("No name entered.\n")
        elif input_name.isdigit():
            print("Pet name must include letters.\n")
        elif not input_name.isalpha():
            print("Pet name can only contain letters.\n")    
        else:
            break
   
    # capitalize first letter of name for later printing.
    input_name = input_name.capitalize()
    
    # set Animal's name property to name input from user.
    Animal.set_name(input_name) 
    
    
    # get and validate "type" input.
    while True:
        try:
            # display “Enter a pet type:”. 
            input_type = str(input("Please enter the type of animal.\n"))
    
        # validate input.
        except ValueError:
            print("Pet type must be a string.\n")
        if input_type == "" or input_type.isspace() :
            print("No name entered, please try again.\n")
        elif input_type.isdigit():
            print("Pet type must include letters.\n")
        elif not input_type.isalpha():
            print("Pet type can only contain letters.\n")    
        else:
            break
    
    # capitalize pet type for later printing
    input_type = input_type.capitalize()

    ####Input inputType
    # set Animal's type property to type input from user 
    Animal.set_type(input_type) 

    # get and validate "age" input.
    while True:
        try:
    
            # display “Enter a pet age:”
            input_age = int(input("Please enter the age of the pet.\n"))
        # validate input. 
        except ValueError:
            print("Pet age must be an integer.\n")
        if input_age < 0 and type(input_age) == int:
            print("Pet age cannot be a negative value.\n")
        elif input_age == 0:
            print("Pet age cannot be zero.\n")    
        else:
            break    


    ####Input inputAge 
    # set Animal's age property to age input from user.
    Animal.set_age(input_age) 

    
    
    
    
    ############################
    # show values for this pet # 
    ############################



    # print the pet's name.
    print("\nThe pet's name is: ",Animal.get_name(),".",sep="")
       
    # print the type of pet.
    print("\nThe type of pet is: ",Animal.get_type(),".",sep="")
    
    # print the pet's age. 
    print("\n",Animal.get_name(),"'s age is: ",Animal.get_age(),"\n",sep="") 




# call main function
main()    