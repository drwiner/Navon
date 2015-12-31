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
        self.canvas = Canvas(5,5,canvasSize,PVector(0,0)); 
        # figure size, growth rate, upperLeftCoord, canvasSize

    def execute(self):
        canvasToDraw = self.canvas.execute();
        sleep(.1);
        return canvasToDraw;

def drawCanvas(listOfCells):
    fill(0,255,0,191);
    for cell in listOfCells:
        cellX,cellY = cell.position;
        rect(cellX,cellY,cell.dim);