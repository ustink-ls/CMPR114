#Creating Lists and Tuples
   
#The get_scores function gets a series of test scores from
#the user and stores them in a list. A reference to the list
#is returned.
def get_scores():
    #create an empty list.
    test_scores = []

    #create a variable to control the loop.
    again = 'y'

    #get the scores from the user and add them to the list.
    while again == 'y':
        #get a score and add it to the list.
        value = float (input('Enter a test score: '))
        test_scores.append(value)

        #want to do this again?
        print ('Do you want to add another score? ')
        again = input ('y = yes, anything else = no: ')
        print()
    
    #return the list.
    return test_scores

#The get_total function accepts a list as an argument and returns
#the total of the values in the list.
def get_total(value_list):
    #create a variable to use as an accumulator.
    total = 0

    #calculate the total of the list elements.
    for num in value_list:
        total += num
    
    #return the total
    return total

def main():
    #call the main function.
    if __name__ == '__main__':
        main()
