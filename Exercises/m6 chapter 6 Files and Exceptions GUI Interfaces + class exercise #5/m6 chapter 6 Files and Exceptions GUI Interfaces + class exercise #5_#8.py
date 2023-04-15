#Challenge Exercise #8: create a console application 
#(NO GUI) that will write random numbers from 1-10 
#into a text file and read the contents.

#Python provides several library functions for 
#working with random numbers. These functions are 
#stored in a module named random in the standard 
#library. 
import random

def writeRandomNumbers():
    #Open the file for writing.
    num_file = open('/Users/leslyesirena/Desktop/Python/m6 chapter 6 Files and Exceptions GUI Interfaces + class exercise #5_#8.txt','w')
    num_file.write("Here is the list of random numbers written into the file:\n")

    #run a loop to display 10 random numbers.
    print("Here is the list of random numbers displayed in the console:")
    for number in range(10):
        #print random numbers 1-10
        number = random.randint(1, 10)
        print(number)
        #numbers written to file.
        num_file.write(str(number) + '\n')

    #close the file.
    num_file.close()
    print('Data has been recorded to file.\n')
writeRandomNumbers()


def readRandomNumbers():
    num_file = open('/Users/leslyesirena/Desktop/Python/m6 chapter 6 Files and Exceptions GUI Interfaces + class exercise #5_#8.txt','r')
    line = num_file.readline()

    while line != '':
        number = (line)
        print (number)
        line = num_file.readline()
    
    num_file.close()
readRandomNumbers()