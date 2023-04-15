#Challenge Exercise #7: create a console (NO GUI) application that 
#will ask the user to enter the full name, with the grade of the midterm 
#and final exam and write the average grade with letter grade into a text file. 
#Use the table as a guide. Use also the try statement for this application. 
#Make sure to append the data and read the content of the file also.
#90-100	Letter grade A
#80-89	Letter grade B
#70-79	Letter grade C
#60-69	Letter grade D
#Under 60	Letter grade F

def main(): 
    try:
        #Get the user's information.
        name = input("Enter your full name: ")
        #If this statement raises a ValueError exception...
        midterm = int(input('Enter the score of your midterm exam: '))
        final = int(input('Enter the score of your final exam: '))
    #The program jumps to the except ValueError clause and executes its handler.
    except ValueError:
        print('ERROR: The scores of your midterm and final exams must be valid numbers.')

    # Calculate the average grade.
    average_grade = (midterm + final)/ 2
    # Display the average grade.
    print(f'Average grade: {average_grade:,.2f}')
    #Call and assign the letter grade function to a variable.
    average_letter_grade = letter_grade(average_grade)

    #Open the file for writing.
    emp_file = open('/Users/leslyesirena/Desktop/Python/m6 chapter 6 Files and Exceptions GUI Interfaces + class exercise #5_#7.txt','w')
    #Write the user's information to the empty file.
    emp_file.write(f'Full Name: {name}\n')
    emp_file.write(f'Average grade: {average_grade}\n')
    emp_file.write(str(average_letter_grade))
    #close the file.
    emp_file.close()
    print('\nData has been recorded to file.')

def letter_grade(average_grade):
    #Based on average grade, determine average letter grade. 
    if (average_grade <60):
        #"print" is displayed in the console.
        print('Average letter grade: F')
        #"return" is displayed in the text file.
        return 'Average letter grade: F'
    elif (average_grade>=60 and average_grade <70):
        print('Average letter grade: D')
        return 'Average letter grade: D'
    elif (average_grade>=70 and average_grade <80):
        print('Average letter grade: C')
        return 'Average letter grade: C'
    elif (average_grade>=80 and average_grade <90):
        print('Average letter grade: B')
        return 'Average letter grade: B'
    else:
        print('Average letter grade: A')
        return 'Average letter grade: A'
    
main()