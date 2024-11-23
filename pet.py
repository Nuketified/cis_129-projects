# Module 12 Lab 12
# Mat Bakarich
# November 20, 2024


# Module to define "Pet" Class



# define Pet class.
class Pet:
    
# fields
    ####Private String name __name__
    
    
    
    __pet_name = ""
    ####Private String type
    __pet_type = ""
    ####Private String age
    __pet_age = 0

    ###############
    # constructor #
    ###############

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
    

    ############
    # mutators #
    ############


    # Public Module setName(string a)
        
    def set_name(self, pet_name):
        # validate input is a string
        if type(pet_name) != str  or not pet_name.isspace:
            raise ValueError("Pet name must be a string.")
        # change the pet name
        else:
            self.__pet_name = pet_name
        
        
    

    # Public Module setType(string)
        
    def set_type(self, pet_type):
        # validate input is a string    
        if type(pet_type) != str or not pet_type.isspace:
            raise ValueError("Pet type must be a string.")
        # change pet type    
        else: 
            self.__pet_type = pet_type   

              
    

    # Public Module setAge(integer)
        
    def set_age(self, pet_age):
        # validate input is an integer
        if type(pet_age) != int:
            raise ValueError("Pet age must be an integer.")
        if pet_age < 1:
            raise ValueError("Pet age must be greater than 0.")
        # change pet age
        else:
            self.__pet_age = pet_age 

            
    


    #############
    # accessors # 
    #############


    # Public Function String getName()
    def get_name(self): 
        return self.__pet_name
   

    # Public Function String getType()
    def get_type(self):
        return self.__pet_type
    
    
    # Public function getAge()
    def get_age(self):
        return self.__pet_age
    