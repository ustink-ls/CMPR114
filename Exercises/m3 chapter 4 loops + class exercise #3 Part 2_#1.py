#This program calculates the sum of a series of numbers
#entered by the user.

#Create a variable to control the loop.
max_input = 5

#Initialize an accumulator variable.
total = 0.0

#Explain what this program does.
print ('This program calculates the sum and average of ', end='')
print (f'{max_input} numbers you will enter.')

#Get the user's temperatures and sum/average them.
for counter in range(max_input):
    number = float(input('Enter a number: '))
    total = total + number
    average = total/max_input

#Display the total of the temperatures.
print(f'The total is {total}.')

#Display the average of the temperatures.
print(f'The average is {average}.')

