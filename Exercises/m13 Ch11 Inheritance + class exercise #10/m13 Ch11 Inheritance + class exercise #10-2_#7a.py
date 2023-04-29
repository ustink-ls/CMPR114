#Employee and ProductionWorker Classes

#Write an Employee class that keeps data attributes for the 
#following pieces of information:
#• Employee name
#• Employee number
#Next, write a class named ProductionWorker that is a subclass 
#of the Employee class. The ProductionWorker class should keep 
#data attributes for the following information:
#• Shift number (an integer, such as 1, 2, or 3)
#• Hourly pay rate
#The workday is divided into two shifts: day and night. The shift 
#attribute will hold an integer value representing the shift that 
#the employee works. The day shift is shift 1 and the night shift 
#is shift 2. Write the appropriate accessor and mutator methods 
#for each class.
#Once you have written the classes, write a program that creates 
#an object of the ProductionWorker class and prompts the user to
#enter data for each of the object’s data attributes. Store the 
#data in the object, then use the object’s accessor methods to 
#retrieve it and display it on the screen.

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

#the ProductionWorker class is a subclass of the Employee class.
class ProductionWorker(Employee):
    #The init method accepts arguments for the
    #name, number, shift_number, hourly_pay_rate.
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        #call the superclass __init_ method.
        Employee.__init__(self, name, number)

        #initialize the __shift_number/hourly_pay_rate attributes.
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    #the set_shift_number/hourly_pay_rate are mutators for the 
    #__shift_number/hourly_pay_rate attributes.
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
    
    def hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate
    
    #the get_shift_number/hourly_pay_rate methods are acessors for the
    #__shift_number/hourly_pay_rate attributes.
    def get_shift_number(self):
        return self.__shift_number
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

