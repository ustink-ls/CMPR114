#This program asks the user to enter the number of packages purchased.
#The program then displays the amount of the discount (if any) and
#the total amount of the purchase after the discount.

#Named constants to represent the quantity thresholds.
price = 99

#Named constants to represent the quantity thresholds.
quantity1 = 10
quantity2 = 20
quantity3 = 50
quantity4 = 100

#Get the number of packages purchased from the user.
packages = float(input('Enter the number of packages purchased: '))

#Calculate discounts based on number of packages.
totalpurchase = packages * price

#Calculate discounts based on number of packages.
discount1 = totalpurchase * .10
discount2 = totalpurchase * .20
discount3 = totalpurchase * .30
discount4 = totalpurchase * .40

#Determine which quarter the month falls under.
if packages >= quantity1 and packages < quantity2:
    print('Your discount amount is $', discount1, '.') 
    print('Your total purchase amount is $', totalpurchase - discount1, '.')
elif packages >= quantity2 and packages < quantity3:
    print('Your discount amount is $', discount2, '.') 
    print('Your total purchase amount is $', totalpurchase - discount2, '.')
elif packages >= quantity3 and packages < quantity4:
    print('Your discount amount is $', discount3, '.') 
    print('Your total purchase amount is $', totalpurchase - discount3, '.')
elif packages >= quantity3:
    print('Your discount amount is $', discount4, '.') 
    print('Your total purchase amount is $', totalpurchase - discount4, '.')
else:
    print('Discount is not applicalbe. Your total purchase amount is ', totalpurchase, '.')