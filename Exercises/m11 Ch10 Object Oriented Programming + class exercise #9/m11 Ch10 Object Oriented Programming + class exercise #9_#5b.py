#import the other class file that contains the data. Since I cannot 
#import a file with a long file name that includes spaces, use 
#the below import. Or name module something simple like class3, 
#and then use import class3.
import sys
sys.path.append("/Users/leslyesirena/Desktop/Python/m11 Ch10 Object Oriented Programming + class exercise #9_#5a")
class3 = __import__("m11 Ch10 Object Oriented Programming + class exercise #9_#5a")

#start the main function
def main():
    #get the starting balance.
    start_bal = float (input("enter your starting balance: "))

    #call the external class3.name of the class, in our its
    #called BankAccount from the class 3
    #Create a BankAccount object.
    savings = class3.BankAccount(start_bal)

    #Deposit the user's paycheck.
    pay = float(input("how much were you paid this week? "))
    print("I will deposit that amount into your account.")
    #the deposit function is passing one argument called amount
    #so we have to fulfill that argument with pay
    savings.deposit(pay)

    #retrieved the balance from the external class
    #display the balance.
    print("your account balance is $", format(savings.get_balance(),',.2f'))

    #Get the amount to withdraw.
    cash = float(input("how much would you like to withdraw? "))
    print("I will withdraw that amount from your account.")
    #calls the withdraw function from the external class
    #and fulfills the one argument that is passed with cash
    savings.withdraw(cash)

    #retrieved the blance from the external class
    #display the balance.
    (print("your account balance is $", format(savings.get_balance(),',.2f')))

main()