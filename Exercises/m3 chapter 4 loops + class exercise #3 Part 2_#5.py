#Lap Times
#Write a program that asks the user to enter the number of times
#they have run around a racetrack, and then uses a loop to prompt
#them to enter the lap time for each of their laps. When the
#loop finishes, the program should display the time of their
#fastest lap, the time of their slowest lap, and their average
#lap time.

#Ask the user the number of times they have run around a racetrack.
num_laps = int(input('Enter the number of times you ran around the racetrack: '))

#variables
fastest = None
slowest = None

#Initializer
total = 0

#For loop to grab the number of times. Conditions and total calculated.
for counter in range(num_laps):
    lap_time = int(input('\nEnter the lap time in minutes for each lap: '))
    if num_laps <= 0:
        print ('Invalid input. Number of laps run must be greater than 0.')
    elif fastest is None:
        fastest = lap_time
        slowest = lap_time
    elif lap_time < fastest:
        fastest = lap_time
    elif lap_time > slowest:
        slowest = lap_time
    total = total + lap_time
    average = total/num_laps

#Display the results.
print (f'\nYour fastest lap time is {fastest} minutes.')
print (f'Your slowest lap time is {slowest} minutes.')
print (f'Your average lap time is {average} minutes.')

