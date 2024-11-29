# Module 12 Lab 12
# Mat Bakarich
# November 20, 2024



"""This class is for creating and editing 'Pet' objects in python. 

The pet object stores 3 values, a string for name, a string for pet type, and an intger for age.
The setter functions modify the values for a pet object.
The getter functions return the assigned values.
"""


# define Pet class.
class Pet:
    
# fields
    
    #Private String name 
    __pet_name = ""
   
    #Private String type
    __pet_type = ""
    
    #Private String age
    __pet_age = 0


##############################
##        constructor       ##
##############################

    def __init__(self,pet_name,pet_type,pet_age):
        self.__pet_name = pet_name
        self.__pet_type = pet_type
        self.__pet_age = pet_age
        
        # validate user inputs before initializing Pet object.
        if type(pet_name) != str:
            raise ValueError("Pet name must be a string.")
        if type(pet_type) != str:
            raise ValueError("Pet type must be a string.")
        if type(pet_age) != int:
            raise ValueError("Pet age must be an integer.")  
    

##############################
##         mutators         ##
##############################


# Public Module set_name(string)   
    def set_name(self, pet_name):
        # validate input is a string
        if type(pet_name) != str  or pet_name.isspace():
            raise ValueError("Pet name must be a string.")
        # change the pet name
        else:
            self.__pet_name = pet_name
        
        
    

# Public Module set_type(string)    
    def set_type(self, pet_type):
        # validate input is a string    
        if type(pet_type) != str or pet_type.isspace():
            raise ValueError("Pet type must be a string.")
        # change pet type    
        else: 
            self.__pet_type = pet_type   

              
    

# Public Module set_age(integer)       
    def set_age(self, pet_age):
        
        # validate input is an integer
        if type(pet_age) != int:
            raise ValueError("Pet age must be an integer.")
        if pet_age < 1:
            raise ValueError("Pet age must be greater than 0.")     
        # change pet age
        else:
            self.__pet_age = pet_age
                 

            
    

###############################
##         accessors         ##
###############################


    # Public Function String get_name()
    def get_name(self): 
        return self.__pet_name
   

    # Public Function String get_type()
    def get_type(self):
        return self.__pet_type
    
    
    # Public function Integer get_age()
    def get_age(self):
        return self.__pet_age
    