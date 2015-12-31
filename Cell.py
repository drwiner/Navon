class Cell:
    def __init__(self, positionVector, dim):
        self.position = positionVector;
        self.dim = dim;
    def update(self):
        if (hasattr(self, desiredPosition)):
            lerp(self.currentPosition, self.desiredPosition, .1);
        else:
            raise AttributeError("Desired Position not set");
        if (hasattr(self,desiredDim)):
            lerp(self.dim, self.desiredDim,.1);
        else:
            raise AttributeError("Desired Dimension not set");
    
    def outOfBounds(self):
        x,y = self.position;
        if x >= 0 and y >= 0 and x <= width-self.dim and y <= width-self.dim:
            return True;
        return False;
    
    def getCellAsRect(self):
        if not self.outOfBounds():
            return (self.position.x, self.position.y, self.dim);
        
def outOfBounds(x,y,cellSize):
    if x >= 0 and y >= 0 and x <= width-cellSize and y <= width-cellSize:
        return True;
    return False;