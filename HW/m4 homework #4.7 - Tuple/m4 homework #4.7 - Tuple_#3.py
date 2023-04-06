#3 Find the sum of all integer numbers in this Tuple
#test_tup = ([17, 28], [93, 11], [20, 17])


#assign values to tupple
test_tup = ([17, 28], [93, 11], [20, 17])

# Create a variable to use as an accumulator. 
total = 0

# Display the list elements. 
print('Here is the list of numbers in the tuple:')
for row in test_tup:
    for element in row:
        total += element
        print(element)

# Display the total of the list elements.
print(f'The total of the list of numbers in the tuple is {total}.')