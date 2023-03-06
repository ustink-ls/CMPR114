#This program will ask the user to enter a series of positive
#numbers. The user should enter a negative number to signal 
#the end of the series. After all the positive numbers have 
#been entered, the program should display their sum.

#Initialize an accumulator variable.
sum = 0.0

#Explain what this program does.
print ('This program calculates the sum of the positive numbers ')
print ('you enter. Enter a negative number to end the series.\n')

#Get the user's numbers.
positive_number = int(input('Enter a positive number: '))

#Conditioned series.
while positive_number >= 0:
   sum += positive_number
   positive_number = int(input('Enter a positive number: '))
   if positive_number < 0:
        print('You have ended the series.')
        print(f'The sum is {sum}.')



