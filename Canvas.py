from random import random;
from math import floor
from Cell import Cell
from Cell import patternA
from Cell import coordToOrder

class Canvas(Cell):
    #A Cell has a position, size. Use hasattr to determine if cell is a canvas
    
    def __init__(self, position, initialCellSize, initialCanvasSize):
        super(Canvas,self).__init__(position,initialCanvasSize);
        self.childCellSize = initialCellSize;
        self.genCells();
        self.numRows = int(sqrt(len(self.cellList)));
        self.grandParent = False;
        self.genPattern();
        self.pickRandomTarget();
        
    def execute(self):
        return self.cellList;
        #Step 1 - return a list of coordinates and a size to draw
        #Step 2 - narrow down list of coordinates to just those that are some random subset for now, later representing the letter pattern
                
    ### CALLED in INIT ###
    def genCells(self):
        canvasRange = self.getRange();
        # Checked and working: generating range from 0 to 599 (size is 600).
        self.cellList  = [Cell(PVector(r,c),self.childCellSize) for r in canvasRange for c in canvasRange if r%self.childCellSize ==0 and c%(self.childCellSize)==0];
        #Creation of cavnas' children, Not causing error
        return self.cellList;
    
    # Each adjacent cell's location and size will depend on the single adjusted cell
    # Change to top left --> no position change, just size change. Update adjacent cell positions. If out of bounds, 
    def updateCells(self,increase):
        if increase > 0:
            print("center ", self.centerInOrder);
            self.lastCenterPosition = self.getCenter().position;
            print("before ", self.lastCenterPosition);
            #Two phases: first, calculate displacement of center. subtract from origin. second, calculate journey to top left. Divide journey into bouts of 12 by 12. 
            self.dim += int(increase); # The canvas is now larger.
            distributedIncrease = int(increase/self.numRows); # The increase divided by the number of cells in the row/col. Thus, increase should be dividible into num rows...
            self.childCellSize += distributedIncrease; #The children are larger
            self.updateCellPositions(self.getRange(),distributedIncrease);
            #calculate displacement
            print("after ", self.getCenter().position);
            print("displacement ", self.displacement());
            self.position.add(self.displacement());
            self.updateCellPositions(self.getRange(),0);
            print("after2 ", self.getCenter().position);
            print("new Position ", self.position);
            
    #Returns the cell at index centerInOrder
    
    def updateCellPositions(self, canvasRange, distributedIncrease):
        newPositions = (PVector(r,c) for r in canvasRange for c in canvasRange if (r-self.position.x)%self.childCellSize==0 and (c-self.position.y)%self.childCellSize ==0)
        for cell in self.cellList:
            cell.position = newPositions.next(); 
            #print(cell.position);
            if isinstance(cell,Canvas):
                cell.updateCells(int(distributedIncrease));
            else:
                cell.dim = self.childCellSize;
    
    def getCenter(self):
        return self.cellList[self.centerInOrder];
    
    #Creates a list of integers corresponding to indices in the cellList
    def genPattern(self):
        pA = patternA();
        self.pattern = [coordToOrder(i,12) for i in pA];
    
    #Selects a random integer from the pattern, a list of integers
    def pickRandomTarget(self):
        spaceSize = len(self.pattern);
        self.centerInOrder = self.pattern[int(floor(random()*spaceSize))];
        
    def displacement(self):
        return PVector.sub(self.lastCenterPosition, self.getCenter().position);

class CanvasManager:
    #, Canvas(50,0,canvasSize,PVector(0,0))
    def __init__(self, initialSize, totalBoardSpace):
        #On init, generate a single cell for the board, then turn this cell into a canvas, then generate cells for the canvas
        #Canvas created by consuming a cell. Canvas List created with initial cell entry
        self.canvasList = [Canvas(PVector(0,0),initialSize,totalBoardSpace)]; #Canvas that takes entire board
    
    #For each canvas in the set of active canvi being drawn, see if any are out of bounds and remove them.
    #Make increase to canvas size and cells.
    #Check If canvas children should become canvi, and add them if they are in bounds.
    def update(self, amountIncrease):
        
        #For each canvas in the set of active canvi being drawn,
        #____________________________________
        for canvas in self.canvasList:
            
            #Remove from consideration if canvas isn't on board
            if not cellInBounds(canvas):
                self.canvasList.remove(canvas);
                continue;
            
            #Make increase to canvas size and cells
            #_____________________________________
            #Establish canvas Size increase.
            #Propogate increase to cells of canvas
            canvas.updateCells(amountIncrease);
            
            #Check if canvas children should become canvi, add them if they are in bounds
            #_____________________________________
#             if canvas.childCellSize >= 144 and not canvas.grandParent:
#                 canvas.grandParent = True;
#                 for cell in canvas.cellList:
#                     if cellInBounds(cell):
#                         cell = Canvas(cell.position, 12, cell.dim); #This cell is now a canvas. 
#                         self.canvasList.append(cell); #Added to list of active canvi
#                 self.canvasList.remove(canvas);
                #BECAUSE, the children of this canvas are canvi themselves... so no longer need to draw them, just the grandchildren.
                
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

                                                                                                
