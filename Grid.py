import numpy as np
from sklearn.utils.extmath import cartesian

# Grid stores the points on the grid to classify
class Grid:
    def __init__(self, width, height, canvasWidth, canvasHeight):
        self.width = width
        self.height = height
        self.cellWidth = float(canvasWidth)/float(width)
        self.cellHeight = float(canvasHeight)/float(height)

        self.coordinates = np.array([[0,0,'blue']]*(width*height))

        cartesianResult = cartesian([range(width),range(height)])
        cartesianResult[:,0] = cartesianResult[:,0]*self.cellWidth + self.cellWidth/2.0
        cartesianResult[:,1] = cartesianResult[:,1]*self.cellHeight + self.cellHeight/2.0

        self.coordinates[:,:-1] = cartesianResult


        