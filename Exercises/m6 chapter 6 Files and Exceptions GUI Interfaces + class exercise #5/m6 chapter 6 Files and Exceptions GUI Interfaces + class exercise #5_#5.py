#Challenge Exercise #5: Continuing with project #5, add 
#the address, city, state with zip code and transfer the 
#information to a text file.

def main():
    while True:
        #try the batch of code below, if there are no errors then
        #disegard the except.
        try:
            hours = int(input('hours worked: '))
            pay = float(input('hourly pay: '))
            gross = hours * pay
            print('gross pay $', format(gross,',.2f'))
            break
            print ('recorded')
        #if there are errors on the try statement, run the below print
        except ValueError:
            print('ERROR: hours worked and pay must be valid numbers, try again')
        #built-in Exception error processing
        except Exception as err:
            print(err)
main()

#import the GUI interface controls
import tkinter as tk
#imports the messagebox display
from tkinter import messagebox 

#create the window interface
win = tk.Tk()
#width X height in pixels
win.geometry("300x300")
#lable for the title
win.title("Customer Information")

#Label widget
lblLastname = tk.Label(win, text = "enter the last name: ").grid(column = 0, row =0)
lblFirstname = tk.Label(win, text = "enter the first name: ").grid(column=0,row=1)
lblAddress = tk.Label(win, text = "enter the address: ").grid(column=0,row=2)
lblCity = tk.Label(win, text = "enter the city: ").grid(column=0,row=3)
lblState = tk.Label(win, text = "enter the state: ").grid(column=0,row=4)
lblZipcode = tk.Label(win, text = "enter the zip code: ").grid(column=0,row=5)

def write():
    text_file = open('/Users/leslyesirena/Desktop/Python/m6 chapter 6 Files and Exceptions GUI Interfaces + class exercise #5_#5.txt','w')
    content = text_file.write("\nConfirmation: " + str(LN.get()) + ", " + str(FN.get()) + ", " + str(ADDRESS.get()) + ", " + str(CITY.get()) + ", " + str(STATE.get())+ ", " + str(ZC.get()))
    text_file.close()
    messagebox.showinfo("information", "Data recorded")

def quit():
    messagebox.showinfo("information", "Thank you. . .")
    #closes the interface
    win.destroy()

#function name
def submit():
    #display info
    messagebox.showinfo("information", "entered :" + LN.get() + "," + FN.get() + "," + ADDRESS.get() + "," + CITY.get() + "," + STATE.get() + "," + ZC.get())

#the StringVar manages the entry widget
LN = tk.StringVar()
#text entry widget
txtLastname = tk.Entry(win, width = 12, textvariable= LN).grid(column=1, row=0)
FN = tk.StringVar()
txtFirstname = tk.Entry(win, width=12, textvariable=FN).grid(column=1,row=1)
ADDRESS = tk.StringVar()
txtADDRESS = tk.Entry(win, width=12, textvariable=ADDRESS).grid(column=1,row=2)
CITY = tk.StringVar()
txtCITY = tk.Entry(win, width=12, textvariable=CITY).grid(column=1,row=3)
STATE = tk.StringVar()
txtSTATE = tk.Entry(win, width=12, textvariable=STATE).grid(column=1,row=4)
ZC = tk.StringVar()
txZipcode = tk.Entry(win, width=12, textvariable=ZC).grid(column=1,row=5)

#command calls the click function
#button widget
btnSubmit = tk.Button(win,text="submit", command=submit).grid(column=1,row=6)

#command calls the quit function
#Button widget
btnQuit = tk.Button(win, text = "quit", command = quit).grid(column =1, row=6)

#call the function write
#button widget
btnWrite = tk.Button(win, text = "transfer",command = write).grid(column=2, row=6)

#ensures the interface stays on the screen or window
win.mainloop()

submit()