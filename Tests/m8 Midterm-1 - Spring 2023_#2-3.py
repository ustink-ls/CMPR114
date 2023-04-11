#Project #2 (based on Chapter 6 Files and Exceptions)
#Write a program that will read the coffee text file 
#(please download from module 8 midterm). Display the entire
#file on the console.

def ReadCoffee():
    #open a file called Coffee.txt and read it.
    coffee_file = open("/Users/leslyesirena/Desktop/Python/Coffee.txt","r")

    print('Here is the data from the Coffee.txt file: \n')

    #Read the file's contents. 
    file_contents = coffee_file.read()

    #close the file.
    coffee_file.close()

    # Print the data that was read into memory.
    print(file_contents)
ReadCoffee()

#Write a program that will write to the coffee text file. 
#Ask user to enter their favorite coffee brand, with the prod number 99-8888, 
#and price $9.88. Verify by reading the file content.

def WriteCoffee():
    coffee = (input('\nEnter your favorite coffee brand: '))
    prod_number = (input('\nEnter the prod number 99-8888: '))
    price_number = (input('\nEnter the price $9.88: '))
    coffee_file = open("/Users/leslyesirena/Desktop/Python/Coffee.txt","a")

    # Write the data to the file.
    coffee_file.write("\nHere is the user's coffee data:\n")
    coffee_file.write(coffee + '\n')
    coffee_file.write(prod_number + '\n')
    coffee_file.write(price_number + '\n')

    #close the file.
    coffee_file.close()

    print("user's coffee data recorded. \n")

WriteCoffee()

