#Get the gross salary from the user.
salary = float(input('Enter your gross salary: '))

#Calculate 10% of salary.
ten_percent = (salary * .10)

#Add salary and 10% of salary together.
total_salary = salary + ten_percent

#Display the total salary.
print("Your total salary is: ${:,.2f}".format(total_salary))
