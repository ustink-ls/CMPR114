#Property Tax
#A county collects property taxes on the assesment value of a
#property, which is 60% of the property's actual value. For example,
#if an acre of land is valued at $10,000.00, it's assessment
#value is $6,000.00. The property tax is then $0.72 for each $100
#of the assessment value. The tax for the acre assessed at $6,000.00
#will be $43.20. Write a program that asks for the actual value
#of a piece of property and displays the assesment value and
#property tax.

def main():
    #Ask the user for the actual value for a piece of property.
    actual_value = float(input('Enter the actual value of a piece of property: '))
    #Call the assessment function.
    assessment(actual_value)

#The assessment function calculates the assessment value based on the user's input
#of the actual value of a piece of property.
def assessment(actual_value):
    #Calculate the assessment value based on the actual value of the property.
    asessement_value = actual_value * .6
    #This is what will be displayed after the assessment function is called
    #in the main function.
    print(f'The assessment value is ${asessement_value:,.2f}.')
    #Call the property function.
    property (asessement_value)

#The property function calculates the property tax based on the assessment value.
def property(assessment_value):
    #Convert property tax of $0.72 per $100 to decimal and assign it
    #to the variable property_unit_tax.
    property_unit_tax = .72 / 100
    #Calculate the property tax based on the asessment value of the property.
    property_tax = assessment_value * property_unit_tax
    #This is what will be displayed after the main function calls the assessment 
    #function, which then calls the proeprty function.
    print(f'The property tax is ${property_tax:,.2f}.')

main()
