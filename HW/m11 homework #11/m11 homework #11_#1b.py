#1b. Pet Class

#Once you have written the class, write a program that creates an object of the class and 
#prompts the user to enter the name, type, and age of his or her pet. This data should be 
#stored as the object’s attributes. Use the object’s accessor methods to retrieve the pet’s
#name, type, and age and display this data on the screen.

#import the other class file that contains the data. Since I cannot 
#import a file with a long file name that includes spaces, use 
#the below import. Or name module something simple like classPet, 
#and then assign import to classPet.
import sys
sys.path.append("/Users/leslyesirena/Desktop/Python/m11 homework #11_#1a")
classPet = __import__("m11 homework #11_#1a")

#start the main function
def main():

    name = (input("enter the name of your pet: "))
    animal_type = (input("what type of pet do you have: "))
    age = (input("enter your pet's age: "))

    #calling classPet or the system file, then the name of the
    #class, then the name of the function which equals to the 
    #input variables
    p1 = classPet.Pet.set_name = name
    p2 = classPet.Pet.set_animal_type = animal_type
    p3 = classPet.Pet.set_age = age

    #Display the results.
    print("\n")
    print("Your pet's name is: ", p1)
    print("The type of pet you have is: ", p2)
    print("Your pet's age is: ", p3)

main()