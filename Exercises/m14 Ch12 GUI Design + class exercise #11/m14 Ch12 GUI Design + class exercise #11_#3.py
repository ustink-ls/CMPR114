#Class Exercise #3: Continuing with project 6, create two 
#additional labels with a positive quote of your choice. Ensure 
#to put padding so it will fit the window neatly.

#Project #6 (INTERNAL PADDING)

#This program demonstrates internal padding.
import tkinter

class MyGui:
    def __init__(self):
        
        #creat the main window widget.
        self.main_window = tkinter.Tk()

        #create two label widgets with solid borders.
        self.label1 = tkinter.Label (self.main_window,
                                     text = "Hello World!",
                                     borderwidth=1,
                                     relief="solid")
        self.label2 = tkinter.Label (self.main_window,
                                     text = "This is my GUI program.",
                                     borderwidth=1,
                                     relief="solid")
        self.label3 = tkinter.Label (self.main_window,
                                text = "Alas, poor Yorick!",
                                borderwidth=1,
                                relief="solid")
        self.label4 = tkinter.Label (self.main_window,
                        text = "A rose by any other name would smell as sweet.",
                        borderwidth=1,
                        relief="solid")

        
        #display the Labels with 20 pixels of horizontal
        #and vertical internal padding.
        self.label1.pack (ipadx=20, ipady=20)
        self.label2.pack (ipadx=20, ipady=20)
        self.label3.pack (ipadx=20, ipady=20)
        self.label4.pack (ipadx=20, ipady=20)

        #enter the tkinter main loop.
        tkinter.mainloop()

#create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGui()