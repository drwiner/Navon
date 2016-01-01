
from Cell import Cell

class Canvas(Cell):
    #A Cell has a position, size. Use hasattr to determine if cell is a canvas
    
    def __init__(self, position, initialCellSize):
        super().__init__(position,initialCellSize);
        self.graduated = False;
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
        x,y = unpack(self.position);
        canvasRange = range(int(x), int(x) + self.canvasSize);
        # Checked and working: generating range from 0 to 599 (size is 600).

        everyPixel = [(r,c) for r in canvasRange for c in canvasRange];
        # Every 1x1 coordinate in the canvasRange
        
        self.cellList  = [Cell(PVector(r,c),self.fs) for r,c in everyPixel if r%self.fs ==0 and c%(self.fs)==0];
        #Not causing error
        
        return self.cellList;
    
    
    def graduationTime(self):
        if self.dim > 100 and not self.graduated:
            return True;
        return False;
        

class CanvasManager:
    #, Canvas(50,0,canvasSize,PVector(0,0))
    def __init__(self, initialSize, totalBoardSpace):
        #On init, generate a single cell for the board, then turn this cell into a canvas, then generate cells for the canvas
        #Canvas created by consuming a cell. Canvas List created with initial cell entry
        self.canvasList = [Canvas(Cell(PVector(0,0),initialSize))];
    
    def update(self, amountIncrease):
        for canvas in self.canvasList:
            #Remove from consideration if canvas isn't on board
            if not canvasInBounds(canvas):
                self.canvasList.remove(canvas);
                continue;
            
            #Establish canvas Size increase.
            canvas.dim += amountIncrease;
            #Propogate increase to cells of canvas
            canvas.updateCells(amountIncrease);
            
            if canvas.graduationTime():
                for cell in canvas.cellList:
                    cell.update(amountIncrease);
                for cell in canvas.cellList:
                    #if the cell is in the canvas bounds (when is it not in bounds?)
                    if cellInCanvasBounds(cell,canvas) and not cell.isCanvas:
                        #Create new canvas for this cell
                        cell.isCanvas = True;
                        #initial size, growth rate, canvas size, upperleftcorner
                        self.canvasList.append(Canvas(25, canvas.growthRate, cell.dim, cell.position));
                    #Remove unused cell
                    elif not cell.iscanvas and not cellInCanvasBounds(cell,canvas):
                        canvas.cellList.remove(cell);
                        
            #If the cells in the canvas are larger than some threshold
            if canvas.dim > 100:
                
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

                                                                                                