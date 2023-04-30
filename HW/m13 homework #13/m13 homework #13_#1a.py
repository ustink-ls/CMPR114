#ShiftSupervisor Class

#In a particular factory, a shift supervisor is a salaried 
#employee who supervises a shift. In addition to a salary, 
#the shift supervisor earns a yearly bonus when his or her 
#shift meets production goals. Write a ShiftSupervisor 
#class that is a subclass of the Employee class you created 
#in Programming Exercise 1. The ShiftSupervisor class should 
#keep a data attribute for the annual salary, and a data 
#attribute for the annual production bonus that a shift 
#supervisor has earned. Demonstrate the class by writing a 
#program that uses a ShiftSupervisor object.


#The Employee class.
class Employee:
    #The __init__ method accepts an argument for the 
    #employee class's data attributes.
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
        
    #the following methods are mutators for the data
    #attributes
    def set_name(self, name):
        self.__name = name
    
    def set_number(self, number):
        self.__number = number

    #The following methods are accessors for the
    #data attributes.   
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number

#the ShiftSupervisor class is a subclass of the Employee class.
class ShiftSupervisor(Employee):
    #The init method accepts arguments for the
    #name, number, annual_salary, annual_prod_bonus.
    def __init__(self, name, number, annual_salary, annual_prod_bonus):
        #call the superclass __init_ method.
        Employee.__init__(self, name, number)

        #initialize the __annual_salary/annual_prod_bonus attributes.
        self.__annual_salary = annual_salary
        self.__annual_prod_bonus = annual_prod_bonus

    #the set_annual_salary/hourly_pay_rate are mutators for the 
    #__annual_salary/hourly_pay_rate attributes.
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary
    
    def annual_prod_bonus(self, annual_prod_bonus):
        self.annual_prod_bonus = annual_prod_bonus

    #the get_annual_salary/annual_prod_bonus methods are acessors 
    #for the __annual_salary/annual_prod_bonus attributes.
    def get_annual_salary(self):
        return self.__annual_salary
    def get_annual_prod_bonus(self):
        return self.__annual_prod_bonus

