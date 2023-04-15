#Challenge Exercise #1: write a program that will ask the user
#to enter the first, last name with the age, and write the 
#contents to a file, and then read from the file.

#Get user's information.
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = input("Enter your age: ")

#Variable is file pointer. Open the file and write the user's inputs into the file.
fileptr = open("/Users/leslyesirena/Desktop/Python/m6 chapter 6 Files and Exceptions GUI Interfaces + class exercise #5_#1.txt", "w")

#write the content to the file.
fileptr.write(f'First name: {firstName}\n')
fileptr.write(f'Last name: {lastName}\n')
fileptr.write(f'Age: {age}\n')

#print when the process has completed.
print ('All done')

#close/save the file.
fileptr.close()