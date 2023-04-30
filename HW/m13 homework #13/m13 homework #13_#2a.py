#Person and Customer Classes

#Write a class named Person with data attributes for a person’s 
#name, address, and telephone number. Next, write a class named 
#Customer that is a subclass of the Person class. The Customer 
#class should have a data attribute for a customer number, and 
#a Boolean data attribute indicating whether the customer wishes 
#to be on a mailing list. Demonstrate an instance of the Customer 
#class in a simple program.

#The Person class.
class Person:
    #The __init__ method accepts an argument for the 
    #person's data attributes.
    def __init__(self, name, address, telephone_number):
        self.__name = name
        self.__address = address
        self.__telephone_number = telephone_number
        
    #the following methods are mutators for the data
    #attributes
    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address

    def set_address(self, telephone_number):
        self.__telephone_number = telephone_number

    #The following methods are accessors for the
    #data attributes.   
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_telephone_number(self):
        return self.__telephone_number

#the Customer class is a subclass of the Person class.
class Customer(Person):
    #The init method accepts arguments for the
    #name, address, telphone number, customer_number, mailing_list.
    def __init__(self, name, address, telephone_number, customer_number, mailing_list):
        #call the superclass __init_ method.
        Person.__init__(self, name, address, telephone_number)

        #initialize the new attributes.
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    #the set_ are mutators for the new attributes.
    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number
    
    def mailing_list(self, mailing_list):
        self.mailing_list = mailing_list

    #the get_methods are acessors for the new attributes.
    def get_customer_number(self):
        return self.__customer_number
    def get_mailing_list(self):
        return self.__mailing_list