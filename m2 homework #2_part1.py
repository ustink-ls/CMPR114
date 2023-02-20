#This program asks the user for a month as a number between 1 and 12. 
#The program should display a message indicating whether the month 
#is in the first quarter, the second quarter, the third quarter, or 
#the fourth quarter of the year.

#Named constants to represent the quarter thresholds.
Q0 = 0
Q1 = 3
Q2 = 6
Q3 = 9
Q4 = 12

#Get the month as a number between 1 and 12 from the user.
month = int(input('Enter a number between 1 and 12: '))

#Determine which quarter the month falls under.
if month <= Q0:
    print('Error! The number is not between 1 and 12.') 
elif month <= Q1:
    print('The month is in the first quarter.')
elif month <= Q2:
    print('The month is in the second quarter.')
elif month <= Q3:
    print('The month is in the third quarter.')
elif month <= Q4:
    print('The month is in the fourth quarter.')
else:
    print('Error! The number is not between 1 and 12.')