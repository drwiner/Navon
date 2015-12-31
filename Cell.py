class Cell:
    def __init__(self, positionVector, dim):
        self.position = positionVector;
        self.dim = dim;
        self.isCanvas = False;
    def update(self):
        if (hasattr(self, desiredPosition)):
            lerp(self.currentPosition, self.desiredPosition, .1);
        else:
            raise AttributeError("Desired Position not set");
        if (hasattr(self,desiredDim)):
            lerp(self.dim, self.desiredDim,.1);
        else:
            raise AttributeError("Desired Dimension not set");