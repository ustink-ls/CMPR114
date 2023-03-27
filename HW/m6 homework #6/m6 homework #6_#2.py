#2. Write a program that opens the things.txt file created by the 
#program in Algorithm Workbench 1, reads all of the data from the
#file before closing it, and then displays the data from the file.

#open a file called things.txt
infile = open("/Users/leslyesirena/Desktop/Python/things.txt","r")

#read the file's contents.
file_contents = infile.read()

#close the file.
infile.close()

#Print the data that was read into memory.
print(file_contents)
