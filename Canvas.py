from random import random;
from math import floor
from Cell import Cell
from Cell import patternA
from Cell import coordToOrder
from Cell import orderToCoord

class Canvas(Cell):
    #A Cell has a position, size. Use hasattr to determine if cell is a canvas
    
    def __init__(self, position, initialCellSize, initialCanvasSize, index):
        super(Canvas,self).__init__(position,initialCanvasSize);
        self.genCells();
        self.genPattern();
        self.index = index;
        
    def assembleChildren():
        childrenCells = self.genCells();
        children = [];
        for i,child in enumerate(childrenCells):
            if i in self.pattern:
                children.append(child.assembleChildren());
        return children;
                
    def genCells(self):
        canvasRangeX, canvasRangeY = self.getRange();
        
        if not self.children:
            self.children = [Cell(PVector(r,c), self.childCellSize) for r in canvasRangeX for c in canvasRangeY if (r-self.position.x)%self.childCellSize ==0 and (c-self.position.y)%(self.childCellSize)==0];
        else:
            self.childrenPositions  = ((r,c) for r in canvasRangeX for c in canvasRangeY if (r-self.position.x)%self.childCellSize ==0 and (c-self.position.y)%(self.childCellSize)==0);
            for i, child in enumerate(self.children):
                nextPos = self.childrenPositions.next();
                if i in self.pattern:
                    child.position = nextPos;
            self.favoriteChild = self.children[self.pattern[0]];
        #Used as a sample to update .dim size in updateChildren.
        
        
    
    def updateChildren(self, amountIncrease):
        self.genCells();
        for i, child in enumerate(self.children):
            if i in self.pattern:
                child.updateChildren(amountIncrease);
        self.dim = self.favoriteChild.dim *12;
        self.genCells();
    
    def updateCells(self,displacement,increase):
       
        #Canvas Size
        self.dim += int(increase); # The canvas is now larger.
        distributedIncrease = int(increase/self.numRows); # The increase divided by the number of cells in the row/col. Thus, increase should be dividible into num rows...
        
        #Cell Size
        self.childCellSize += distributedIncrease; #The children are larger
        print("childcellsize: ", self.childCellSize);
        
        #Canvas Position
        self.position.add(displacement);
        
        #Cell Position
        self.genCells();            

    #Creates a list of integers corresponding to indices in the cellList
    def genPattern(self):
        pA = patternA();
        self.pattern = [coordToOrder(i,12) for i in pA];
    
    #Selects a random integer from the pattern, a list of integers
    #Returns a cell in canvas that is the center for all canvi
    #Called by Canvas Manager
    def pickRandomTarget(self):
        spaceSize = len(self.pattern);
        self.centerInOrder = self.pattern[int(floor(random()*spaceSize))];
        self.center = self.cellList[self.centerInOrder]
        return (self.center, self.centerInOrder);
        


#Helpful method for returning (x,y) tuple that is iterable from pvector
def unpack(pvector):
    return (pvector.x,pvector.y);

#Helpful method for detecting if a cell, be it canvas or not, is on the board
def cellInBounds(cell, maxCanvasSize = 599):
    x,y = unpack(cell.position);
    #if top left corner is in
    if inBounds(x) and inBounds(y):
        return True;
    #if top right corner is in
    tx = x+cell.dim-1;
    if inBounds(tx) and inBounds(y):
        return True;
    #if bot left corner is in
    by = y + cell.dim -1;
    if inBounds(x) and inBounds(by):
        return True;
    #if bot right corner is in
    if inBounds(tx) and inBounds(by):
        return True;
    if x <= 0 and y <= 0:
        return True;
    return False; #Cell not in bounds


def inBounds(unit, low=0, up=599):
    if unit >= low and unit <= up:
        return True;
    return False;

                                                                                                
