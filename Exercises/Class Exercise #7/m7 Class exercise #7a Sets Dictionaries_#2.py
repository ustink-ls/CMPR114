#Challenge Exercise #2: continuing with project #3, 
#print the food items.

#Create a GUI with some listboxes items.
#Import tkinter.
from tkinter import *

#Create a Tk root window named top.
top = Tk()

#create a listbox.
listbox = Listbox(top, height=10,
                  width=15, bg="grey",
                  activestyle='dotbox',
                  font="Helvita",
                  fg="yellow",
                  selectmode=MULTIPLE)

#define the size of the window.
top.geometry('300x250')

#Define the label for the list.
label = Label(top, text = " FOOD ITEMS")

#insert elements by index with their names as parameters.
listbox.insert(1, "Sandwich")
listbox.insert(2, "Burger")
listbox.insert(3, "Pizza")
listbox.insert(4, "French Fries")
listbox.insert(5, "Hot Dogs")
listbox.insert(6, "Cheeseburger")

#fucntion for printing the selected listbox value(s).
def selected_item():
    for i in listbox.curselection():
        #Traverse the tuple returned by curselection 
        #method and print corresponding value(s) in
        #the listbox.
        print(listbox.get(i))

#create a bottom widget and map the command paremeter to selected_
#item function.
btn = Button(top, text='Print Selection', command=selected_item)

#placing the bottom in the listbox.
btn.pack(side='bottom')

#pack the widgets
label.pack()
listbox.pack()

#Display until user exits themselves.
top.mainloop()

