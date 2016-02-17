from random import random;
from math import floor
from Cell import Cell
from Cell import patternA
from Cell import coordToOrder
from Cell import orderToCoord

#CanvasLeaf is the parent of cells that are drawn to screen
class CanvasLeaf(Cell):
    
    def __init__(self, position, canvasLeafSize):
        super(CanvasLeaf,self).__init__(position,canvasLeafSize);
        
        #Gives position and size
        self.genPattern();
        
        #Selects pattern-member as centerInOrder
        self.pickRandomTarget();
        
        #Gives pattern order in 12 by 12
        self.genCells();
        #Generates and assigns positions to children. Permanent Assignment.
        
        
        
    def growChildren(self, amountIncrease):
        
        #grow Children
        for i,child in enumerate(self.children):
            if i in self.pattern:
                child.dim = child.dim + amountIncrease;
                
        #grow Self
        self.dim = self.favoriteChild.dim *12;

        #Check if time to blossom
        self.checkBlossom();
        
    #ONLY CALLED ON INIT: original children list generation
    def genCells(self):
        canvasRangeX, canvasRangeY = self.getRange();
        #Limit cell positions to canvas range
        
        childCellSize = self.dim/12;
        #The self.dim is prescribed by construction
        
        #print("[leafnode init genCells]:: childCellSize: ", childCellSize);
        self.children = [Cell(PVector(r,c), childCellSize) for r in canvasRangeX for c in canvasRangeY if (r-self.position.x)%childCellSize ==0 and (c-self.position.y)%(childCellSize)==0];
        self.favoriteChild = self.getFavoriteChild();
        self.checkBlossom();
        
    def getCenterPosition(self):
        return self.position;
    
    def checkBlossom(self):
        
        childCellSize = self.favoriteChild.dim
        if childCellSize >= 12 and childCellSize%12 == 0:
            self.blossom();
    
    def blossom(self):
        self.__class__ = Canvas;
        for i, child in enumerate(self.children):
            if i in self.pattern:
#                 #print(i, "blossom", child.position, child.dim);
                child.__class__ = CanvasLeaf;
                child.genPattern();
                child.pickRandomTarget();
                child.genCells();
        self.favoriteChild = self.getFavoriteChild();

            
    def assembleChildren(self):
        if cellInBounds(self):
            self.genCells();
            children = [child for (i,child) in enumerate(self.children) if i in self.pattern];
            return children;
        else:
            return [];
    
    #Creates a list of integers corresponding to indices in the cellList
    def genPattern(self):
        pA = patternA();
        self.pattern = [coordToOrder(i,12) for i in pA];
    
    #Selects a random integer from the pattern, a list of integers
    #Returns a cell in canvas that is the center for all canvi
    def pickRandomTarget(self):
        spaceSize = len(self.pattern);
        self.centerInOrder = self.pattern[int(floor(random()*spaceSize))];  
    
    def getFavoriteChild(self):
        return self.children[self.centerInOrder];
        
        
        
#Middle Nodes in tree/ root node after first blossom
class Canvas(CanvasLeaf):
    #A Cell has a position, size. Use hasattr to determine if cell is a canvas
    
    def __init__(self, position, initialCanvasSize):
        super(Canvas,self).__init__(position,initialCanvasSize);
        
    def assembleChildren(self):
        self.updateChildrenPositions();
        children = [];
        #Update positions of children
        for i,child in enumerate(self.children):
            if i in self.pattern:
                if cellInBounds(child):
                    children.extend(child.assembleChildren());
                    
        return children; 
    
    def updateChildrenPositions(self):
        canvasRangeX, canvasRangeY = self.getRange();
        childCellSize = self.dim/12;
        #Already has children, because it is a canvasLeaf
        childrenPositions  = (PVector(r,c) for r in canvasRangeX for c in canvasRangeY if (r-self.position.x)%childCellSize ==0 and (c-self.position.y)%(childCellSize)==0);
        for i,child in enumerate(self.children):
            try:
                child.position = childrenPositions.next();
            except:
                print("childcellsize: ", childCellSize);
                print(self.position);
                print(childrenPositions.next());
                
        
    def blossom(self):
        for i, child in enumerate(self.children):
            if i in self.pattern:
                child.blossom();
    
    def growChildren(self, amountIncrease):
        for i, child in enumerate(self.children):
            if i in self.pattern:
                if cellInBounds(child):
                    child.growChildren(amountIncrease);
        print("favoriteChildSize: ", self.favoriteChild.dim);
        self.dim = self.favoriteChild.dim *12;
    
             
    def getCenterPosition(self):
        return self.favoriteChild.getCenterPosition();



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

                                                                                                
