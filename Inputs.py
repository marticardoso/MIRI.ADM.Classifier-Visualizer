import Tkinter
import tkMessageBox
import ttk
import Classifiers 
from MyCanvas import *

# All logic related to the inputs parameters
class Inputs():
    def __init__(self, GUI, inputsFrame):
        self.GUI = GUI
        
        lab = Tkinter.Label(inputsFrame, width=33, text="Configuration", anchor='center')
        lab.pack()

        #Train/test ratio
        self.trainTestFrame = Tkinter.LabelFrame(inputsFrame, text="Train/test ratio")
        self.trainTestFrame.pack(padx = 4)
        (self.trainTestRatioSlider,_) = self.makeSliderform(self.trainTestFrame, "train/test ratio", initValue= self.GUI.currentValues.trainTestRatio*100, minValue=1, maxValue=99, onUpdate=self.updateTrainTestRatio, textWidth=15, scaleWidth=20)       
        
        splitButton = Tkinter.Button(self.trainTestFrame, text='Split train/test', command=self.splitTrainTest, padx=20)
        splitButton.pack(pady = 5, padx = 10)


        #Classifier
        classifierFrame = Tkinter.LabelFrame(inputsFrame, text="Classifier")
        classifierFrame.pack(padx = 4)

        classifierVar = Tkinter.StringVar(classifierFrame)
        classifierVar.set(self.GUI.currentValues.classifier) # default value
        w = Tkinter.OptionMenu(classifierFrame, classifierVar, *self.GUI.currentValues.classifiers, command=self.changeClassifier)
        w.pack()
        #Classifier options
        (_,self.kknnFrame) = self.makeSliderform(classifierFrame, "k value (knn)", initValue= self.GUI.currentValues.knn_k, minValue=1, maxValue=31, onUpdate=self.updateKKnn, textWidth=15, scaleWidth=20)       
        (_,self.decisionTreeMaxDepthFrame) = self.makeSliderform(classifierFrame, "max depth", initValue= self.GUI.currentValues.decisionTree_maxDepth, minValue=1, maxValue=31, onUpdate=self.updateDecisionTreeMaxDepth, textWidth=15, scaleWidth=20)       
        (_,self.RandomForestMaxDepthFrame) = self.makeSliderform(classifierFrame, "max depth", initValue= self.GUI.currentValues.randomForest_maxDepth, minValue=1, maxValue=31, onUpdate=self.updateRandomForestMaxDepth, textWidth=15, scaleWidth=20)       
        (_,self.RandomForestNFrame) = self.makeSliderform(classifierFrame, "n estimators", initValue= self.GUI.currentValues.randomForest_n, minValue=1, maxValue=31, onUpdate=self.updateRandomForestN, textWidth=15, scaleWidth=20)       
        
        (_,_,self.LinearSVMCFrame) = self.makeInputform(classifierFrame, "C value", initValue= self.GUI.currentValues.linearSVM_c, onUpdate=self.updateLinearSVMC)       
        (_,_,self.SVMCFrame) = self.makeInputform(classifierFrame, "C value", initValue= self.GUI.currentValues.svm_c, onUpdate=self.updateSVMC)       
        (_,_,self.SVMGammaFrame) = self.makeInputform(classifierFrame, "Gamma value", initValue= self.GUI.currentValues.svm_gamma, onUpdate=self.updateSVMGamma)   
        (_,self.MLPLayersFrame) = self.makeSliderform(classifierFrame, "hidden layers", initValue= self.GUI.currentValues.MLP_hiddenLayers, minValue=1, maxValue=10, onUpdate=self.updateMLPHiddenLayers, textWidth=15, scaleWidth=20)       
        (_,self.MLPNeuronsFrame) = self.makeSliderform(classifierFrame, "neurons/layer", initValue= self.GUI.currentValues.MLP_numNeurons, minValue=1, maxValue=100, onUpdate=self.updateMLPNumNeurons, textWidth=15, scaleWidth=20)       
        
        
        self.classifyButton = Tkinter.Button(classifierFrame, text='Classify', command=self.classify, padx=20)
        self.classifyButton.pack(pady = 10, padx = 20)

        self.changeClassifier('knn')
        
        #Points options
        pointsFrame = Tkinter.LabelFrame(inputsFrame, text="Points options")
        pointsFrame.pack()
        (self.radiusSlider,_) = self.makeSliderform(pointsFrame, "Point radius", initValue= self.GUI.currentValues.radius, minValue=1, maxValue=10, onUpdate=self.updateRadius, textWidth=15, scaleWidth=20)       
        (self.numPoints,_) = self.makeSliderform(pointsFrame, "Points per click", initValue= self.GUI.currentValues.nPointsPerClick, minValue=1, maxValue=100, onUpdate=self.updateNumPointsPerClick, textWidth=15, scaleWidth=20)
        
        #Distribution frame
        self.distributionFrame = Tkinter.LabelFrame(inputsFrame, text="Distribution")
        self.distributionFrame.pack()

        variable = Tkinter.StringVar(inputsFrame)
        variable.set("Normal dist") # default value
        w = Tkinter.OptionMenu(self.distributionFrame, variable, "Normal dist", "Uniform dist", command=self.changeDistribution)
        w.pack()

        (self.UniformWeightSlider,self.UniformWeightFrame) = self.makeSliderform(self.distributionFrame, "width (uniform):", initValue= self.GUI.currentValues.unifDistMargin, minValue=4, maxValue=200, onUpdate=self.updateUniformWeight, textWidth=15, scaleWidth=20)       
        
        (self.NormalSdSlider,self.NormalSdFrame) = self.makeSliderform(self.distributionFrame, "sd (normal):", initValue= self.GUI.currentValues.normalSd, minValue=1, maxValue=100, onUpdate=self.updateNormalSd, textWidth=15, scaleWidth=20)       
        
        self.changeDistribution("Normal dist")

        # Clear button
        clearButton = Tkinter.Button(inputsFrame, text='Clear', command=self.clearCanvas, padx=20)
        clearButton.pack(pady = 10, padx = 20)

    def changeClassifier(self, event):
        self.classifyButton.pack_forget()
        self.GUI.currentValues.classifier = event
        if(event == "knn"):
            self.kknnFrame.pack()
        else:
            self.kknnFrame.pack_forget()

        if(event == "Decision tree"):
            self.decisionTreeMaxDepthFrame.pack()
        else:
            self.decisionTreeMaxDepthFrame.pack_forget()

        if(event == "MLP"):
            self.MLPLayersFrame.pack()
            self.MLPNeuronsFrame.pack()
        else:
            self.MLPLayersFrame.pack_forget()
            self.MLPNeuronsFrame.pack_forget()

        if(event == "Random Forest"):
            self.RandomForestMaxDepthFrame.pack()
            self.RandomForestNFrame.pack()
        else:
            self.RandomForestMaxDepthFrame.pack_forget()
            self.RandomForestNFrame.pack_forget()
        if(event == "SVM (linear kernel)"):
            self.LinearSVMCFrame.pack()
        else:            
            self.LinearSVMCFrame.pack_forget()
        if(event == 'SVM (rbf kernel)'):
            self.SVMCFrame.pack()
            self.SVMGammaFrame.pack()
        else:            
            self.SVMCFrame.pack_forget()
            self.SVMGammaFrame.pack_forget()

        self.classifyButton.pack(pady = 10, padx = 50)
        

    def updateRadius(self, event): 
        self.GUI.currentValues.radius = int(event)  
        self.GUI.canvas.render()

    def updateTrainTestRatio(self, event):   
        self.GUI.currentValues.trainTestRatio= int(event)/100.0

    def updateNumPointsPerClick(self, event):
        self.GUI.currentValues.nPointsPerClick = int(event)

    def updateUniformWeight(self, event):
        self.GUI.currentValues.unifDistMargin = int(event)

    def updateNormalSd(self, event):
        self.GUI.currentValues.normalSd = int(event)

    def updateLinearSVMC(self, event):
        if(event!=''):
            self.GUI.currentValues.linearSVM_c = float(event)

    def updateSVMC(self, event):
        if(event!=''):
            self.GUI.currentValues.svm_c = float(event)

    def updateSVMGamma(self, event):
        if(event!=''):
            self.GUI.currentValues.svm_gamma = float(event)

    def changeDistribution(self, event):
        if(event == "Normal dist"):
            self.UniformWeightFrame.pack_forget()
            self.NormalSdFrame.pack()
            self.GUI.currentValues.isNormalDistribution = True
        if(event == "Uniform dist"):
            self.NormalSdFrame.pack_forget()
            self.UniformWeightFrame.pack()
            self.GUI.currentValues.isNormalDistribution = False



    def helloCallBack(self):
        tkMessageBox.showinfo( "Hello Python", "Hello World")

    def clearCanvas(self):
        self.GUI.canvas.clear()

    def splitTrainTest(self):
        self.GUI.canvas.splitTrainTest()

    def updateKKnn(self, event):
        self.GUI.currentValues.knn_k = int(event)
    
    def updateDecisionTreeMaxDepth(self, event):
        self.GUI.currentValues.decisionTree_maxDepth = int(event)

    def updateMLPNumNeurons(self, event):
        self.GUI.currentValues.MLP_numNeurons = int(event)

    def updateMLPHiddenLayers(self, event):
        self.GUI.currentValues.MLP_hiddenLayers = int(event)

    def updateRandomForestMaxDepth(self, event):
        self.GUI.currentValues.randomForest_maxDepth = int(event)

    def updateRandomForestN(self, event):
        self.GUI.currentValues.randomForest_n = int(event)

    def makeInputform(self, root, field, initValue, onUpdate):
        row = Tkinter.Frame(root)
        var = Tkinter.StringVar()
        var.set(initValue)
        var.trace("w", lambda name, index, mode, sv=var: onUpdate(sv.get()))
        lab = Tkinter.Label(row, width=15, text=field, anchor='e')
        ent = Tkinter.Entry(row,textvariable=var, width = 20)
        row.pack(side=Tkinter.TOP, fill=Tkinter.X, padx=0, pady=5)
        lab.pack(side=Tkinter.LEFT)
        ent.pack(side=Tkinter.RIGHT, expand=Tkinter.YES, fill=Tkinter.X)
        return (ent, var, row)

    def makeSliderform(self, root, field, initValue, minValue, maxValue, onUpdate, textWidth=15, scaleWidth=15, resolution=1):
        row = Tkinter.Frame(root)
        lab = Tkinter.Label(row, width=textWidth, text=field, anchor='center')
        scale = Tkinter.Scale(row, from_=minValue, to=maxValue, resolution=resolution, orient=Tkinter.HORIZONTAL, command=onUpdate, width = scaleWidth)
        scale.set(initValue)
        row.pack(side=Tkinter.TOP, fill=Tkinter.X, padx=0, pady=1)
        lab.pack(side=Tkinter.LEFT)
        scale.pack(side=Tkinter.RIGHT, expand=Tkinter.YES, fill=Tkinter.X)
        return (scale, row)

    def classify(self):
        self.GUI.classify()