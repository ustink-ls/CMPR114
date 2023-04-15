#Challenge Exercise #4: Continuing with project #4, read 
#the content of the employees.txt file.

def Employees():
    #Get the number of employee records to create.
    num_emps = int(input('enter the number of employee records: '))

    #Open the file for writing.
    emp_file = open('/Users/leslyesirena/Desktop/Python/m6 chapter 6 Files and Exceptions GUI Interfaces + class exercise #5_#4.txt','w')

    #Get each employees data and write it to the file.
    for count in range(1, num_emps +1):
        print (f'enter data for employee #{count}')

        name = input("Name: ")
        id_num = input("ID NUMBER: ")
        dept = input ('DEPARTMENT: ')

        emp_file.write(f'{name}\n')
        emp_file.write(f'{id_num}\n')
        emp_file.write(f'{dept}\n')

        #display a blank line.
        print()

    #close the file.
    emp_file.close()
    print('recorded')

Employees()

def ReadEmployees():
    emp_file = open('/Users/leslyesirena/Desktop/Python/m6 chapter 6 Files and Exceptions GUI Interfaces + class exercise #5_#4.txt','r')
    #Read the first line from the file, which is the 
    #name field of the first record.
    name = emp_file.readline()
    
    #If a field was read, continue processing.
    while name != '':
        #Read the ID number field. 
        id_num = emp_file.readline()

        #Read the department field. 
        dept = emp_file.readline()

        #Strip the newlines from the fields. 
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        # Display the record.
        print(f'Name: {name}')
        print(f'ID: {id_num}')
        print(f'Dept: {dept}')
        print()

        #Read the name field of the next record. 
        name = emp_file.readline()
    
    #Close the file.
    emp_file.close()

ReadEmployees()
