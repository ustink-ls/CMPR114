#1a. Pet Class

#Write a class named Pet, which should have the following 
#data attributes:
class Pet:
    #The Pet class should have an __init__ method that creates
    #these attributes.
    def __init__ (self,name, animal_type, age):
        #for the name of a pet
        self.__name = name
        #for the type of animal that a pet is. example values are
        #'Dog', 'Cat', and 'Bird'
        self.__animal_type = animal_type
        #for the pet's age
        self.__age = age
    
    #this method assigns a value to the __name field.
    def set_name(self,name):
        self.__name = name
    
    #this method assigns a value to the __animal_type field.
    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type
    
    #this method assigns a value to the __age field.
    def set_age(self,age):
        self__age = age

    #This method returns the value of the __name field.
    def get_name(self):
        return self.__name
    
    #This method returns the value of the __animal_type field.
    def get_animal_type(self):
        return self.__animal_type
    
    #This method returns the value of the __age field.
    def get_age(self):
        return self.__age



