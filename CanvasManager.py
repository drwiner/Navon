from Canvas import Canvas
class CanvasManager:
    def __init__(self, initialCanvas):
        self.canvasList = [initialCanvas];
    
    def update(self):
        for canvas in self.canvasList:
            if not canvasInBounds(canvas):
                self.canvasList.remove(canvas);
            else:
            #If the canvas has a large enough figure size
                if canvas.fs > 100:
                    for cell in canvas.cellList:
                        if cellInCanvasBounds(cell,canvas) and not cell.isCanvas:
                            #Create new canvas for this cell
                            cell.isCanvas = True;
                            #initial size, growth rate, canvas size, upperleftcorner
                            self.canvasList.append(Canvas(25, canvas.growth, cell.dim, cell.position));
        
def unpack(pvector):
    return (pvector.x,pvector.y);

def cellInCanvasBounds(cell, canvas):
    x,y = unpack(cell.position);
    Cx,Cy = unpack(canvas.upperLeftCorner);
    if not canvasInBounds(canvas):
        return False;
    if inBounds(x,Cx,Cx + canvas.canvasSize) and inBounds(y,Cy,Cy+canvas.canvasSize):
        return True;
    return False;

def canvasInBounds(canvas, maxCanvasSize = 599):
    x,y = unpack(canvas.upperLeftCorner);
    if inBounds(x) and inBounds(y):
        return True;
    dim = canvas.canvasSize;
    if inBounds(x+dim-1) and inBounds(y+dim-1):
        return True;
    return False; #Canvas not in bounds


def inBounds(unit, low=0, up=599):
    if unit >= low and unit <= up:
        return True;
    return False;

                                                                                                