#Project #2 (This is another example of two classes and inheritance, 
#the car_demo class will inherit from the Automobiles class),
#the __init__ function is called automatically every time the class 
#is used to create an object.

#Create a new class and name its vehicles and type in the 
#following code below:

class Automobiles:

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    #these are the mutator methods
    def set_make(self, make):
        self.__make = make
    
    def set_model(self,model):
        self.__model = model

    def set_mileage(self,mileage):
        self.__mileage = mileage

    def set_price(self,price):
        self.__price = price

    #these are the accesssor methods
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_mileage(self):
        return self.__mileage
    
    def get_price(self):
        return self.__price
        

