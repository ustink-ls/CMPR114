#Stadium Seating
#There are three seating categories at a stadium. Class A seats
#cost #20, Class B seats cost $15, and Class C seats cost $10.
#Write a program that asks how many tickets for each class of seats
#were sold, then displays the amount of income genreated from
#the ticket sales.

def main():
    #Ask the user how many tickets were sold for each class.
    classA = float(input('Enter the number of Class A seat tickets sold: '))
    classB = float(input('Enter the number of Class B seat tickets sold: '))
    classC = float(input('Enter the number of Class C seat tickets sold: '))
    print('\n')
    #Call the income_per_class function.
    income_per_class(classA,classB,classC)

#The income_per_class function calculates the income  for each
#class from the user's inputs.
def income_per_class(classA,classB,classC):
    #Calculate the income of each class.
    incomeA = classA * 20
    incomeB = classB * 15
    incomeC = classC * 10
    #This is what will be displayed after the income_per_class function is called
    #in the main function.
    print(f'The income generated from Class A seat ticket sales is ${incomeA:,.2f}.')
    print(f'The income generated from Class B seat ticket sales is ${incomeB:,.2f}.')
    print(f'The income generated from Class C seat ticket sales is ${incomeC:,.2f}.')
    print('\n')
    #Call the total_income function.
    total_income (incomeA, incomeB, incomeC)

#The total_income function calculates the total income based on the total
#income calculated for each class in the income_per_class function.
def total_income (incomeA, incomeB, incomeC):
    #Calculate the total income based on the income calculated for each class.
    incomeTotal = incomeA + incomeB + incomeC
    #This is what will be displayed after the main function calls the income_per_class 
    #function, which then calls the total_income function.
    print(f'The total income generated for all seat ticket sales is ${incomeTotal:,.2f}.')

main()
