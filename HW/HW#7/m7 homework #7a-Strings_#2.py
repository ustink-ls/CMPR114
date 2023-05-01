#2. Most Frequent Character
#Write a program that lets the user enter a string and displays 
#the character that appears most frequently in the string.

#Use the collections module.
import collections

#Get the user's input.
user_input = input('Enter a string: ')

#From the collections module, use the counter tool, and then
#most_common([n]) object, which returns a list of the n most 
#common elements.
print(collections.Counter(user_input).most_common(1)[0])
