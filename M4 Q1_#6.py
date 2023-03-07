#Create a variable to control the loop.
min_input = 1
max_input = 4

#Initialize an accumulator variable.
total = 0.0

#Explain what this program does.
print ('This program calculates the sum and average of ', end='')
print (f'{max_input} test scores you will enter.')

#Get the user's 4 test scores and sum/average them.
while min_input <= max_input:
    score = float(input('Enter your score: '))
    total += score
    average = total/max_input
    min_input +=1

#Display the average of the temperatures.
print(f'Your average is {average}.')

#Assign the letter grade.
if average >= 90 and average <= 100:
    print('You received an A.') 
elif average >= 80 and average < 90:
        print('You received a B.')
elif average >= 70 and average < 80:
        print('You received a C.')
elif average >= 60 and average < 70:
        print('You received a D.')
elif average >= 0 and average < 60:
        print('You received an F.')
else:
    print("The average is greater than 100. Re-enter 4 scores.")

