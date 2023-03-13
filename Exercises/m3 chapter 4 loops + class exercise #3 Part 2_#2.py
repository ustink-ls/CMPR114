#Write a while loop that lets the user enter a number. The 
#number should be multiplied by 10, and the result assigned to 
#a variable named product. The loop should iterate as long as
#product is lesss than 100.

#This represents the multplier.
multiplier = 10

#Explain the instructions to the user.
print ('Enter a number < 100. If number is > 100, the program will exit.')

#Continue processing as long as the user does not enter a number
#greater than 100.
number = int (input ('Number: '))
while number < 100:
    #Multiply the user's number by the multiplier, 10.
    number_10 = number * multiplier
    #Display the results.
    print ('Your number multiplied by 10 is ',number_10)
    #Get the next number.
    print('Enter the next number < 100 or enter the next number > 100 to exit.')
    number = int (input ('Number: '))
