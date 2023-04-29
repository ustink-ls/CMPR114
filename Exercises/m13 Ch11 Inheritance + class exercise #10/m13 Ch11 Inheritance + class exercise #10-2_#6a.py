#Challenge Exercise #6: Continuing from project #3, add an 
#electric vehicle car with the same description, and print the 
#screen below.

#Project #3 (This is a continuation of project #2 (Automobile class)

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

class Truck(Automobiles):
    def __init__(self,make,model,mileage,price):
        Automobiles.__init__(self,make,model,mileage, price)

class SUV(Automobiles):
    def __init__(self,make,model,mileage,price):
        Automobiles.__init__(self,make,model,mileage, price)

#electric vehicle class
class EV(Automobiles):
    def __init__(self,make,model,mileage,price):
        Automobiles.__init__(self,make,model,mileage, price)