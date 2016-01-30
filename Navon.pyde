from Canvas import Canvas
from Canvas import CanvasManager
from time import sleep;
from Canvas import unpack;
from random import random;
from math import floor
from Cell import patternA

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
        growIt = 48;
    main.execute(growIt);
    #rect(20,0,40,40);

    
class controlCenter:
    def __init__(self):
        #Create a Canvas Manager by passing an initial Canvas
        self.canvasManager = CanvasManager(50, canvasSize);
        # figure size, growth rate, upperLeftCoord, canvasSize

    def execute(self, growing):
        #Update the canvas manager and pass back a list of active canvi
        activeCanvi = self.canvasManager.update(growing);
        for i, canvas in enumerate(activeCanvi):
            ## THIS IS USEFUL: print(i);
            drawCanvas(canvas.execute(),canvas.dim,canvas.pattern);
            #canvas.execute() returns a list of cells
        #sleep(.1);
        return True;


############ DRAWING METHODS ############
def drawCanvas(listOfCells,cellSize, pattern):
    #testDraw2(listOfCells, cellSize);
    patternDraw(listOfCells,cellSize, pattern);
        
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
    textSize(10);
    colorLevel = 50;
    drawIt = True;
    lastX = 0;
    for cell in listOfCells:
        cellX,cellY = unpack(cell.position);
        #print(cellX,cellY);
        if  cellX > lastX:
            if not drawIt:
                drawIt = True;
            else:
                drawIt = False;
            lastX = cellX;
        if drawIt:
            colorLevel = colorLevel + 2;
            fill(0,255,0,colorLevel);
            rect(cellX,cellY,cell.dim,cell.dim);
            fill(255);
            text(str(cellX) + ' ' + str(cellY),cellX+2,cellY+10);
            drawIt = False;
        else:
            drawIt = True;
        
def randomDraw(listOfCells, cellSize):
    randomCoords = [int(floor(random()*12)) for x in range(0,6)];
    print(randomCoords);
    for i,cell in enumerate(listOfCells):
        if i in randomCoords:
            cellX,cellY = unpack(cell.position);
            fill(0,255,0,191);
            rect(cellX,cellY,cell.dim,cell.dim);
    
def patternDraw(listOfCells, cellSize, pattern):
    textSize(10);
    colorLevel = 50;
    for i,cell in enumerate(listOfCells):
        if i in pattern:
            cellX,cellY = unpack(cell.position);
            colorLevel = colorLevel + 2;
            fill(0,255,0,colorLevel);
            rect(cellX,cellY,cell.dim,cell.dim);
            fill(255);
            #text(str(cellX) + ' ' + str(cellY),cellX+2,cellY+10);
        

        

            
