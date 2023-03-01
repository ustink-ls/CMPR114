#This program places 10 numbers in an array and prints the odd
#and even numbers using a for loop.

#Create variables to control the loop.
min_number = 1
max_number = 10

#Explain what this program does.
print ('I will display the numbers ', end='')
print (f'{min_number} through {max_number}.')

#Place the numbers in an array and print them horizontally.
array = [1,2,3,4,5,6,7,8,9,10]
print (array, end=" ")
print ("\n")

#Use for loop to print odd and even numbers horizontally.
print ('I will display the odd numbers.\n', end='')
for number in array:
    if number % 2!= 0:
        print(number, end=" ")

#Use for loop to print odd and even numbers horizontally.
print ("\n")
print ('I will display the even numbers.\n', end='')
for number in array:
    if number % 2== 0:
        print(number, end=" ")



