import Tkinter
import tkMessageBox
import random
from Point import *
from Grid import *
class MyCanvas():

    def __init__(self, frame, width, height):
        self.width = width
        self.height = height
        self.canvas = Tkinter.Canvas(frame, width=width, height=height)
        self.canvas.bind("<Button-1>",  self.leftclickcallback)
        self.canvas.bind("<Button-3>", self.rightclickcallback)
        self.canvas.pack()
        self.grid = Grid(40,40)
        self.radius = 3
        self.points = []
        self.trainTestRatio = 2.0/3.0
        self.nPointsPerClick = 10
        self.unifDistMargin = 50
        self.normalSd = 20

    def rightclickcallback(self, event):
        self.addNormalDistPoints(event.x,event.y,'red')
        #self.addUniformPoints(event.x,event.y,'red')

    def leftclickcallback(self,event):
        self.addNormalDistPoints(event.x,event.y,'blue')
        #self.addUniformPoints(event.x,event.y,'blue')

    def splitTrainTest(self):
        
        for point in self.points:
            point.isTest = False
        testSample = sorted(random.sample(xrange(len(self.points)), int((1-self.trainTestRatio)*len(self.points))))
        for p in testSample:
            self.points[p].isTest = True
        self.render()
    
    def clear(self):
        self.points = []
        self.canvas.delete("all")

    def render(self):
        self.canvas.delete("all")
        self.renderGrid()
        for point in self.points:
            self.renderPoint(point)
        

    def renderPoint(self, point):
        x1, y1 = (point.x - self.radius), (point.y - self.radius)
        x2, y2 = (point.x + self.radius), (point.y + self.radius)
        if(point.isTestPoint()):
            self.canvas.create_oval(x1, y1, x2, y2, width = 1, outline = point.getColor())
        else:
            self.canvas.create_oval(x1, y1, x2, y2, width = 0, fill = point.getColor())

    def setRadius(self, radius):
        self.radius = radius
        self.render()

    def setTrainTestRatio(self, ratio):
        self.trainTestRatio = ratio
            
    def renderGrid(self):
        nRows = len(self.grid.grid)
        nCols = len(self.grid.grid[1])
        for i in range(nRows):
            for j in range(nCols):
                x1 = (self.width/nCols)*j
                x2 = (self.width/nCols)*(j+1)
                y1 = (self.height/nRows)*i
                y2 = (self.height/nRows)*(i+1)
                if(self.grid.grid[i][j]=='white'):
                    color = 'white'
                elif(self.grid.grid[i][j]=='red'):
                    color = '#FFDDDD'
                else:
                    color = '#DDDDFF'
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color,width = 0)
    
    def addUniformPoints(self, x, y, color):
        xMin, xMax = max(1,x-self.unifDistMargin), min(self.width,x+self.unifDistMargin)
        yMin, yMax = max(1,y-self.unifDistMargin), min(self.height,y+self.unifDistMargin)
        for _ in range(self.nPointsPerClick):
            x1 = random.randint(xMin, xMax)
            y1 = random.randint(yMin, yMax)
            newPoint = Point(x1, y1,color, False)
            self.points.append(newPoint)
            self.renderPoint(newPoint)

    def addNormalDistPoints(self, x, y, color):
        for _ in range(self.nPointsPerClick):
            x1 = random.normalvariate(x, self.normalSd)
            y1 = random.normalvariate(y, self.normalSd)
            newPoint = Point(x1, y1,color, False)
            self.points.append(newPoint)
            self.renderPoint(newPoint)


        
        



