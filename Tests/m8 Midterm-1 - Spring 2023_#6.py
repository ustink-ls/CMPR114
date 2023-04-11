#In the 1-D list retrieve only the lucky number 27 and print it.

#assign values to tupple
tup = (20,21,22,23,24,25,26,27,28,29,30)

#Another way that you can access the individual elements in a 
#list is with an index. Each element in a list has an index 
#that specifies its position in the list. Indexing starts at 0, 
#so the index of the first element is 0, the index of the second 
#element is 1, and so forth. The index of the last element in a 
#list is 1 less than the number of elements in the list.
index = 0

#Create a variable that will hold the sum.
sum = 0

#Use a while loop to print a list of the values in the tupple.
print('Here is the list of numbers in the tuple:')
#Python has a built-in function named len that returns the 
#length of a sequence, such as a list.
while index < len(tup):
    print(tup[index]) 
    index += 1

print(f'Here is lucky number: {tup[7]}.')
