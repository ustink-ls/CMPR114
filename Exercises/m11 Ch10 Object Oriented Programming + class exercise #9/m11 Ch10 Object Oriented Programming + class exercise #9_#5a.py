#Project #5
#First Class: Here we have a class named BankAccount which 
#it will be called from another class or an external class. 
#The __init__ allows us to create a custom constructor.

class BankAccount:
    #the self is used to represent the instance of the class.
    #it is used to access variables that belong to that class.
    #The __init__ method accepts an argument for
    #account's balance. It is assigned to the
    #__balance attribute.
    def __init__ (self,bal):
        self.__balance = bal

    #The deposit method makes a deposit into the
    #account.
    def deposit(self,amount):
        #add the balance
        self.__balance += amount
    
    #The withdraw method withdraws an amount from
    #the account
    def withdraw (self,amount):
        if self.__balance >= amount:
            #subtract the balance
            self.__balance -= amount
        else:
            print("error: insufficient funds")
    
    #the get_balance method returns the account
    #balance.
    def get_balance(self):
        return self.__balance