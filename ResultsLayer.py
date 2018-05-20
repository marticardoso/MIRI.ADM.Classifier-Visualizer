import Tkinter
import tkMessageBox
import ttk
import Classifiers 
from MyCanvas import *
class ResultsLayer():
    def __init__(self, GUI, parentFrame):
        self.GUI = GUI
        lab = Tkinter.Label(parentFrame, width=33, text="Results", anchor='center')
        lab.pack(side=Tkinter.LEFT)

    def updateTrainTestRatio(self, event):
        print event 
    def makeInputform(self, root, field):
        row = Tkinter.Frame(root)
        var = Tkinter.StringVar()
        lab = Tkinter.Label(row, width=10, text=field, anchor='e')
        ent = Tkinter.Entry(row,textvariable=var, width = 10)
        row.pack(side=Tkinter.TOP, fill=Tkinter.X, padx=0, pady=5)
        lab.pack(side=Tkinter.LEFT)
        ent.pack(side=Tkinter.RIGHT, expand=Tkinter.YES, fill=Tkinter.X)
        return (ent, var)

    def makeSliderform(self, root, field, initValue, minValue, maxValue, onUpdate, textWidth=15, scaleWidth=15):
        row = Tkinter.Frame(root)
        lab = Tkinter.Label(row, width=textWidth, text=field, anchor='center')
        scale = Tkinter.Scale(row, from_=minValue, to=maxValue,orient=Tkinter.HORIZONTAL, command=onUpdate, width = scaleWidth)
        scale.set(initValue)
        row.pack(side=Tkinter.TOP, fill=Tkinter.X, padx=0, pady=1)
        lab.pack(side=Tkinter.LEFT)
        scale.pack(side=Tkinter.RIGHT, expand=Tkinter.YES, fill=Tkinter.X)
        return (scale, row)