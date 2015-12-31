from CanvasManager import CanvasManager;
from Cell import Cell

class Canvas:
    
    def __init__(self, initialCellSize = 5, growth = 0, canvasSize = 600,  upperLeftCorner = 0):
        self.growthRate = growth;
        self.fs = initialCellSize;
        self.initial = initialCellSize;
        self.canvasSize = canvasSize; # To indicate current size of canvas
        self.upperLeftCorner = upperLeftCorner;
        # To indicate current position of canvas 
          
        self.genCells(); 
    def execute(self):
        return self.cellList;
        #Step 1 - return a list of coordinates and a size to draw
        #Step 2 - narrow down list of coordinates to just those that are some random subset for now, later representing the letter pattern

        #For all cells in this canvas, move and grow
        #Delete any cells that are off the canvas range
       # self.fs += self.growthRate;
        #self.TFig.update(self.fs);
    def genCells(self):
        x,y = unpack(self.upperLeftCorner);
        canvasRange = range(int(x), int(x) + self.canvasSize);
        # Checked and working: generating range from 0 to 599 (size is 600).

        everyPixel = [(r,c) for r in canvasRange for c in canvasRange];
        # Every 1x1 coordinate in the canvasRange
        
        self.cellList  = [Cell(PVector(r,c),self.fs) for r,c in everyPixel if r%self.fs ==0 and c%(self.fs)==0];
        #Not causing error
        
        return self.cellList;
    
    def lerpCanvas(vector):
        return None;
    
    def getCanvasAsRects(self):
        return ((r,c,self.fs) for r,c in self.cellList if not outOfBounds(r,c,self.fs));
    
    def makeChild(self, particularCell):
        self.child = Canvas(self.initial, self.growthRate, particularCell.position, canvasSize = self.fs);