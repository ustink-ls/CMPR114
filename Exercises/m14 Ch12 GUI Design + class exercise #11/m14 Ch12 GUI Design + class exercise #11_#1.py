#Class Exercise #1: Using the geometry method, increase the
#width so the title is visible.


#Project #1 (EMPTY WINDOW)
import tkinter

def main():
    #create the main window widget.
    main_window = tkinter.Tk()

    #enter the tkinter main loop.
    tkinter.mainloop()

main()


#Project #2 (TITLE BAR)
import tkinter

class MyGui:
    def __init__(self):
        #create the main window weidget.
        self.main_window = tkinter.Tk()

        #display a title.
        self.main_window.title('My First GUI')

        # creating fixed geometry of the
        # tkinter window with dimensions 150x200
        self.main_window.geometry('400x200')

        #Enter the tkinter main loop.
        tkinter.mainloop()

#create an instance of the MyGui class.
if __name__ == '__main__':
    my_gui = MyGui()

