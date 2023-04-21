#Challenge Exercise #1: Continuing from project #1, create a 
#third object (Student3) where the user will be able to enter 
#the student’s information.

class Students:
    #the keyword(self)
    #it is used to access variables that belong to the class.
    def GetInformation(self):
        print("student Lastname name is " + self.Lastname)
        print("student Firstname name is " + self.Firstname)
        print("student Address name is " + self.Address)
        print("student City name is " + self.City)
        print("student State name is " + self.State)
        print("student Zipcode name is " + self.Zipcode)

#ask user to enter information for student#3.
ln = input("Enter the student's last name: ")
fn = input("Enter the student's first name: ")
address = input("Enter the student's address: ")
city = input("Enter the student's city: ")
state = input("Enter the student's state: ")
zc = input("Enter the student's zipcode: ")
print("\n")

#creates the Student1 object
Student1 = Students()
Student1.Lastname = "Doe"
Student1.Firstname = "Jane"
Student1.Address = "111 St"
Student1.City = "Santa Ana"
Student1.State = "CA"
Student1.Zipcode = "12345\n"

#creates the Student2 object
Student2 = Students()
Student2.Lastname = "Cantor"
Student2.Firstname = "Mike"
Student2.Address = "222 St"
Student2.City = "Garden Grove"
Student2.State = "CA"
Student2.Zipcode = "67890\n"

#creates the Student3 object
Student3 = Students()
Student3.Lastname = ln
Student3.Firstname = fn
Student3.Address = address
Student3.City = city
Student3.State = state
Student3.Zipcode = zc

#calling the function
Student1.GetInformation()
Student2.GetInformation()
Student3.GetInformation()