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
        sleep(.1);
    main.execute(growIt);
    #rect(20,0,40,40);

    
class controlCenter:
    def __init__(self):
        self.canvasRoot = CanvasRoot(CANVASSIZE);

    def execute(self, growth):
        drawCells(self.canvasRoot.update(growth));
        return True;


############ DRAWING METHODS ############
#Provide with generator
def drawCells(listOfCells):
    #print('drawing');
    fill(0,255,0,150);
    for i,cell in enumerate(listOfCells):
        #print(i, cell.position);
        rect(cell.position.x,cell.position.y,cell.dim,cell.dim);
  

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
        

        

            
