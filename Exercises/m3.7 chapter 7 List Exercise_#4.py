#This program will add to the list and delete from the list.

def main():
    names = ['Howard', 'Jamie', 'Jill']
    #element     0         1        2
    print ('The list before the insert or remove: ')
    print (names)
    
    NameRemove = input ('Enter the name to remove: ')
    names.insert(0,'Joe')#insert the new name at element 0, moving/shifting element 0 to 1
    names.remove(NameRemove)#removes the user's input name from the list
    print (names)
main()

def total():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    sum = 0
    for value in numbers:
        sum+=value #total the numbers in the list
    average = sum/len(numbers)#the len function returns the number of items in the list
    print ('The total is ', sum, '. The average is ', average, '.')
    outfile = open ('/Users/leslyesirena/Desktop/Working File/Python/HW/m3.7 chapter 7 List Exercise_#4_textfile.txt', 'w')
    outfile.write(str(numbers))
    outfile.close()
    print('The numbers list is in a text file now.')
total() 




