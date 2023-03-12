#Project #2 (creating lists, with input values and outputting 
#the list to a text file)

def main1():
    prodNums = ['V475','F987','Q143','R688'] #list of values
    search = input ('Enter a product: ')
    #if statement determines if product # is in the list.
    if search in prodNums:
        print (search, ' was found on the list.')
    else:
        print (search, ' was not found on the list.')
main1()

print("\n")
def main2():
    nameList = []
    again = 'y'
    while again == 'y':
        name = input ('Enter a name: ')
        nameList.append(name) #this appends (adds items to a list) the names in a list format
        print (' do you want to add another name? ')
        again = input ('y = yes, hit any other key for NO ')
        print ()
        print ('Here are the names you entered: ')
        for name in nameList: #loop through each name
            print (name)
        outfile = open ('/Users/leslyesirena/Desktop/Working File/Python/HW/names.txt', 'w')
        outfile.write(str(nameList))
        outfile.close()
        print('recorded the names in the list ')
main2 ()

