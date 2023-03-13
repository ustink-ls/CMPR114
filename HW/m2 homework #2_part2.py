#This program calculates the number of packages of hot dogs and the
#number of packages of hot dog buns needed for a cookout, with the 
#minimum amount of leftovers.

#Function needed to round minimum numberup.
import math

#Variables.
hotdogs = 10
buns = 8

#Get the number of people attending the cookout from the user:
people = float(input('How many people will attend the cookout? '))

#Get the number of hot dogs each person will be given from the user:
number_hotdogs = float(input('How many hot dogs will each person given? '))

#Calculate the total number of hot dogs required and assign the result to the total_hotdogs variable.
total_hotdogs = (people * number_hotdogs)

#Calculate the minimum number of packages of hot dogs required and assign the result to the min_hotdogs variable.
min_hotdogs = (total_hotdogs / hotdogs)

#Calculate the minimum number of packages of hot dog buns required and assign the result to the min_buns variable.
min_buns = (total_hotdogs / buns)

#Calculate the leftovers.
leftovers_hotdogs = total_hotdogs % hotdogs
leftovers_buns = total_hotdogs % buns

#Display the results.
print('\n')
print('The minimum number of packages of hot dogs required is ', float(math.ceil(min_hotdogs)))
print('The number of hot dogs that will be leftover is ', leftovers_hotdogs)
print('\n')
print('The minimum number of packages of hot dog buns required is ', float(math.ceil(min_buns)))
print('The number of hot dog buns that will be leftover is ', leftovers_buns)

