
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

    #TODO consider a recursive solution: each cell's position depends on changes to one cell (the top left).
    # Each adjacent cell's location and size will depend on the single adjusted cell
    # Change to top left --> no position change, just size change. Update adjacent cell positions. If out of bounds, 
    def updateCells(self,increase):
        for cell in self.cellList:
            cell.dim += increase;
            #cell.position.x+=increase;
            #cell.position.y+=increase;
    
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
        

class CanvasManager:
    def __init__(self, initialCanvas):
        self.canvasList = [initialCanvas];
    
    def update(self, amountIncrease):
        for canvas in self.canvasList:
            canvas.fs += amountIncrease;
            canvas.updateCells(amountIncrease);
            if not canvasInBounds(canvas):
                self.canvasList.remove(canvas);
            else:
            #If the canvas has a large enough figure size
                if canvas.fs > 100:
                    for cell in canvas.cellList:
                        if cellInCanvasBounds(cell,canvas) and not cell.isCanvas:
                            #Create new canvas for this cell
                            cell.isCanvas = True;
                            #initial size, growth rate, canvas size, upperleftcorner
                            self.canvasList.append(Canvas(25, canvas.growthRate, cell.dim, cell.position));
                        #Remove unused cell
                        elif not cell.iscanvas and not cellInCanvasBounds(cell,canvas):
                            canvas.cellList.remove(cell);
        return self.canvasList;
        
def unpack(pvector):
    return (pvector.x,pvector.y);

def cellInCanvasBounds(cell, canvas):
    x,y = unpack(cell.position);
    Cx,Cy = unpack(canvas.upperLeftCorner);
    if not canvasInBounds(canvas):
        return False;
    if inBounds(x,Cx,Cx + canvas.canvasSize) and inBounds(y,Cy,Cy+canvas.canvasSize):
        return True;
    return False;

def canvasInBounds(canvas, maxCanvasSize = 599):
    x,y = unpack(canvas.upperLeftCorner);
    if inBounds(x) and inBounds(y):
        return True;
    dim = canvas.canvasSize;
    if inBounds(x+dim-1) and inBounds(y+dim-1):
        return True;
    return False; #Canvas not in bounds


def inBounds(unit, low=0, up=599):
    if unit >= low and unit <= up:
        return True;
    return False;

                                                                                                