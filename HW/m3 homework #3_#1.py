#This program will ask the user to enter the speed for a vehicle (in
#miles per hour) and the number of hours it traeled. It will then
#use a loop to display the distance the vehicle has traveled for 
#each hour of that time period.

#Create a variable to control the loop.
rerun = "Y"

#Explain what this program does.
print ('This program calculates the distance a vehicle travels.\n')

while rerun == 'Y' or rerun =='y':
    speed = int(input('What is the speed of the vehicle in mph? '))
    time = int(input('How many hours has it traveled? '))
    if speed <= 0 or time <= 0:
        print('Invalid entry! Speed and time must be greater than 0.')
    else:    
        #Display the results
        print('Hour\t\tDistance Traveled')
        print('---------------------------------')
        for hour in range(time):
            distance = speed * (hour+1)
            print(f'{hour+1}\t\t{distance}')
    #Do you want to program
    rerun = input('Do you want to rerun this program? ' + 
                  '(Enter "Y" for Yes): ')