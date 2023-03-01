#This program will ask the user to enter 4 sets of temps under 
#102.5 and then get the sum and average of the four temps when 
#the user enter a temp over 102.5.

#Create a variable to control the loop.
min_input = 1
max_input = 4

#Create a named constant (a variable that does not change.)
max_temp = 102.5

#Initialize an accumulator variable.
total = 0.0

#Explain what this program does.
print ('This program calculates the sum and average of ', end='')
print (f'{max_input} temperatures you will enter.')

#Get the user's temperatures and sum/average them.
while min_input <= max_input:
    temperature = float(input('Enter a temperature: '))
    total += temperature
    average = total/max_input
    min_input +=1

#Get the user's 4 conditional termperatures and sum/average them.
while temperature < max_temp:
    print ('The temperature is too low.')
    temperature = float(input(f'Enter a temperature above {max_temp}: '))
    
#Display the total of the temperatures.
print(f'The total is {total}.')

#Display the average of the temperatures.
print(f'The average is {average}.')

