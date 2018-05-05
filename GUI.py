import Tkinter
import tkMessageBox
from MyCanvas import *
from Inputs import *

class GUI():

    canvas = None
    def __init__(self):
        # create the root window
        root = Tkinter.Tk()

        # modify the window
        root.title("Create a window")
        root.geometry("800x500")

        canvasFrame = Tkinter.Frame(root, highlightbackground="black", highlightcolor="red", highlightthickness=1, width=500, height=500, bd= 0)
 
        canvasFrame.pack(side = Tkinter.RIGHT, fill=Tkinter.NONE)
        self.canvas = MyCanvas(canvasFrame,400,400)
        
        inputsFrame = Tkinter.Frame(root, bg = 'red')
        inputsFrame.pack(side = Tkinter.LEFT, fill=Tkinter.BOTH)
        self.inputs = Inputs(self, inputsFrame)


        # Start the window's event-loop
        root.mainloop()