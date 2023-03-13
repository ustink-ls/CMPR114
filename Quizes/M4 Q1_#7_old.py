#Initialize an accumulator variable.
sum = 0.0

#Explain what this program does.
print ('This program calculates the sum of the numbers 1-10')

#Get the user's numbers.
positive_number = int(input('Enter a positive number: '))

#Conditioned series.
while positive_number >= 0 and positive_number <= 10:
   sum += positive_number
   positive_number = int(input('Enter a positive number: '))
   if positive_number < 0 or positive_number >10:
        print('You have ended the series.')
        print(f'The sum is {sum}.')