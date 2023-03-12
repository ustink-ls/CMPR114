#RAINFALL APP: Design a program that lets the user to enter the total rainfall for each of the 12 months into a list. 
#The program should calculate and display the total rainfall for the year, the average monthly rainfall, the months 
#with the highest and lowest amounts of rainfall. Plus output the results into a text file as well as the console.

#This program will ask the user for the monthly rainfall to get
#the total and store it in a list.

def main():
    month_of_the_year = ['January','February','March','April','May','June','July','August','September','October','November','December']
    monthly_rain = []
    print ('Enter the rainfall for each month. \n')

    index = 0
    for i in month_of_the_year: #loop to ask the user's input for each month in the month_of_the_year list
        rain = float(input(f'Enter the amount of rain for {i}: '))
        monthly_rain.insert(index,rain) #insert the user's monthly rain input starting at element 0
        index +=1

    total_rain = total (monthly_rain) #calls the total function
    average_rain = total_rain/len(monthly_rain)
    less_rain = min (monthly_rain)
    less_rain_index = monthly_rain.index(less_rain)
    most_rain = max(monthly_rain)
    most_rain_index = monthly_rain.index(most_rain)

    print (f'The total rain in the year was: {total_rain}')
    print (f'The average rain in each month is: {average_rain:.2f}')
    print (f'The month with the lowest rain was {month_of_the_year[less_rain_index]} with {less_rain} inches of rain.') #this needs to be updated to return all the months that have the same amount of rain
    print (f'The month with the highest rain was {month_of_the_year[most_rain_index]} with {most_rain} inches of rain.') #this needs to be updated to return all the months that have the same amount of rain

    write ('/Users/leslyesirena/Desktop/Working File/Python/HW/yearly_rain.txt', monthly_rain, total_rain, month_of_the_year)

def total (numbers):
    sum = 0
    for value in numbers:
        sum += int(value or 0)
    return sum

def write (name, monthly_rain, total, month_of_the_year):
    index = 0
    output = open (name, 'w')
    for rain in monthly_rain:
        output.writelines (f'{month_of_the_year[index]}: {rain} inches \n')
        index +=1
    output.writelines (f'Total rain: {total:.2f} inches \n')
    output.writelines (f'The average rain on this year was {total/len(month_of_the_year):.2f} inches. \n')
    less_rain = min (monthly_rain)
    less_rain_index = monthly_rain.index(less_rain)
    most_rain = max (monthly_rain)
    most_rain_index = monthly_rain.index(most_rain)
    output.writelines (f'The month with the lowest rain was {month_of_the_year[less_rain_index]} with {less_rain} inches of rain. \n')
    output.writelines (f'The month with the highest rain was {month_of_the_year[most_rain_index]} with {most_rain} inches of rain. \n')

main()
