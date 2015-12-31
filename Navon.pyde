from Canvas import Canvas
from time import sleep;

canvasSize = 600;
twiceCanvas = canvasSize*2;
def setup():
    size(canvasSize,canvasSize)
    global main
    main = controlCenter();
    background(0);
    noStroke();

def draw():
    global main;
    background(0);
    main.execute();
    #rect(20,0,40,40);

    
class controlCenter:
    def __init__(self):
        canvas = Canvas(25,0,canvasSize,PVector(0,0));
        self.activeCanvi = [canvas];
        # figure size, growth rate, upperLeftCoord, canvasSize

    def execute(self):
        for canvas in self.activeCanvi:
            canvasToDraw = canvas.execute();
            if 
            self.activeCanvi.append(canvas.
            drawCanvas(canvas.execute());
        # A "canvasToDraw" is a list of cells (self.cellList)
        sleep(.1);
        return True;

def drawCanvas(listOfCells):
    testDraw(listOfCells);
        
def realDraw(listOfCells):
    fill(0,255,0,191);
    for cell in listOfCells:
        cellX,cellY = (cell.position.x,cell.position.y);
        print(cellX,cellY,cell.dim);
        rect(cellX,cellY,cell.dim,cell.dim);
                
def testDraw(listOfCells):
    fill(0,255,0,191);
    for cell in listOfCells:
        cellX,cellY = (cell.position.x,cell.position.y);
        if cellX % 50 == 0 and cellY%50 == 0:
            rect(cellX,cellY,cell.dim,cell.dim);