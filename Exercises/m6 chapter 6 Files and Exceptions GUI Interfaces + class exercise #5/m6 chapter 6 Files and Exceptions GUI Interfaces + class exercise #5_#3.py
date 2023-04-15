#Challenge Exercise #3:  continuing from project #3, write a 
#program that will ask the user to enter the sales with salary, 
#and if the total sales are greater than 1000 add 10% commission 
#to the salary write and read the data using the print statement.

def sales():
    num_days = int(input('Enter the days of sales: '))
    sales_file = open('/Users/leslyesirena/Desktop/Python/m6 chapter 6 Files and Exceptions GUI Interfaces + class exercise #5_#3.txt','w')

    for count in range (1, num_days +1):
        sales = float(input('enter the sales for day #' + str(count) + ": "))
        sales_file.write(str(sales) + '\n')
    
    sales_file.close()
    print('sales recorded \n')

sales()

def ReadSales():
    sales_file = open('/Users/leslyesirena/Desktop/Python/m6 chapter 6 Files and Exceptions GUI Interfaces + class exercise #5_#3.txt','r')
    line = sales_file.readline()

    while line != '':
        amount = float(line)
        print (format(amount, '.2f'))
        line = sales_file.readline()
    
    sales_file.close()

ReadSales()