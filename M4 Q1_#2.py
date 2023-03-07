#Create a variable to control the loop.
max_input = 4

#Initialize an accumulator variable.
sum = 0.0

#Explain what this program does.
print ('This program calculates the sum of ', end='')
print (f'{max_input} scores you will enter.')

#Get the user's 4 scores and sum/average them.
for counter in range(max_input):
    scores = float(input('Enter a score: '))
    sum = sum + scores
    average = sum / max_input

#Display the total/average.
print(f'The total is {sum}.')
print(f'The average is {average}.')