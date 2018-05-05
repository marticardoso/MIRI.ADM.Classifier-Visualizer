class Point:
    def __init__(self, x, y, c, isTest):
        self.x = x
        self.y = y
        self.color = c
        self.isTest = isTest

    def getColor(self):
        return self.color
    
    def getClass(self):
        if(self.color == 'red'):
            return 0
        else:
            return 1
    def isTestPoint(self):
        return self.isTest