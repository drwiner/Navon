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
    
    
    # twiceCanvasRange = range(-twiceCanvas,twiceCanvas);
    # #for i in twiceCanvasRange:
    #  #   if j %fs ==0;
    
    # for j in twiceCanvasRange:
    #    if j %tf==0:
    #         [rect(j+x,i+y,fs,fs) for i in twiceCanvasRange if i%tf==0];
    #    elif j%fs==0:
    #        [rect(j+x,i+y+fs,fs,fs) for i in twiceCanvasRange if i%tf==0];
           #for i in twiceCanvasRange:
            #   if i%tf==0:
             #      print('x: ', j+x-(fs/5.0), ' y: ', i+y-(fs/5.0));
           #[print(j+x-(fs/5.0),i+y-(fs/5.0),fs,fs) for i in twiceCanvasRange if i%tf==0];
    
    # fill(0,100,100,100);
    # for j in twiceCanvasRange:
    #    if j %twiceTenthFig==0:
    #         [rect(j+x,i+y,tenthFig,tenthFig) for i in twiceCanvasRange if i%twiceTenthFig==0];
    #    elif j%tenthFig==0:
    #        [rect(j+x,i+y+tenthFig,tenthFig,tenthFig) for i in twiceCanvasRange if i%twiceTenthFig==0];

    #fill(255,0,0,191);
    #print(x,y);
    #print('figSize: ' , fs);
    #rect(quintileFig + x-(fs/5.0),(quintileFig + y)-(fs/5.0),fs,fs);