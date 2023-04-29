#Inheritance allows a new class to extend an existing class. 
#The new class inherits the members of the class it extends. 
#Inheritance allows to inheritance of attributes and methods 
#from a parent class to a child class or classes.

#Challenge Exercise #1: continuing from project #1 (A), add 
#the 3rd animal and print screen the results with the code below:

class AnimalType:
    #self represents the instance of the class. by using the "self"
    #we can access the attributes and methods of the class in python.
    #it binds the attributes with the given arguments.
    def eats(self):
        print ("This animal likes to eat?")

class rabbits(AnimalType):
    def munch(self):
        print ("carrots")
        print("answer: rabbit\n")

class birds(rabbits):
    def munch1(self):
        print ("seeds")
        print("answer: bird\n")

class cats(birds):
    def munch2(self):
        print ("fish")
        print("answer: cat\n")

RabbitObject = rabbits()
RabbitObject. eats()
RabbitObject.munch()

#here we have the Bird Object inheriting from two different
#classes
BirdObject = AnimalType()
BirdObject = birds()
BirdObject.eats()
BirdObject.munch1()

#here we have the Cat Object inheriting from two different
#classes
CatObject = AnimalType()
CatObject = cats()
CatObject.eats()
CatObject.munch2()




