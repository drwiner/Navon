from Canvas import Canvas
from CanvasRoot import CanvasRoot
from time import sleep;
from Canvas import unpack;
from random import random;
from math import floor
from Cell import patternA

CANVASSIZE = 576;
twiceCanvas = CANVASSIZE*2;
def setup():
    size(CANVASSIZE,CANVASSIZE)
    global main
    main = controlCenter();
    background(0);
    noStroke();

def draw():
    global main;
    background(0);
    growIt = 0;
    if keyPressed:
        growIt = 4;
    main.execute(growIt);
    #rect(20,0,40,40);

    
class controlCenter:
    def __init__(self):
        #Create a Canvas Manager by passing an initial Canvas
        self.canvasRoot = CanvasRoot(CANVASSIZE, 44);
        # figure size, growth rate, upperLeftCoord, canvasSize

    def execute(self, growth):
        #Update the canvas manager and pass back a list of active canvi
        self.cellList = self.canvasRoot.update(growth);
        drawCells(self.cellList);
        
#         for i, cell in enumerate(self.cellList):
#             ## THIS IS USEFUL: 
#             #print(i);
#             drawCanvas(canvas.execute(),canvas.dim,canvas.pattern);
            #canvas.execute() returns a list of cells
        #sleep(.1);
        return True;


############ DRAWING METHODS ############
def drawCells(listOfCells):
    while 1:
        try:
            cell = listOfCells.next();
            print(cell.position);
            fill(0,255,0,150);
            rect(cell.position.x,cell.position.y,cell.dim,cell.dim);
        except:
            break;
  

def drawCanvas(listOfCells,cellSize, pattern):
    #testDraw2(listOfCells, cellSize);
    patternDraw(listOfCells,cellSize, pattern);

def patternDraw(listOfCells, cellSize, pattern):
    #listOfCells = the list of cells in a particular canvas
    #cellSize = the size of the canvas. not needed since we draw at every cell position in designated cell size.
    #pattern = a set of indices of the listOfCells for which the shape has its pattern
    textSize(10);
    giveSizeOnce = False;
    colorLevel = 50;
    for i,cell in enumerate(listOfCells):
        if i in pattern:
            cellX,cellY = unpack(cell.position);
            colorLevel = colorLevel + 2;
            fill(0,255,0,colorLevel);
            if not giveSizeOnce:
                #print("cell.dim, ", cell.dim, " canvas.dim, ", cellSize);
                giveSizeOnce = True;
            rect(cellX,cellY,cell.dim,cell.dim);
            fill(255);
            #text(str(cellX) + ' ' + str(cellY),cellX+2,cellY+10);
        

        

            
