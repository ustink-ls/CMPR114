#Class Exercise #2: Create three labels with values of last 
#name, first name, and age.

#Project #3 (LABEL)

#This program displays a label with text.
import tkinter

class MyGUI:
    def __init__(self):
        
        #create the main window widget.
        self.main_window = tkinter.Tk()

        # creating fixed geometry of the
        # tkinter window with dimensions 150x200
        self.main_window.geometry('200x150')

        #create a label widget containing the text "Hello world!"
        self.label_1 = tkinter.Label(self.main_window, text="Hellow World!")
        self.label_2 = tkinter.Label(self.main_window, text="Last name!")
        self.label_3 = tkinter.Label(self.main_window, text="First name!")
        self.label_4 = tkinter.Label(self.main_window, text="Age!")

        #call the label widget's pack method.
        self.label_1.pack()
        self.label_2.pack()
        self.label_3.pack()
        self.label_4.pack()

        #enter the tkinter main loop.
        tkinter.mainloop()

#create an instance of the My GUI class.
if __name__ == '__main__':
    my_gui = MyGUI()