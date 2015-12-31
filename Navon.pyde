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
    drawCanvas(main.execute());
    #rect(20,0,40,40);

    
class controlCenter:
    def __init__(self):
        self.canvas = Canvas(25,0,canvasSize,PVector(0,0)); 
        # figure size, growth rate, upperLeftCoord, canvasSize

    def execute(self):
        canvasToDraw = self.canvas.execute();
        # A "canvasToDraw" is a list of cells (self.cellList)
        sleep(.1);
        return canvasToDraw;

def drawCanvas(listOfCells):
    fill(0,255,0,191);
    testDraw(listOfCells);
    #for cell in listOfCells:
     #   cellX,cellY = (cell.position.x,cell.position.y);
      #  print(cellX,cellY,cell.dim);
        #rect(cellX,cellY,cell.dim,cell.dim);
        
def testDraw(listOfCells):
    fill(0,255,0,191);
    for cell in listOfCells:
        cellX,cellY = (cell.position.x,cell.position.y);
        if cellX % 50 == 0 and cellY%50 == 0:
            rect(cellX,cellY,cell.dim,cell.dim);