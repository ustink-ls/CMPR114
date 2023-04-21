#Project #4
#The Customer class creates functions and objects.

class Customer:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    
    def set_name(self,name):
        self.__name = name
    
    def set_address(self,address):
        self.__address = address

    def self_phone(self,phone):
        self.__phone = phone

    def self_city(self,city):
        self.__city = city

    def self_city(self,zipCode):
        self.__zipCode = zipCode

    def self_city(self,age):
        self.__age = age
