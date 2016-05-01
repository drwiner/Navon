#from canvas import Canvas
from vecutil import *
from canvas import *
from time import sleep
MAXBOUND = 2000
MINBOUND = 0
NUM_LEVELS = 3
GROWTH_RATE = 1.05
ORIGIN = Vec({0,1},{0:0,1:0})

def setup():
    size(MAXBOUND,MAXBOUND)
    global main
    background(0);
    noStroke();
    main = controlCenter();
    

def draw():
    #global main
    #if keyPressed:
    #sleep(.05)
    #if keyPressed:
    main.grow(GROWTH_RATE)
    main.execute()
    #sleep(.2)24

    
class controlCenter:
    def __init__(self):
        self.has_center = False
        #self.letters = ['A' for x in range(NUM_LEVELS) if x%0 is 0]
        self.letters=['A','A','A']
        
        first_canvas = Canvas(ORIGIN,MAXBOUND,self.letters[NUM_LEVELS-1])
        self.createCanvas(first_canvas)
        drawCells(self.canvi_vec[0])
    
    def createCanvas(self,first_canvas):
        first_level = {NUM_LEVELS-1:[first_canvas]}
        first_vec = Vec(set(range(NUM_LEVELS)),first_level)
        self.canvi_vec = canviGen(first_vec, NUM_LEVELS-2, self.letters)

    def execute(self):
        background(0)
        drawCells(self.canvi_vec[0])
        return True;
    
    def grow(self, rate):
        if self.has_center is False:
            self.center = chooseCenter(self.canvi_vec)
            self.Center = Center(self.center,GROWTH_RATE)
            self.has_center = True
        self.canvi_vec = dilateVectors(self.canvi_vec,self.center.top_left,GROWTH_RATE,self.Center.translate_rate)
        if self.center.cell_size > MAXBOUND:
            first_canvas = Canvas(self.center.top_left,self.center.cell_size,self.letters[NUM_LEVELS-1])
            self.createCanvas(first_canvas)
            self.has_center = False
            #print("adding level")
            
        #self.canvi_vec = addLevel(self.canvi_vec,'A',self.center)
            #print('len top level: ', len(self.canvi_vec[2]))
            #print('len second level: ', len(self.canvi_vec[1]))
            #print('len prim level: ', len(self.canvi_vec[0]))
        

############ DRAWING METHODS ############

def drawCells(listOfCells):
    fill(0,255,0,150);
    for cell in listOfCells:
        rect(cell.top_left[0],cell.top_left[1],cell.cell_size,cell.cell_size);
        

def testCanviVec(canvi_vec, num_levels):
    for i in range(num_levels):
        print(i)
        print(canvi_vec[i][0].top_left)
        print(canvi_vec[i][0].cell_size)
