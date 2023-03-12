#Challenge Exercise #4: This program continues from project #6
#screenshot. This program deletes the names in the original array 
#and asks user to add their first and last name using a parallel 
#for loops (use two for loops). The first for loop will loop
#through your last name, and the second for loop will print 
#your first name.

#This section of the program demonstrates a simple for loop that
#uses a list of strings.

#Explain what this program does. 
print ('Below is the list of names before adjusting: \n')
for name in ['Winken', 'Blinken', 'Nod']:
    print(name)

#Ask user to input their first and last name.
print ('\n')
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

#display the updated list.
print ('\n')
print ('Your full name is ', first_name, last_name)

        
