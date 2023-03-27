#3. Write code that does the following: opens an output file with
#the file name number_list.txt, uses a loop to write the numbers
#1 through 100 to the file, then closes the file.

#open a file called things.txt
infile = open("/Users/leslyesirena/Desktop/Python/number_list.txt","w")

#write the numbers 1-100 as a list on the file.
for counter in range (1, 101):
    numbers = int(counter)
    #write the numbers list to the file.
    infile.write(str(numbers) + '\n')

#close the file.
infile.close()

#Print once the data is in the file.
print('Data is written into file.')

