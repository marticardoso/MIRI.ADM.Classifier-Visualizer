import Tkinter
import tkMessageBox
import ClassifiersManager as classifiers
from MyCanvas import *
from Inputs import *
from ResultsLayer import *

class GUI():

    canvas = None
    classifier = "knn"
    classifiers = ["knn", "MLP", "Naive Bayes", "Decision tree", "AdaBoost"]
    def __init__(self, width, height):
        # create the root window
        root = Tkinter.Tk()

        # modify the window
        root.title("Create a window")
        root.geometry("1000x600")

        canvasFrame = Tkinter.Frame(root, highlightbackground="black", highlightcolor="red", highlightthickness=1, width=500, height=500, bd= 0)
 
        canvasFrame.pack(side = Tkinter.RIGHT, fill=Tkinter.NONE)
        self.canvas = MyCanvas(canvasFrame,500,500)
        
        inputsFrame = Tkinter.Frame(root, highlightbackground="gray",highlightthickness=1)
        inputsFrame.pack(side = Tkinter.LEFT, fill=Tkinter.BOTH)
        self.inputs = Inputs(self, inputsFrame)


        resultsFrame = Tkinter.Frame(root, highlightbackground="gray",highlightthickness=1)
        resultsFrame.pack(side = Tkinter.LEFT, fill=Tkinter.BOTH)
        self.resultsLayer = ResultsLayer(self, resultsFrame)

        # Start the window's event-loop
        root.mainloop()

    def classify(self):
        points = np.array(self.canvas.points)

        #Train points
        trainPoints = points[points[:,3]=='False']
        trainPointsAttr = trainPoints[:,0:2].astype(float)
        trainPointsLabels = trainPoints[:,2]

        #Test points, ToDo
        testPoints = points[points[:,3]=='True']
        testPointsAttr = testPoints[:,0:2].astype(float)
        testPointsLabels = testPoints[:,2]


        

        parameters = {}
        if(self.classifier =="knn"):
            parameters = {"k":self.canvas.k_knn}
        elif(self.classifier == "MLP"):
            parameters = {"alpha":1}
        elif(self.classifier == "Decision tree"):
            parameters = {"max_depth": 5}
        model = classifiers.createModel(self.classifier, parameters, trainPointsAttr, trainPointsLabels)


        #Predict grid
        gridCoord = self.canvas.grid.coordinates[:,:-1].astype(float)
        gridResult = classifiers.predict(self.classifier, model, gridCoord)
        self.canvas.grid.coordinates[:,2] = np.array(gridResult)


        self.canvas.render()
