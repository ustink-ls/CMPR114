#Challenge Exercise #5: See the UML diagram below and create 
#the following three classes. The Insect class will be the main 
#or the superclass and the bumblebee and grasshopper classes 
#will act as the two sub-classes. Provide two characteristic 
#behaviors for the bumblebee and grasshopper, be sure to use 
#Mutator and Accessor methods for each class. Print or display 
#the two characteristics of each insect below.

#The Insect class represents a generic insect.
class Insect:
    #The __init__ method accepts an argument for the 
    #insect's species, ability, color.
    def __init__(self, species, ability, color):
        self.__species = species
        self.__ability = ability
        self.__color = color
        
    #the following methods are mutators for the data
    #attributes
    def set_species(self, species):
        self.__species = species
    
    def set_ability(self,ability):
        self.__ability = ability

    def set_color(self,color):
        self.__color = color

    #The following methods are accessors for the
    #data attributes.   
    def get_species(self):
        return self.__species
    
    def get_ability(self):
        return self.__ability
    
    def get_color(self):
        return self.__color

#the bumblebee class is a subclass of the Insect class.
class Bumblebee(Insect):
    #The init method accepts arguments for the
    #species, ability, color, and texture.
    def __init__(self, species, ability, color,texture):
        #call the superclass __init_ method.
        Insect.__init__(self, species, ability, color)

        #initialize the __texture attribute.
        self.__texture = texture

    #the set_texture is a mutator for the 
    #__texture attribute.
    def set_texture(self, texture):
        self.__texture = texture
    
    #the get_texture method is an acessor for the
    #__texture attribute.
    def get_texture(self):
        return self.__texture

#the grasshopper class is a subclass of the Insect class.
class Grasshopper(Insect):
    #The init method accepts arguments for the
    #species, ability, color, and body type.
    def __init__(self, species, ability, color,body_type):
        #call the superclass __init_ method.
        Insect.__init__(self, species, ability, color)

        #initialize the __body_type attribute.
        self.__body_type = body_type

    #the set_body_type is a mutator for the 
    #__body_type attribute.
    def set_body_type(self, body_type):
        self.__body_type = body_type
    
    #the get_texture method is an acessor for the
    #__texture attribute.
    def get_body_type(self):
        return self.__body_type