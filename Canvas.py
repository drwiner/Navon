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
        #self.pickRandomTarget();
        
    def execute(self):
        return self.cellList;
        #Step 1 - return a list of coordinates and a size to draw
        #Step 2 - narrow down list of coordinates to just those that are some random subset for now, later representing the letter pattern
                
    ### CALLED in INIT ###
    def genCells(self):
        canvasRangeX = self.getRangeX();
        canvasRangeY = self.getRangeY();
        # Checked and working: generating range from 0 to 599 (size is 600).
        self.cellList  = [Cell(PVector(r,c),self.childCellSize) for r in canvasRangeX for c in canvasRangeY if (r-self.position.x)%self.childCellSize ==0 and (c-self.position.y)%(self.childCellSize)==0];
        #Creation of cavnas' children, Not causing error
        return self.cellList;
    
    # Each adjacent cell's location and size will depend on the single adjusted cell
    # Change to top left --> no position change, just size change. Update adjacent cell positions. If out of bounds, 
    def updateCells(self,increase):
        if increase > 0:
            print("center, index cellList ", self.center);
            self.lastCenterPosition = self.getCenter().position;
            print("before ", self.lastCenterPosition);
            
            #Two phases: first, calculate displacement of center. subtract from origin. second, calculate journey to top left. Divide journey into bouts of 12 by 12. 
            self.dim += int(increase); # The canvas is now larger.
            distributedIncrease = int(increase/self.numRows); # The increase divided by the number of cells in the row/col. Thus, increase should be dividible into num rows...
            self.childCellSize += distributedIncrease; #The children are larger
            ###############
            #displacement = PVector.sub(self.lastCenterPosition, orderToCoord(self.centerInOrder,12,distributedIncrease));
            self.genCells();
            ###############
            
            #TODO: add new position to center only so that we don't have to gen cells.
            print("displacement ", self.displacement());
            print("new displacement ", displacement);
            self.position.add(self.displacement());
            #Also should add "journey" here. before reupdating cells. Now, what 
            
            ###############
            self.genCells();
            ###############
            print("after ", self.getCenter().position);
            print("new Position ", self.position);
            
            #Replace divided journey with journey that is getting center of canvas (position + 0.5 *canvas.dim) to center of board (boardSize/2,boardSize/2)
            totalJourney = PVector.mult(self.getCenter().position,-1);
            dividedJourney = PVector.div(totalJourney,12);
            dividedJourney.x = floor(dividedJourney.x);
            dividedJourney.y = floor(dividedJourney.y);
            
            print(dividedJourney);
            self.position.add(dividedJourney);
            ###############
            self.genCells();
            ###############
            print("after2 ", self.getCenter().position);
            print("new Position 2 ", self.position);
            

    
    def getCenter(self):
        return self.cellList[self.centerInOrder];
    
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
        
    def displacement(self):
        return PVector.sub(self.lastCenterPosition, self.getCenter().position);

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
        
    def updateCenter(self, amountIncrease):
        #Calculate new position of center
        distributedIncrease = amountIncrease/12;
        
        #The amount that all canvi should be moved, is the amount the center will move
        displacement = PVector.sub(self.center.position,orderToCoord(self.centerInOrder, 12, distributedIncrease));
        
        #The amount to get teh center cell to the center of board
        journey = PVector.sub(PVector(300,300),self.center.position);
        journey.div(12);
        
        return PVector.add(displacement, journey);
        
    
    #THIS IS CALLED EVERY FRAME
    #For each canvas in the set of active canvi being drawn, see if any are out of bounds and remove them.
    #Make increase to canvas size and cells.
    #Check If canvas children should become canvi, and add them if they are in bounds.
    def update(self, amountIncrease):
        
        #TODO: Need to calculate new position of center FIRST, because all updates are made with respect to this. We should be able to calculate this
        
        canviToAdd = [];
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
            if canvas.childCellSize >= 84 and not canvas.grandParent:
                canvas.grandParent = True;
                print("_________________________________________________");
                for i,cell in enumerate(canvas.cellList):
                    if cellInBounds(cell) and i in canvas.pattern:
                    #print(i, ", creating new canvas from cell, its member size is: ", int(floor(canvas.childCellSize/12)),  " and here's the position: ", cell.position, "  and here's the cell.dim ", cell.dim); 
                        # initial cell size should be 1/12 OF the new canvas size. the new canvas size IS the size of the cell.
                        cell = Canvas(cell.position, int(floor(canvas.childCellSize/12)), cell.dim); #This cell is now a canvas. 
                    # print(i, ", after creating, its size is: ", cell.childCellSize,  " and here's the position: ", cell.position, "  and here's the cell.dim ", cell.dim); 
                    canviToAdd.append(cell);
                    #self.canvasList.append(cell); #Added to list of active canvi
            self.canvasList.remove(canvas); 
        #Do not start updating increase for the NEW canvi, doy
        if len(canviToAdd) > 0:
            self.canvasList.extend(canviToAdd);
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

                                                                                                
