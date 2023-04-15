#Challenge Exercise #2: continuing with project #2, read the 
#data using the print statement.

def WriteNumbers():
    
    outfile = open('/Users/leslyesirena/Desktop/Python/m6 chapter 6 Files and Exceptions GUI Interfaces + class exercise #5_#2.txt','a')

    num1 = int(input('enter #1 '))
    num2 = int(input('enter #2 '))
    num3 = int(input('enter #3 '))

    sum = num1 + num2 + num3
    avg = sum/3

    outfile.write("The 1st number is " + str(num1) + '\n')
    outfile.write("The 2nd number is " + str(num2) + '\n')
    outfile.write("The 3rd number is " + str(num3) + '\n')
    outfile.write("The avg number is " + str(avg) + '\n')
    outfile.write("The total number is " + str(sum) + '\n')

    print('data recorded')

WriteNumbers()