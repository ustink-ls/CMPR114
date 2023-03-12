#TOTAL SALES APP: Design a program that asks the user to enter a 
#store’s sales for each day of the week. The amount should be 
#stored in a list. Use loop to calculate the total sales for 
#the week and display the result. Plus output the results into 
#a text file as well as the console.


#This program will ask for the week's sales to get the total and store it in a list.

def main():
    days_in_the_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    week_sales = []
    print ('Enter the sales for the week. \n')

    index = 0 #initialize the accumulator variable
    for i in days_in_the_week: #i counts the elements in the list and determines the max number of the loop.
        sale = float(input(f'Enter the sales for {i}: '))
        week_sales.insert(index,sale)#insert the user's sale at element 0
        index =+ 1 #repeatedly asks user to enter sales until max number of the loop is reached

    total_sales = total(week_sales) #goes to the total function to get the total of user's inputted sales
    print(f'The total sales of the week is ${total_sales:,.2f}')#this is displayed in the console, not text file.
    write('/Users/leslyesirena/Desktop/Working File/Python/HW/week_sales.txt', week_sales, total_sales)#this is displayed in the text file.

def total (numbers): #can't use week_sales variable name again, so numbers variable is used instead
    sum = 0 
    for value in numbers:
        sum += int(value or 0)
    return sum

#this function is the output for the textfile.
def write(name, sales, total):#can't use filename, week_sales, total_sales variables again, so name,sales,totale variable used instead
    output = open (name, 'w')
    for money in sales:
        output.writelines (str(money) + '\n')
    output.writelines(f'Total sales: ${total:,.2f}')

