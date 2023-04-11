#Create a 2-D list with the numbers 1-10 and retrieve 
#the lucky number 7. Below is an example of a 2-d list.

#assign values to tupple
tup = ([1, 2, 3], [4, 5, 6], [7, 8, 9, 10])

# Create a variable to use as an accumulator. 
total = 0

# Display the list elements. 
print('Here is the list of numbers in the tuple:')
for row in tup:
    for element in row:
        total += element
        print(element)

lucky_number = [element[0] for element in tup if element[0]==7]

print(f'Here is lucky number: {lucky_number}.')
