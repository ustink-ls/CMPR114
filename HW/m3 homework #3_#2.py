#Average Rainfall
#Write a program that uses nested loops to collect data and 
#calculate the average rainfall over a period of years. The 
#program should first ask for the number of years. The outer 
#loop will iterate once for each year. The inner loop will 
#iterate twelve times, once for each month. Each iteration of 
#the inner loop will ask the user for the inches of rainfall for 
#that month. After all iterations, the program should display the 
#number of months, the total inches of rainfall, and the average 
#rainfall per month for the entire period.

#Ask the user for the number of years rainfall data is collected.
years = int(input('How many years of rainfall data was collected? '))
print ('\n')

#Initialize an accumulator variable for rainfall.
total_rainfall= 0.0

#Set a variable for the number of months that can be entered by the user.
months = 12

#For loop to request the yearly input from the user.
for counter in range(years):
    #Nested For loop to request the monthly rainfall data of each year from the user.
    for i in range(months):
        #repeatedly asks user to enter monthly rainfall data collected until max number of the years loop is reached.
        monthly_rainfall = float(input(f'How many inches of rainfall was collected for month {i+1} of year {counter+1}: '))
        total_rainfall = total_rainfall + monthly_rainfall

#calculations
total_months = years * months
average_rainfall = total_rainfall / total_months

#Display the results.
print (f'\nThe total number of months of rainfall data collected is {total_months}.')
print (f'\nThe total inches of rainfall data collected is {total_rainfall}.')
print (f'\nThe average rainfall per month for the entire period is {average_rainfall}.')