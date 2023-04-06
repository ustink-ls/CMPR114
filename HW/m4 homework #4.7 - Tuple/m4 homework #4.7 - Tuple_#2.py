#2 Find the largest number in this Tuple 
#test_tup = (15, 20, 123, 47, 26, 81)

#assign values to tupple
test_tup = (15, 20, 123, 47, 26, 81)

#Another way that you can access the individual elements in a 
#list is with an index. Each element in a list has an index 
#that specifies its position in the list. Indexing starts at 0, 
#so the index of the first element is 0, the index of the second 
#element is 1, and so forth. The index of the last element in a 
#list is 1 less than the number of elements in the list.
index = 0

#Use a while loop to print the values listed in the tupple.
print('Here is the list of numbers in the tuple:')
#Python has a built-in function named len that returns the 
#length of a sequence, such as a list.
while index < len(test_tup):
    print(test_tup[index]) 
    index += 1

#The max function accepts a sequence, such as a list, 
#as an argument and returns the item that has the highest 
#value in the sequence.
print(f'The largest number in this tuple is {max(test_tup)}.')
