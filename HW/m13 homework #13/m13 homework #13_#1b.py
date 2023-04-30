#import the other class file that contains the data. Since I cannot 
#import a file with a long file name that includes spaces, use 
#the below import. Or name module something simple like insects, 
#and then assign import to insects.
import sys
sys.path.append("/Users/leslyesirena/Desktop/Python/m13 homework #13_#1a")
#epw stands for Employee ShiftSupervisor
ess = __import__("m13 homework #13_#1a")

#start the main function
def main():
    #Get the employee name, number.
    print('Enter the following Employee data: ') 
    name = input('Employee Name: ')
    number = input('Employee Number: ')
    
    #Create an Employee object.
    employee = ess.Employee(name, number)

    #Get the annual salary, annual prod bonus.
    print('Enter the following ShiftSupervisor data: ') 
    annual_salary = float(input('Annual Salary: '))
    annual_prod_bonus = float(input('Annual production bonus: '))

    #Create a ShiftSupervisor object.
    shiftSup = ess.ShiftSupervisor(name, number, annual_salary, annual_prod_bonus)

    #Display the results of Employee.
    print("\nHere is the date you entered:")
    print("Employee Name: ", employee.get_name())
    print("Number: ", employee.get_number())
    #Display the results of ShiftSupervisor
    print("Annual Salary: ", shiftSup.get_annual_salary())
    print("Annual Production Bonus: ", shiftSup.get_annual_prod_bonus())

main()