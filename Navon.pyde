from Canvas import Canvas
from Canvas import CanvasManager
from time import sleep;
from Canvas import unpack;

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
    growIt = 0;
    if keyPressed:
        growIt = 5;
    main.execute(growIt);
    #rect(20,0,40,40);

    
class controlCenter:
    def __init__(self):
        #Create a Canvas Manager by passing an initial Canvas
        self.canvasManager = CanvasManager(Canvas(25,0,canvasSize,PVector(0,0)));
        # figure size, growth rate, upperLeftCoord, canvasSize

    def execute(self, growing):
        #Update the canvas manager and pass back a list of active canvi
        activeCanvi = self.canvasManager.update(growing);
        for canvas in activeCanvi:
            drawCanvas(canvas.execute(),canvas.fs);
            #canvas.execute() returns a list of cells
        sleep(.1);
        return True;

def drawCanvas(listOfCells,cellSize):
    testDraw2(listOfCells, cellSize);
        
def realDraw(listOfCells):
    fill(0,255,0,191);
    for cell in listOfCells:
        cellX,cellY = unpack(cell.position);
        print(cellX,cellY,cell.dim);
        rect(cellX,cellY,cell.dim,cell.dim);
                
def testDraw(listOfCells, cellSize):
    fill(0,255,0,191);
    for cell in listOfCells:
        cellX,cellY = unpack(cell.position);
        if cellX % (cellSize*2) == 0 and cellY%(cellSize*2) == 0:
            rect(cellX,cellY,cell.dim,cell.dim);

def testDraw2(listOfCells, cellSize):
    fill(0,255,0,191);
    drawIt = True;
    lastX = 0;
    for cell in listOfCells:
        cellX,cellY = unpack(cell.position);
        if  cellX > lastX:
            if not drawIt:
                drawIt = True;
            else:
                drawIt = False;
            lastX = cellX;
        if drawIt:
            rect(cellX,cellY,cell.dim,cell.dim);
            drawIt = False;
        else:
            drawIt = True;
       # print(cellX,cellY);
            