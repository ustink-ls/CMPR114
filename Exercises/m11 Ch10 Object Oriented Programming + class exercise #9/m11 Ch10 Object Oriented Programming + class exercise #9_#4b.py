#The second class

#import the other class file that contains the data. Since I cannot 
#import a file with a long file name that includes spaces, use 
#the below import. Or name module something simple like class7, 
#and then use import class7.
import sys
sys.path.append("/Users/leslyesirena/Desktop/Python/m11 Ch10 Object Oriented Programming + class exercise #9_#4a")
class7 = __import__("m11 Ch10 Object Oriented Programming + class exercise #9_#4a")

#start the main function
def main():

    name = (input("enter the name: "))
    address = (input("enter the address: "))
    phone = (input("enter the phone: "))
    city = (input("enter the city: "))
    zipCode = (input("enter the zip code: "))
    age = (input("enter the age: "))

    #calling class7 or the systen file, then the name of the
    #class, then the name of the function which equals to the 
    #input variables
    v1 = class7.Customer.set_name = name
    v2 = class7.Customer.set_address = address
    v3 = class7.Customer.set_phone = phone
    v4 = class7.Customer.set_city = city
    v5 = class7.Customer.set_zipCode = zipCode
    v6 = class7.Customer.set_age = age

    print("\nHello " + v1 + 
          ". Your address is " + v2 + 
          ", your phone numbers is " + v3 + 
          ", your city is " + v4 +
          ", your zip code is " + v5 +
          ", and your age is " + v6 + ".")

main()