import Tkinter
import tkMessageBox
import ttk
from MyCanvas import *

class Inputs():
    def __init__(self, GUI, inputsFrame):
        self.GUI = GUI

        

        self.trainTestRatioSlider = Tkinter.Scale(inputsFrame, label='Train/Test ratio', from_=1, to=99,orient=Tkinter.HORIZONTAL, command=self.updateTrainTestRatio)
        self.trainTestRatioSlider.set(int(self.GUI.canvas.trainTestRatio*100))
        self.trainTestRatioSlider.pack(pady = 10, padx = 20)

        splitButton = Tkinter.Button(inputsFrame, text='Split train/test', command=self.splitTrainTest, padx=20)
        splitButton.pack(pady = 10, padx = 20)

        self.radiusSlider = Tkinter.Scale(inputsFrame, label='Point radius', from_=1, to=10,orient=Tkinter.HORIZONTAL, command=self.updateRadius)
        self.radiusSlider.set(self.GUI.canvas.radius)
        self.radiusSlider.pack(pady = 10, padx = 20)

        self.numPoints = Tkinter.Scale(inputsFrame, label='Points per click', from_=1, to=100,orient=Tkinter.HORIZONTAL, command=self.updateNumPointsPerClick)
        self.numPoints.set(self.GUI.canvas.nPointsPerClick)
        self.numPoints.pack(pady = 10, padx = 20)

        variable = Tkinter.StringVar(inputsFrame)
        variable.set("Normal dist") # default value
        w = Tkinter.OptionMenu(inputsFrame, variable, "Normal dist", "Uniform dist")
        w.pack()

        self.UniformWeight = Tkinter.Scale(inputsFrame, label='Uniform dist - Weight:', from_=4, to=200,orient=Tkinter.HORIZONTAL, command=self.updateUniformWeight)
        self.UniformWeight.set(self.GUI.canvas.unifDistMargin)
        self.UniformWeight.pack(pady = 10, padx = 20)

        self.NormalSdSlider = Tkinter.Scale(inputsFrame, label='Normal dist - sd:', from_=1, to=100,orient=Tkinter.HORIZONTAL, command=self.updateNormalSd)
        self.NormalSdSlider.set(self.GUI.canvas.normalSd)
        self.NormalSdSlider.pack(pady = 10, padx = 20)

        clearButton = Tkinter.Button(inputsFrame, text='Clear', command=self.clearCanvas, padx=20)
        clearButton.pack(pady = 10, padx = 20)


    def updateRadius(self, event):   
        self.GUI.canvas.setRadius(self.radiusSlider.get())

    def updateTrainTestRatio(self, event):   
        self.GUI.canvas.setTrainTestRatio(self.trainTestRatioSlider.get()/100.0)

    def updateNumPointsPerClick(self, event):
        self.GUI.canvas.nPointsPerClick = self.numPoints.get()

    def updateUniformWeight(self, event):
        self.GUI.canvas.unifDistMargin = self.UniformWeight.get()

    def updateNormalSd(self, event):
        self.GUI.canvas.normalSd = self.NormalSdSlider.get()

    def helloCallBack(self):
        tkMessageBox.showinfo( "Hello Python", "Hello World")

    def clearCanvas(self):
        self.GUI.canvas.clear()

    def splitTrainTest(self):
        self.GUI.canvas.splitTrainTest()

