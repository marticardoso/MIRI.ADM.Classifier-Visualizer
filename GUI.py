import Tkinter
import tkMessageBox
import ClassifiersManager as classifiers
from MyCanvas import *
from Inputs import *
from Values import *
from ResultsLayer import *

# Main class. It creates the windows and when needed it classify the points
class GUI():

    canvas = None
    
    def __init__(self):
        self.currentValues = Values()
        # create the root window
        root = Tkinter.Tk()

        # modify the window
        root.title("ADM - Essay 4 - By Marti Cardoso")
        root.geometry("1000x600")

        canvasFrame = Tkinter.Frame(root, highlightbackground="black", highlightcolor="red", highlightthickness=1, width=500, height=500, bd= 0)
 
        self.canvasWidth = 500
        canvasFrame.pack(side = Tkinter.RIGHT, fill=Tkinter.NONE)
        self.canvas = MyCanvas(canvasFrame, self.currentValues, self.canvasWidth,self.canvasWidth)
        
        inputsFrame = Tkinter.Frame(root, highlightbackground="gray",highlightthickness=1)
        inputsFrame.pack(side = Tkinter.LEFT, fill=Tkinter.BOTH)
        self.inputs = Inputs(self, inputsFrame)


        resultsFrame = Tkinter.Frame(root, highlightbackground="gray",highlightthickness=1)
        resultsFrame.pack(side = Tkinter.LEFT, fill=Tkinter.BOTH)
        self.resultsLayer = ResultsLayer(self, resultsFrame)

        # Start the window's event-loop
        root.mainloop()

    def classify(self):
        points = np.array(self.currentValues.points)

        #Train points
        trainPoints = points[points[:,3]=='False']
        trainPointsAttr = trainPoints[:,0:2].astype(float)/self.canvasWidth
        trainPointsLabels = trainPoints[:,2]

        #Test points, ToDo
        testPoints = points[points[:,3]=='True']
        testPointsAttr = testPoints[:,0:2].astype(float)/self.canvasWidth
        testPointsLabels = testPoints[:,2]

        parameters = {}
        if(self.currentValues.classifier =="knn"):
            parameters = {"k":self.currentValues.knn_k}
        elif(self.currentValues.classifier == "MLP"):
            parameters = {"hiddenLayers":self.currentValues.MLP_hiddenLayers, "numNeurons": self.currentValues.MLP_numNeurons}
        elif(self.currentValues.classifier == "Decision tree"):
            parameters = {"max_depth": self.currentValues.decisionTree_maxDepth}
        elif(self.currentValues.classifier == "Random Forest"):
            parameters = {'max_depth': self.currentValues.randomForest_maxDepth, 'n':self.currentValues.randomForest_n, 'max_features': 1}
        elif(self.currentValues.classifier == "SVM (linear kernel)"):
            parameters = {"c": self.currentValues.linearSVM_c}
        elif(self.currentValues.classifier == 'SVM (rbf kernel)'):
            parameters = {"gamma": self.currentValues.svm_gamma, "c": self.currentValues.svm_c}

        model = classifiers.createModel(self.currentValues.classifier, parameters, trainPointsAttr, trainPointsLabels)


        #Predict grid
        gridCoord = self.canvas.grid.coordinates[:,:-1].astype(float)/self.canvasWidth
        gridResult = classifiers.predict(self.currentValues.classifier, model, gridCoord)
        self.canvas.grid.coordinates[:,2] = np.array(gridResult)


        #Predict training points
        if(len(testPointsAttr)>0):
            testResults = classifiers.predict(self.currentValues.classifier, model, testPointsAttr)
            numCorrectTest = sum(testPointsLabels == testResults)

            trainResults = classifiers.predict(self.currentValues.classifier, model, trainPointsAttr)
            numCorrectTrain = sum(trainPointsLabels == trainResults)

            self.resultsLayer.updateResults(len(trainPointsLabels), len(testPointsLabels), numCorrectTrain, numCorrectTest)

        self.canvas.render()
