#This program asks the user to enter sales with comission 4 times, 
#and on the fourth time, will sum the sales with commission.

#Create a variable to control the loop.
max_input = 4

#Initialize an accumulator variable.
total = 0.0

#Explain what this program does.
print ('This program calculates the sum of ', end='')
print (f'{max_input} sales with commssions you will enter.')

#Get the user's 4 sales with commssions and sum them.
for counter in range(max_input):
    sales = float(input('Enter the amount of sales with commissions: '))
    total = total + sales

#Display the total of the sales with commissions.
print(f'The total is {total}.')

