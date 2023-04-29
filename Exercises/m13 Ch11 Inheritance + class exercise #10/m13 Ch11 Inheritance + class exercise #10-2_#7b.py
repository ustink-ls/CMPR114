#import the other class file that contains the data. Since I cannot 
#import a file with a long file name that includes spaces, use 
#the below import. Or name module something simple like insects, 
#and then assign import to insects.
import sys
sys.path.append("/Users/leslyesirena/Desktop/Python/m13 Ch11 Inheritance + class exercise #10-2_#7a")
#epw stands for Employee ProductionWorker
epw = __import__("m13 Ch11 Inheritance + class exercise #10-2_#7a")

#start the main function
def main():
    #Get the employee name, number.
    print('Enter the following Employee data: ') 
    name = input('Employee Name: ')
    number = input('Employee Number: ')
    
    #Create an Employee object.
    employee = epw.Employee(name, number)

    #Get the shift, pay.
    print('Enter the following ProductionWorker data: ') 
    shift_number = float(input('Shift number (1 for night shift 2 for night shift): '))
    hourly_pay_rate = float(input('Hourly pay rate: '))

    #Create a ProductionWorker object.
    prodWorker = epw.ProductionWorker(name, number, shift_number, hourly_pay_rate)

    #Display the results of Employee.
    print("\nHere is the date you entered:")
    print("Employee Name: ", employee.get_name())
    print("Number: ", employee.get_number())
    #Display the results of ProductionWorker
    print("Shift Number: ", prodWorker.get_shift_number())
    print("Hourly Pay rate: ", prodWorker.get_hourly_pay_rate())

main()