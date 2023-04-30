#import the other class file that contains the data. Since I cannot 
#import a file with a long file name that includes spaces, use 
#the below import. Or name module something simple like insects, 
#and then assign import to insects.
import sys
sys.path.append("/Users/leslyesirena/Desktop/Python/m13 homework #13_#2a")
#pc stands for Person/Customer
pc = __import__("m13 homework #13_#2a")

#start the main function
def main():
    #Get the person's name, address, and telphone number.
    print('Enter the following Person data: ') 
    name = input('Name: ')
    address = input('Address: ')
    telephone_number = input("Telephone Number: ")
    
    #Create a Person object.
    person = pc.Person(name, address, telephone_number)

    #Get the Customer's number, mailing list.
    print('Enter the following Customer data: ') 
    customer_number = float(input('Customer number: '))
    #convert input to lowercase
    mailing_list = input("Do you wish to be on the mailing list? (yes/no): ").lower()  
    if mailing_list == "yes":
        print("Great! You're on the mailing list.")
        want_mailing_list = True
    elif mailing_list == "no":
        print("Okay, you're not on the mailing list.")
        want_mailing_list = False
    else:
        print("Sorry, I didn't understand your answer.")
        want_mailing_list= False

    #Create a Customer object.
    customer = pc.Customer(name, address, telephone_number, customer_number, mailing_list)

    #Display the results of Person.
    print("\nHere is the date you entered:")
    print("Name: ", person.get_name())
    print("Addres: ", person.get_address())
    print("Telephone Number: ", person.get_telephone_number())
    #Display the results of Customer
    print("Customer Number: ", customer.get_customer_number())
    print("Mailing List: ", customer.get_mailing_list())

main()