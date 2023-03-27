#4. In this chapters source code folder, you will find a text file
#named numbers.txt. Write a prgoram that reads all of the numbers
#in the file and calculates them.

#open a file called things.txt
numbers_file = open("/Users/leslyesirena/Desktop/Python/numbers.txt","r")

#Initialize an accumulator variable.
total = 0

#Initialize a count variable.
count = 0

#read the file's contents and print them.
print('Here are the numbers from the file: \n')

#Calculate the total of the numbers from the file.
#use a for loop.
for line in numbers_file:
    #convert a line to a float.
    number = float(line)
    #add 1 to the count variable
    count += 1
    #display the numbers in the file
    print('Number ',count, ':', number)
    #add the number to total
    total += number

#close the file.
numbers_file.close()

#Display the total.
print (f'\nThe total is {total}.')




