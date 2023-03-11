#Tuples are used to store multiple items in a single variable.

#creating lists
sum = 0
evenNumbers = [2,4,6,8,10]
print (evenNumbers)
#Specifying which number in a list to print using indexes, notice the 0-index pointing to the number 2.
for a in evenNumbers:
    sum+=a #adds the numbers in the list
print (evenNumbers[0])
print ("total sum " + str(sum))
print("\n")

names = ["ian","jason","molly"]
print (names)
print("\n")

info = ["ally",27,1550.87]
print (info)
print("\n")

numbers = [5] * 5 #print the number "5" 5x
print (numbers)
print("\n")

#using a for loop to print numbers in a list.
LoopNumbers =  [1,2,3,4,5,6,7] #1-7 are the elements in this list.
for n in LoopNumbers:
    print (n, end=" ") #end=" " prints the list horizontally.
print("\n")

#using a while loop and incrementing by 1
index = 0 
while index < 4:
    print (LoopNumbers[index], end = " ") #end=" " prints the list horizontally.
    index+=1
print("\n")

#the len function counts how many numbers there are in the list
size = len(LoopNumbers)
print (size)

