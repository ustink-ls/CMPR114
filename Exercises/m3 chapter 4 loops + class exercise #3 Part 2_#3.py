#A bug collector collects bugs every day for five days.
#Write a program that keeps a running total of the number
#of bugs collected for each day, and when the loop is finished,
#the program should display the total number of bugs collected.

def main():
    days_in_the_week = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    week_bugs = []
    print ('Enter the number of bugs collected for every day of the week. \n')

    index = 0 #initialize the accumulator variable
    for i in days_in_the_week: #i counts the elements in the list and determines the max number of the loop.
        bugs = float(input(f'Enter the number of bugs collected for {i}: '))
        week_bugs.insert(index,bugs)#insert the user's bugs at element 0
        index =+ 1 #repeatedly asks user to enter bugs collected until max number of the loop is reached

    total_bugs = total(week_bugs) #goes to the total function to get the total of user's inputted bug collections
    
    print('\nThe total number of bugs collected for the week is', total_bugs,'.')#this is displayed in the console

def total (numbers): #can't use week_bugs variable name again, so numbers variable is used instead
    sum = 0 
    for value in numbers:
        sum += int(value or 0)
    return sum

main()
