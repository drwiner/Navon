
class Canvas:
    
    def __init__(self, initialCellSize = 5, growth = 0, canvasSize = 600,  upperLeftCorner = 0):
        self.growthRate = growth;
        self.fs = initialCellSize;
        self.initial = initialCellSize;
        self.canvasSize = canvasSize; # To indicate current size of canvas
        if (upperLeftCorner == 0):
            self.upperLeftCorner = PVector(0,0); # To indicate current position of canvas
        else:
            self.upperLeftCorner = upperLeftCorner;
        #genCells(self, upperLeftCorner);
    def execute(self):
        #Step 1 - return a list of coordinates and a size to draw
        self.genCells();
        #Step 2 - narrow down list of coordinates to just those that are some random subset for now, later representing the letter pattern
        
        
        #For all cells in this canvas, move and grow
        #Delete any cells that are off the canvas range
       # self.fs += self.growthRate;
        #self.TFig.update(self.fs);
    def genCells(self):
        x,y = self.upperLeftCorner;
        canvasRange = range(int(self.upperLeftCorner.x), int(self.upperLeftCorner.x + self.canvasSize));
        everyPixel = [(r,c) for r in canvasRange for c in canvasRange];
        # for r,c in everyPixel:
        #     if r%self.fs ==0 and c%self.fs ==0:
        #         self.cells[
        #         self.cells[(r,c)] = Cell(r,c,self.fs);
        self.cellList  = [Cell(r,c,self.fs) for r,c in everyPixel if r%self.fs ==0 and c%(self.fs*2)==0];
        return self.cellList;
    
    def lerpCanvas(vector):
        return None;
    
    def getCanvasAsRects(self):
        return ((r,c,self.fs) for r,c in self.cellList if not outOfBounds(r,c,self.fs));
    
    def makeChild(self, particularCell):
        self.child = Canvas(self.initial, self.growthRate, particularCell.position, canvasSize = self.fs);