from random import random;
from math import floor
from Cell import Cell
from Cell import patternA
from Cell import coordToOrder
from Cell import orderToCoord
from Canvas import Canvas

class CanvasLeaf(Canvas):
    #A Cell has a position, size. Use hasattr to determine if cell is a canvas
    
    def __init__(self, position, canvasLeafSize, childSize):
        super(CanvasLeaf,self).__init__(position,canvasLeafSize,childSize);
        self.center = self.children[self.centerInOrder];
        
    def updateChildren(self, amountIncrease):
        self.cellSize = self.cellSize + amountIncrease;
        self.dim = self.dim + amountIncrease*12;
        for i in self.children:
            i.updateChildren(amountIncrease);
                
            #CalculateDisplacement after growth

    #def updateDisplacement(self, amountIncrease):
     #   distributedIncrease =
    
    def getCenterPosition(self):
        return self.center.position;
            
    def assembleChildren(self):
        self.genCells();
        return self.children;
