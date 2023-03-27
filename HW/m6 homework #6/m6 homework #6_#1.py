#1. Write a program that opens an output file with the filename
#things.txt, writes the name of an animal, a fruit, and a country
#to the file on the separate lines, then closes the file.


#open a file called things.txt
outfile = open("/Users/leslyesirena/Desktop/Python/things.txt","w")

#write the names of an animal,fruit, country to the file.
outfile.write("The name of an animal is cat." + '\n')
outfile.write("The name of a fruit is apple." + '\n')
outfile.write("The name of a country is Kenya." + '\n')

#print data recorded on the console.
print('data recorded')

#close the file.
outfile.close()


