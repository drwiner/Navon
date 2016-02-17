from math import floor

class Cell(object):
    def __init__(self, positionVector, dim):
        self.position = positionVector;
        self.dim = dim;
        
    def getRange(self):
        return (getRangeJ(self.position.x,self.dim), getRangeJ(self.position.y,self.dim));

    def update(self):
        if (hasattr(self, desiredPosition)):
            lerp(self.currentPosition, self.desiredPosition, .1);
        else:
            raise AttributeError("Desired Position not set");
        if (hasattr(self,desiredDim)):
            lerp(self.dim, self.desiredDim,.1);
        else:
            raise AttributeError("Desired Dimension not set");
            


def patternA():
    return [(5,0),(6,0),(5,1),(6,1),(4,2),(5,2),(6,2),(7,2),(4,3),(5,3),(6,3),
        (7,3),(3,4),(4,4),(7,4),(8,4),(3,5),(4,5),(7,5),(8,5),(2,6),(3,6),
        (4,6),(5,6),(6,6),(7,6),(8,6),(9,6),(2,7),(3,7),(4,7),(5,7),(6,7),
        (7,7),(8,7),(9,7),(1,8),(2,8),(9,8),(10,8),(1,9),(2,9),(9,9),(10,9),
        (0,10),(1,10),(10,10),(11,10),(0,11),(1,11),(10,11),(11,11)];
    
def coordToOrder(coord,numRows):
    x,y = coord;
    return x*numRows + y;

def orderToCoord(order,numRows,delta):
    x = floor(float(order) / float(numRows));
    y = order - (numRows * x);
    x = (x * delta);
    y = (y * delta);
    #print(x,y);
    return PVector(float(x),float(y));

        
def getRangeJ(x, dim):
    return range(x, x + dim);
