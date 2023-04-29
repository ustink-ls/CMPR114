#Project #1 (B): this example is using the super keyword 
#to inherit attributes and arguments.

#Challenge Exercise #2: Continuing from project #1 (B) add to
#the super constructor and add the address, city, 
#state, and zip code) for the Student and Teacher. 

class person:
    #__init__ method initializes object attributes so they can be
    #shared throughout the program
    def __init__(self,name,age, address, city, state, zipCode):
        self.name = name
        self.age = age
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode

#the student class in inheriting from the person class
class Student(person):
    def __init__(self,name,age,studentID,GPA, address, city,state, zipCode):

        #The super keyword is calling the suepr class
        #which is the person class and passing name, and age

        super().__init__(name,age,address, city, state, zipCode)

        self.studentID= studentID
        self.GPA = GPA

class Teacher(person):
    def __init__(self,name,age,TeacherID,ClassTeaching, address, city, state,zipCode):
        super().__init__(name,age, address, city, state, zipCode)
        self.TeacherID = TeacherID
        self.ClassTeaching = ClassTeaching

student = Student('Jane Doe', 25, 777, 3.8, '123 shire', 'Anaheim','CA', 92709)
print("Student Name: ", student.name)
print("Student Age: ", student.age)
print("Student ID: ", student.studentID)
print("Student GPA: ", student.GPA)
print("Student address: ", student.address)
print("Student city: ", student.city)
print("Student state: ", student.state)
print("Student zip code: ", student.zipCode)

print("\n")

teacher = Teacher('Ms. Cantor', 45, 7, "Python", "456 Melrose", "Seattle", "Washington", 83749)
print("Teacher Name: ", teacher.name)
print("Teacher Age: ", teacher.age)
print("Teacher ID: ", teacher.TeacherID)
print("Teacher Course: ", teacher.ClassTeaching)
print("Student address: ", teacher.address)
print("Student city: ", teacher.city)
print("Student state: ", teacher.state)
print("Student zip code: ", teacher.zipCode)
