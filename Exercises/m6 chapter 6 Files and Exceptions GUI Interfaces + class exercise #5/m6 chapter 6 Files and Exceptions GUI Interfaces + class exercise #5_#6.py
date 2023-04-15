#Challenge Exercise #6: create a GUI interface that will write 3 numbers and 
#sum + averages the total into a text file.
#Example output in the text file:
#The three numbers are: 1, 2 and 3
#The total is 6
#The average is 2

#import the GUI interface controls
import tkinter as tk
#imports the messagebox display
from tkinter import messagebox

#fucntion that calculates total/average based
#on the values entered by the user in the 
#window
def calculate():
    #First, the try clause (the statement(s) between the try and except keywords) is executed.
    #If no exception occurs, the except clause is skipped and execution of the try statement is finished.
    try:
        #call and assign the numbers that were entered by the user to the num1/2/3 variables.
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        total = num1 + num2 + num3
        average = total / 3
        #This will be displayd to the user after they press the calculate button.
        messagebox.showinfo("Result", f"Total: {total}\nAverage: {average}")
    #If an exception occurs during execution of the try clause, the rest of the clause is skipped. 
    #Then, if its type matches the exception named after the except keyword, the except clause is 
    #executed, and then execution continues after the try/except block.
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
    
    #Open the file for writing.
    text_file = open('/Users/leslyesirena/Desktop/Python/m6 chapter 6 Files and Exceptions GUI Interfaces + class exercise #5_#6.txt','w')
    with text_file as f:
        f.write("Number 1: {}\n".format(num1))
        f.write("Number 2: {}\n".format(num2))
        f.write("Number 3: {}\n".format(num3))
        f.write("Total: {}\n".format(total))
        f.write("Average: {:.2f}\n".format(average))
        text_file.close()
        messagebox.showinfo("information", "Data recorded")

#create the window interface
root = tk.Tk()
#label for the title
root.title("Number Calculator")

#Label widgets: What will be displayed to user and what will store
#user's info
label1 = tk.Label(root, text="Enter the first number:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Enter the second number:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3 = tk.Label(root, text="Enter the third number:")
label3.grid(row=2, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1)

#button widget: what the user will click on to execute calculation.
button = tk.Button(root, text="Calculate", command=calculate)
button.grid(row=3, column=1)

root.mainloop()

