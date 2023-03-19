#Monthly Slaes Tax
#A retail company must file a monthly sales tax report listing 
#the total sales for the month, and the amount of state and county 
#sales tax collected. The state sales tax rate is 5 percent and 
#the county sales tax rate is 2.5 percent. Write a program that 
#asks the user to enter the total sales for the month. From this 
#figure, the application should calculate and display the following:
#   • The amount of county sales tax
#   • The amount of state sales tax
#   • The total sales tax (county plus state)

def main():
    #Ask the user to enter the total sales for the month.
    total_sales = float(input('Enter the total sales for the month: '))
    print('\n')
    #Call the sales_tax function.
    sales_tax(total_sales)

#The sales_tax function calculates the county/state sales tax based on
#the the user's input for total sales for the month.
def sales_tax(total_sales):
    #Calculate the sales tax for county/state.
    county_rate = .025
    state_rate = .05
    county_sales_tax = total_sales * county_rate
    state_sales_tax = total_sales * state_rate
    #This is what will be displayed after the sales_tax function is 
    #called by the main function.
    print(f'The amount of county sales tax is ${county_sales_tax:,.2f}.')
    print(f'The amount of state sales tax is ${state_sales_tax:,.2f}.')
    print('\n')
    #Call the total_sales_tax function.
    total_sales_tax (county_sales_tax, state_sales_tax)

#The total_sales_tax function calculates the total sales tax based on
#the county/state sales tax calculated in the sales_tax function.
def total_sales_tax (county_sales_tax, state_sales_tax):
    #Calculate the total sales tax based on the county/state
    #sales tax calculated in the sales_tax function.
    salestaxTotal = county_sales_tax + state_sales_tax
    #This is what will be displayed after the main function calls the
    #sales_tax function, which then calls the total_sales_tax function.
    print(f'The total sales tax is ${salestaxTotal:,.2f}.')

main()
