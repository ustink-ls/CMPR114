#4 Sort this Tuple by the list total
#input_tup = ([2, 20], [44, 1], [3, 13])
#sorted_tup should be  ([3, 13], [2, 20], [44, 1])

#assign values to tupple
input_tup = ([2, 20], [44, 1], [3, 13])

#Display the original list. 
print('Original order:', input_tup)

#Sum each tuple using a function.
def total_tup(input_tup):
    return sum(input_tup)

#Create the sorted tup variable, then use the sorted function,
#which calls total_tup function, and sorts the input_tup 
#based on the toal of each tuple.
sorted_tup = sorted(input_tup, key = total_tup)
#Display the sorted list.
print('Sorted order:', sorted_tup)

