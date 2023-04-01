#Challenge Exercise #4: continuing with project #6, 
#the total function, output the numbers list to a text file.

#Project #6: This program will demonstrate how to insert 
#and remove items in a list, and total and average number of 
#items in a list.

def main():
    names = ['Howard', 'Jamie', 'Jill']
    #element    0       1       2

    print('The list before the insert or remove: ')
    print(names)

    NameRemove = input('Enter the name to remvoe: ')

    #insert the new name at element 0, moving or shifting
    #element 0 to 1
    names.insert(0,'Joe')
    #removes the name from the list
    names.remove(NameRemove)
    print('The list after the insert: ')

    print(names)

main()

def total():
    #open the text file
    outfile = open("/Users/leslyesirena/Desktop/Python/m7 Class exercise #7a Sets Dictionaries_#4_textfile.txt","w")

    numbers = [1,2,3,4,5,6,7,8,9,10]
    sum = 0
    for value in numbers:
        #total the numbers in the list
        sum += value
    
    #the lens function returns the number of items in the list
    average = sum/len(numbers)
    print('The total is ',sum,'. The average is ', average,'.')

    #write the numbers list to the file.
    outfile.writelines(str(numbers) + '\n')
    outfile.write("The total is "+str(sum)+". The average is "+ str(average) + '.\n')
    
    #close the file.
    outfile.close()

    #Print once the data is in the file.
    print('Data is written into file.')

total()