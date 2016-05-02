#from canvas import Canvas
from vecutil import *
from canvas import *
from time import sleep
MAXBOUND = 1600
MINBOUND = 0
PRIMSIZE = 12
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
        self.has_primitive = False
        self.num_levels = NUM_LEVELS
        #self.letters = ['A' for x in range(NUM_LEVELS) if x%0 is 0]
        self.letters=['C','A','T','C','A','T']
        first_canvas = Canvas(ORIGIN,MAXBOUND,self.letters[0], 0)
        self.createCanviVec(first_canvas,0)
        self.center = chooseCenter(self.canvi_vec)
        self.Center = Center(self.center,GROWTH_RATE)
        self.primitive = choosePrimitive(self.canvi_vec)
        drawCells(self.canvi_vec[0])
    
    def createCanviVec(self,first_canvas,letter_pos):
        first_level = {self.num_levels-1:[first_canvas]}
        first_vec = Vec(set(range(self.num_levels)),first_level)
        self.canvi_vec = canviGen(first_vec, self.num_levels-2, self.letters,letter_pos)

    def execute(self):
        background(0)
        drawCells(self.canvi_vec[0])
        return True;
    
    def grow(self, growth_rate):
        "TODO: 1) Update when letters decompose, should be earlier!  2) Translate via dilateVectors, do math (meh, working fine :)"

        if self.center.cell_size > MAXBOUND:
            print('this occurred')
            self.canvi_vec = popLevel(self.canvi_vec)
            #first_canvas = Canvas(self.center.top_left,self.center.cell_size,self.center.letter,self.center.letter_pos)
            #self.createCanviVec(first_canvas,self.center.letter_pos)
            self.num_levels = self.num_levels - 1
            self.center = chooseCenter(self.canvi_vec)
            self.Center = Center(self.center,GROWTH_RATE)
        
        if self.primitive.cell_size > PRIMSIZE:
            self.num_levels = self.num_levels + 1
            self.canvi_vec = pushLevel(self.canvi_vec, self.letters,self.primitive)
            self.primitive = choosePrimitive(self.canvi_vec)
        
        if self.num_levels <= 2:
            self.primitive = choosePrimitive(self.canvi_vec)
            self.center = chooseCenter(self.canvi_vec)
            self.Center = Center(self.center,GROWTH_RATE)
            print(self.primitive.cell_size, " ", self.center.cell_size)

        self.canvi_vec = dilateVectors(self.canvi_vec,self.center.top_left,growth_rate,self.Center.translate_rate)

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
