#2. Employee Class
#Write a class named Employee that holds the following data 
#about an employee in attributes: name, ID number, department, 
#and job title.
#Once you have written the class, write a program that creates 
#three Employee objects to hold the following data (assigned
#to each employee object):
#The program should store this data in the three objects, 
#then display the data for each employee on the screen.

class Employee:
    #the keyword(self)
    #it is used to access variables that belong to the class.
    def GetInformation(self):
        print("name: " + self.name)
        print("ID number: " + self.ID_number)
        print("department: " + self.department)
        print("job title: " + self.job_title)

#Employee1 Object
Employee1 = Employee()
Employee1.name = "Susan Meyers"
Employee1.ID_number = "47899"
Employee1.department = "Accounting"
Employee1.job_title = "Vice President\n"

#Employee2 Object
Employee2 = Employee()
Employee2.name = "Mark Jones"
Employee2.ID_number = "39199"
Employee2.department = "IT"
Employee2.job_title = "Programmer\n"

#Employee3 Object
Employee3 = Employee()
Employee3.name = "Joy Rogers"
Employee3.ID_number = "81774"
Employee3.department = "Manufacturing"
Employee3.job_title = "Engineer\n"

#display the results.
print('Employee 1:')
Employee1.GetInformation()
print('Employee 2:')
Employee2.GetInformation()
print('Employee 3:')
Employee3.GetInformation()