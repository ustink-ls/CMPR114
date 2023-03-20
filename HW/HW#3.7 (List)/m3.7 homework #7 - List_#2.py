#Number analysis program
#Design a program that asks the user to enter a series of 20 numbers.
#The program should store the number sin a list then display the
#following data:
#   • The lowest number in the list
#   • The highest number in the list
#   • The total of the numbers in the list
#   • The average of the numbers in the list

#Set a variable for the max numbers that can be entered by the user.
maximum = 20

#Initialize an empty list to hold the numbers.
numbers_list = []

#Explain what we are doing.
print('This program displays the lowest number, the highest ', end='')
print('number, the total, and the average of the ', end='')
print(f'{maximum} numbers you will enter.')

#For loop to request 20 inputs from user.
for counter in range(maximum):
    number = int(input('Enter a number: '))
    #append each value to the list
    numbers_list.append(number)

#Display the results.
print (f'\nYour lowest number is {min(numbers_list)}.')
print (f'Your highest number is {max(numbers_list)}.')
print(f'The total is {sum(numbers_list)}.')
print(f'The average is {sum(numbers_list)/len(numbers_list)}.')

