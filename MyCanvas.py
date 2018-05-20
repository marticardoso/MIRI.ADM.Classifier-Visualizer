import Tkinter
import tkMessageBox
import random
from Grid import *
class MyCanvas():

    def __init__(self, frame, width, height):
        self.width = width
        self.height = height
        self.canvas = Tkinter.Canvas(frame, width=width, height=height)
        self.canvas.bind("<Button-1>",  self.leftclickcallback)
        self.canvas.bind("<Button-3>", self.rightclickcallback)
        self.canvas.pack()
        self.grid = Grid(50,50, width, height)
        self.radius = 3
        self.points = []
        self.trainTestRatio = 2.0/3.0
        self.nPointsPerClick = 10
        self.unifDistMargin = 50
        self.normalSd = 20
        self.k_knn = 1
        self.isNormalDistribution = True


    def rightclickcallback(self, event):
        if(self.isNormalDistribution):
            self.addNormalDistPoints(event.x,event.y,'red')
        else:
            self.addUniformPoints(event.x,event.y,'red')

    def leftclickcallback(self,event):
        if(self.isNormalDistribution):
            self.addNormalDistPoints(event.x,event.y,'blue')
        else:
            self.addUniformPoints(event.x,event.y,'blue')

    def splitTrainTest(self):
        
        for point in self.points:
            point[3] = False
        testSample = sorted(random.sample(xrange(len(self.points)), int((1-self.trainTestRatio)*len(self.points))))
        for p in testSample:
            self.points[p][3] = True
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
        x1, y1 = (point[0] - self.radius), (point[1] - self.radius)
        x2, y2 = (point[0] + self.radius), (point[1] + self.radius)
        if(point[3]):
            self.canvas.create_oval(x1, y1, x2, y2, width = 1, outline = point[2])
        else:
            self.canvas.create_oval(x1, y1, x2, y2, width = 0, fill = point[2])

    def setRadius(self, radius):
        self.radius = radius
        self.render()

    def setTrainTestRatio(self, ratio):
        self.trainTestRatio = ratio
            
    def renderGrid(self):
        for i in range(len(self.grid.coordinates)):
            color = self.grid.coordinates[i,2]
            x1 = int(self.grid.coordinates[i,0]) - self.grid.cellWidth/2.0
            x2 = int(self.grid.coordinates[i,0]) + self.grid.cellWidth/2.0
            y1 = int(self.grid.coordinates[i,1])- self.grid.cellHeight/2.0
            y2 = int(self.grid.coordinates[i,1])+ self.grid.cellHeight/2.0
            if(color=='white'):
                colorBg = 'white'
            elif(color=='red'):
                colorBg = '#FFDDDD'
            else:
                colorBg = '#DDDDFF'
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=colorBg,width = 0)
    
    def addUniformPoints(self, x, y, color):
        xMin, xMax = max(1,x-self.unifDistMargin), min(self.width,x+self.unifDistMargin)
        yMin, yMax = max(1,y-self.unifDistMargin), min(self.height,y+self.unifDistMargin)
        for _ in range(self.nPointsPerClick):
            x1 = random.randint(xMin, xMax)
            y1 = random.randint(yMin, yMax)
            newPoint = [x1, y1,color, False]
            self.points.append(newPoint)
            self.renderPoint(newPoint)

    def addNormalDistPoints(self, x, y, color):
        for _ in range(self.nPointsPerClick):
            x1 = random.normalvariate(x, self.normalSd)
            y1 = random.normalvariate(y, self.normalSd)
            newPoint = [x1, y1,color, False]
            self.points.append(newPoint)
            self.renderPoint(newPoint)

