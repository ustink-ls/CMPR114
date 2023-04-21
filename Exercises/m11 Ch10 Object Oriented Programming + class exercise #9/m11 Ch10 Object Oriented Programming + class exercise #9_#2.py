#Project #2
#Here we are creating a customized constructor by using the 
#__init__ function and passing three arguments starting with 
#name, classroom, and then course. This is a lot cleaner than 
#project #1 but function or behaves the same way.

#Challenge Exercise #2: Add a second object for Teacher2 and 
#add any teacher name, room #, and course assigned.

class Teacher:
    #using init to create a customized constructor
    #here we have three arguments
    def __init__(self, name, classRoom, course):
        self.name = name
        self.classRoom = classRoom
        self.course = course

    def GetProfessor(self):
        print("Professor name is " + self.name)
        print("Professor assigned class is " + self.classRoom)
        print("Professor is teaching " + self.course)
        print("\n")

#creating the Objects and calling the three arguments
Teacher1= Teacher("Prof. Sim", "A206", "Python Programming")
Teacher2= Teacher("Prof. Jean Valjean", "C908", "French")

#calling the function
Teacher1.GetProfessor()
Teacher2.GetProfessor()