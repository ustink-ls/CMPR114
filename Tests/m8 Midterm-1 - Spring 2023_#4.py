#Create a text file that contains your expenses for last 
#month in the following categories: 
#• Rent
#• Gas
#• Food
#• Clothing
#• Car payment
#Write a program to prompt user for each of the 5 categories and 
#write to this text file. 
#You may create and or format text file anyway you wish. 
#Then read and print the content of the file

def WriteFile():
    #Get the user's data.
    print("Enter the amount spent on the following items last month.\n")
    rent = int(input('Rent: '))
    gas = int(input('Gas: '))
    food = int(input('Food: '))
    clothing = int(input('Clothing: '))
    car_payment = int(input('Car Payment: '))

    #Open the file for writing.
    myfile = open('/Users/leslyesirena/Desktop/Python/m8 Midterm-1 - Spring 2023_#4.txt','w')

    #Write the user's data to the file.
    myfile.write("Here are your total expenses for last month:\n")
    myfile.write(f"Rent: {rent} \n")
    myfile.write(f"Gas: {gas} \n")
    myfile.write(f"Food: {food} \n")
    myfile.write(f"Clothing: {clothing} \n")
    myfile.write(f"Car Payment: {car_payment} \n")

    #display a blank line.
    print()

    #close the file.
    myfile.close()
    print('recorded')
WriteFile()

def ReadFile():
    #open the file and read it.
    myfile = open('/Users/leslyesirena/Desktop/Python/m8 Midterm-1 - Spring 2023_#4.txt','r')

    print('Here is the data from the file: \n')

    #Read the file's contents. 
    file_contents = myfile.read()

    #close the file.
    myfile.close()

    # Print the data that was read into memory.
    print(file_contents)

ReadFile()