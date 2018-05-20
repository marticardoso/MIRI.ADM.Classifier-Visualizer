import Tkinter
import tkMessageBox
import ttk
import Classifiers 
from MyCanvas import *
class Inputs():
    def __init__(self, GUI, inputsFrame):
        self.GUI = GUI
        
        lab = Tkinter.Label(inputsFrame, width=33, text="Configuration", anchor='center')
        lab.pack()

        #Train/test ratio
        self.trainTestFrame = Tkinter.LabelFrame(inputsFrame, text="Train/test ratio")
        self.trainTestFrame.pack(padx = 4)

        (self.trainTestRatioSlider,_) = self.makeSliderform(self.trainTestFrame, "train/test ratio", initValue= self.GUI.canvas.trainTestRatio*100, minValue=1, maxValue=99, onUpdate=self.updateTrainTestRatio, textWidth=15, scaleWidth=20)       
        

        splitButton = Tkinter.Button(self.trainTestFrame, text='Split train/test', command=self.splitTrainTest, padx=20)
        splitButton.pack(pady = 5, padx = 10)


        #Classifier
        classifierFrame = Tkinter.LabelFrame(inputsFrame, text="Classifier")
        classifierFrame.pack(padx = 4)

        classifierVar = Tkinter.StringVar(classifierFrame)
        classifierVar.set(self.GUI.classifier) # default value
        w = Tkinter.OptionMenu(classifierFrame, classifierVar, *self.GUI.classifiers, command=self.changeClassifier)
        w.pack()

        (self.kknnSlider,self.kknnFrame) = self.makeSliderform(classifierFrame, "k value (knn)", initValue= self.GUI.canvas.k_knn, minValue=1, maxValue=31, onUpdate=self.updateKKnn, textWidth=15, scaleWidth=20)       
        
        classifyButton = Tkinter.Button(classifierFrame, text='Classify', command=self.classify, padx=20)
        classifyButton.pack(pady = 10, padx = 20)

        #Points options
        pointsFrame = Tkinter.LabelFrame(inputsFrame, text="Points options")
        pointsFrame.pack()
        (self.radiusSlider,_) = self.makeSliderform(pointsFrame, "Point radius", initValue= self.GUI.canvas.radius, minValue=1, maxValue=10, onUpdate=self.updateRadius, textWidth=15, scaleWidth=20)       
        (self.numPoints,_) = self.makeSliderform(pointsFrame, "Points per click", initValue= self.GUI.canvas.nPointsPerClick, minValue=1, maxValue=100, onUpdate=self.updateNumPointsPerClick, textWidth=15, scaleWidth=20)
        
        #Distribution frame
        self.distributionFrame = Tkinter.LabelFrame(inputsFrame, text="Distribution")
        self.distributionFrame.pack()

        variable = Tkinter.StringVar(inputsFrame)
        variable.set("Normal dist") # default value
        w = Tkinter.OptionMenu(self.distributionFrame, variable, "Normal dist", "Uniform dist", command=self.changeDistribution)
        w.pack()

        (self.UniformWeightSlider,self.UniformWeightFrame) = self.makeSliderform(self.distributionFrame, "width (uniform):", initValue= self.GUI.canvas.unifDistMargin, minValue=4, maxValue=200, onUpdate=self.updateUniformWeight, textWidth=15, scaleWidth=20)       
        
        (self.NormalSdSlider,self.NormalSdFrame) = self.makeSliderform(self.distributionFrame, "sd (normal):", initValue= self.GUI.canvas.normalSd, minValue=1, maxValue=100, onUpdate=self.updateNormalSd, textWidth=15, scaleWidth=20)       
        
        self.changeDistribution("Normal dist")

        # Clear button
        clearButton = Tkinter.Button(inputsFrame, text='Clear', command=self.clearCanvas, padx=20)
        clearButton.pack(pady = 10, padx = 20)

    def changeClassifier(self, event):
        self.GUI.classifier = event

    def updateRadius(self, event):   
        self.GUI.canvas.setRadius(int(event))

    def updateTrainTestRatio(self, event):   
        self.GUI.canvas.setTrainTestRatio(int(event)/100.0)

    def updateNumPointsPerClick(self, event):
        self.GUI.canvas.nPointsPerClick = int(event)

    def updateUniformWeight(self, event):
        self.GUI.canvas.unifDistMargin = int(event)

    def updateNormalSd(self, event):
        self.GUI.canvas.normalSd = int(event)

    def changeDistribution(self, event):
        if(event == "Normal dist"):
            self.UniformWeightFrame.pack_forget()
            self.NormalSdFrame.pack()
            self.GUI.canvas.isNormalDistribution = True
        if(event == "Uniform dist"):
            self.NormalSdFrame.pack_forget()
            self.UniformWeightFrame.pack()
            self.GUI.canvas.isNormalDistribution = False

    def helloCallBack(self):
        tkMessageBox.showinfo( "Hello Python", "Hello World")

    def clearCanvas(self):
        self.GUI.canvas.clear()

    def splitTrainTest(self):
        self.GUI.canvas.splitTrainTest()

    def updateKKnn(self, event):
        self.GUI.canvas.k_knn = int(event)



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

    def classify(self):
        self.GUI.classify()