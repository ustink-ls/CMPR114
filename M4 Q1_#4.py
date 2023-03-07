#Named constants to represent the commission thresholds.
Tier1 = 0
Tier2 = 50000
Tier3 = 70000
Tier4 = 90000
Tier5 = 100000

#Get the sales amount from the user.
sales = int(input('Enter your sales amount: '))

#Determine the user's commission based on the sales amount.
if sales >= Tier1 and sales < Tier2:
    print('You do not qualify for a commission.') 
elif sales >= Tier2 and sales < Tier3:
    commission = sales * .1
    print('Your commission is ', commission, '.')
elif sales >= Tier3 and sales < Tier4:
    commission = sales * .2
    print('Your commission is ', commission, '.')
elif sales >= Tier4 and sales <= Tier5:
    commission = sales * .1
    print('Your commission is ', commission, '.')
elif sales > Tier5:
    print('You do not qualify for a commission.')