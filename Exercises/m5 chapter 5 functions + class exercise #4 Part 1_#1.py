#This program demonstrates two functions that have local variables
#with the same name.

def main():
    #ask user for input.
    texas_birds = float (input('Enter the number of birds in Texas: '))
    california_birds = float (input('Enter the number of birds in California: '))
    #call the texas function and pass it
    texas(texas_birds)
    #call the california function
    california(california_birds)

#Definition of the texas function. It creates a local variable
#named birds.
def texas(birds):
    print (f'Texas has {birds} birds.')

#Definition of the california function. It also creates a local
#variable named birds.
def california(birds):
    print (f'California has {birds} birds.')

main()