from random import random;
from math import floor
from Cell import Cell
from Cell import patternA
from Cell import coordToOrder
from Cell import orderToCoord

class Canvas(Cell):
    #A Cell has a position, size. Use hasattr to determine if cell is a canvas
    
    def __init__(self, position, initialCellSize, initialCanvasSize):
        super(Canvas,self).__init__(position,initialCanvasSize);
        self.childCellSize = initialCellSize;
        self.genCells();
        self.numRows = int(sqrt(len(self.cellList)));
        self.grandParent = False;
        self.genPattern();
        
    def execute(self):
        return self.cellList;
                
    def genCells(self):
        canvasRangeX = self.getRangeX();
        canvasRangeY = self.getRangeY();
        print(self.position, self.dim);
        print("childcellsize: ", self.childCellSize);
        self.cellList  = [Cell(PVector(r,c),self.childCellSize) for r in canvasRangeX for c in canvasRangeY if (r-self.position.x)%self.childCellSize ==0 and (c-self.position.y)%(self.childCellSize)==0];
        print(len(self.cellList));
        return self.cellList;
    
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
        


class CanvasManager:
    #THIS ONLY HAPPENS ON FIRST INIT
    def __init__(self, initialSize, totalBoardSpace):
        #On init, generate a single cell for the board, then turn this cell into a canvas, then generate cells for the canvas
        #Canvas created by consuming a cell. Canvas List created with initial cell entry
        self.canvasList = [Canvas(PVector(0,0),initialSize,totalBoardSpace)]; #Canvas that takes entire board
        self.pickCellFromCanvas();
        
        

    def pickCellFromCanvas(self):
        spaceSize = len(self.canvasList);
        randomCanvas = self.canvasList[int(floor(random() * spaceSize))]; 
        self.center, self.centerInOrder = randomCanvas.pickRandomTarget();
        self.smallSize = self.center.dim;
        self.centerCanvasPosition = randomCanvas.position;

        print(":::::::::::::::::::::::::::::::::::::::::");
        print("center selected: ", self.center.position);
        print("center position in list: ", self.centerInOrder);
        print("size: ", self.center.dim);
        print("canvas position of center : ", self.centerCanvasPosition);
        print("predicted center: ", PVector.add(self.centerCanvasPosition, orderToCoord(self.centerInOrder-1,12,self.center.dim)));
        print(":::::::::::::::::::::::::::::::::::::::::");
        
    #Calculate new position of center
    def updateCenter(self, amountIncrease):
        
        #size of cells
        distributedIncrease = amountIncrease/12;
        self.smallSize = self.smallSize + distributedIncrease;
        #Calculate the size.
        newCenterAfterGrowth = PVector.add(self.center.position, orderToCoord(self.centerInOrder, 12, distributedIncrease));
        #print("before" , self.center.position, " after ", newCenterAfterGrowth);
        
        displacement = PVector.sub(self.center.position, newCenterAfterGrowth);
        
        #The amount to get teh center cell to the center of board
        journey = PVector.sub(PVector(288,288),self.center.position);
        journey.div(12);
        
        #print("Displacement vector, ", displacement, " ", journey, " ", PVector.add(displacement, journey));
        totalDisplacement = PVector.add(displacement,journey);
        totalDisplacement.x = int(floor(totalDisplacement.x));
        totalDisplacement.y = int(floor(totalDisplacement.y));
        
        print("total displacement: ", totalDisplacement);
        #print("centerPosition: ", self.center.position);
        

        newCenter = PVector.add(self.center.position, totalDisplacement)

        #print("centerPosition After: ", newCenter);

        
        return totalDisplacement;
        
    
    #THIS IS CALLED EVERY FRAME
    #For each canvas in the set of active canvi being drawn, see if any are out of bounds and remove them.
    #Make increase to canvas size and cells.
    #Check If canvas children should become canvi, and add them if they are in bounds.
    def update(self, amountIncrease):
        if amountIncrease > 0:
            #TODO: Need to calculate new position of center FIRST, because all updates are made with respect to this. We should be able to calculate this
            canviDisplacement = self.updateCenter(amountIncrease);
            
            canviToAdd = [];
            for canvas in self.canvasList:
                #Remove from consideration if canvas isn't on board
                if not cellInBounds(canvas):
                    self.canvasList.remove(canvas);
                    continue;
                
                
                canvas.updateCells(canviDisplacement,amountIncrease);
                
                if canvas.childCellSize >= 60 and not canvas.grandParent:
                    canvas.grandParent = True;
                    print("_________________________________________________");
                    for i,cell in enumerate(canvas.cellList):
                        if cellInBounds(cell) and i in canvas.pattern:
                            cell = Canvas(cell.position, int(floor(canvas.childCellSize/12)), cell.dim);
                            canviToAdd.append(cell);
                    self.canvasList.remove(canvas);
                    
                    #self.smallSize = int(floor(canvas.childCellSize/12));

            if len(canviToAdd) > 0:
                self.canvasList.extend(canviToAdd);
                #Rule - if the canvas being removed had the center, then the center should be reselected
                self.pickCellFromCanvas();
                
        return self.canvasList;

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

                                                                                                
