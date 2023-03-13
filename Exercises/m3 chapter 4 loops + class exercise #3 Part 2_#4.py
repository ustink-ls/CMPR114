#Calories Burned
#Running on a particular treadmill you burn 4.2 calories per minute.
#Write a program that uses a loop to display the number of calories
#burned after 10, 15, 20, 25, and 30 minutes.

#Create a variable to start/end loop.
start_minutes = 10
end_minutes = 35

#Increment by 5 for the start/end minutes.
increment = 5

#Create a variable for a fixed constant.
calories_burned_per_minute = 4.2

#Explain what this program does.
print ('This program calculates the number of calories burned', end='')
print (' after 10, 15, 20, 25, and 30 minutes.\n')

# Print the table headings.
print('Minutes\t\tCalories Burned')
print('-------------------------------')
#Print the minutes 10 through 30 and their calories burned.
for minutes in range(start_minutes, end_minutes, increment):
    calories_burned = minutes * calories_burned_per_minute
    print(f'{minutes}\t\t{calories_burned:.2f}')
