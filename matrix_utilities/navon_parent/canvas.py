#canvas and canvi_vector
#Vector({0,...,n},{0:{B1},1:{C1,C2,C3,C4},2:{D1,D2,D3....})

from vecutil import *
from random import shuffle
from math import floor
MAXBOUND = 2000
MINBOUND = 0
LETTER_PATTERN_LENGTH = 12

ALIST = [(5,0),(6,0),(5,1),(6,1),(4,2),(5,2),(6,2),(7,2),(4,3),(5,3),(6,3),(7,3),(3,4),(4,4),(7,4),(8,4),(3,5),(4,5),(7,5),(8,5),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6),(9,6),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7),(9,7),(1,8),(2,8),(9,8),(10,8),(1,9),(2,9),(9,9),(10,9),(0,10),(1,10),(10,10),(11,10),(0,11),(1,11),(10,11),(11,11)]

CLIST = [(0,4),(0,5),(0,6),(0,7),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(2,2),(2,3),(2,4),(2,7),(2,8),(2,9),(3,1),(3,2),(3,3),(3,8),(3,9),(3,10),(4,0),(4,1),(4,2),(4,9),(4,10),(4,11),(5,0),(5,1),(6,0),(6,1),(7,0),(7,1),(8,0),(8,1),(5,11),(5,10),(6,11),(6,10),(7,11),(7,10),(8,11),(8,10),(9,11),(9,10),(9,9),(10,10),(10,9),(10,8),(9,0),(9,1),(9,2),(9,3),(9,8),(10,1),(10,2),(10,3)]

TLIST = [(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(1,2),(10,2),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9),(6,10),(3,10),(4,9),(4,10),(7,9),(7,10),(8,10)]

LETTER_DICT = {'A':ALIST,'C':CLIST,'T':TLIST}

def canviGen(canvi_vec, i, letter_list, prior_letter_pos):
	"returns Vector of canvi lists"
	"Vector({0,...,n},{0:[Canvas()],1:[Canvas(),...,Canvas()],...,n:[Canvas(),...,]})"
	if i  < 0:
		return canvi_vec
	else:
		if i not in canvi_vec.D:
			canvi_vec.D.add(i)
		this_letter_pos = getNextLetterPos(prior_letter_pos,len(letter_list))
		canvi_vec[i] = makeLevel(canvi_vec[i+1],letter_list[this_letter_pos],this_letter_pos)
		return canviGen(canvi_vec,i-1,letter_list, this_letter_pos)
		
def getAnyItem(some_set_or_list):
	return next(iter(some_set_or_list))
	#shuffle(some_set_or_list)
	#for item in some_set_or_list:
		#print('itemSize: ', item.cell_size)
		#return item

def getNextLetterPos(pos, num_levels):
        if pos >= num_levels-1:
            return 0
        else:
            return pos + 1
		
def makeLevel(composite,letter,letter_pos):
	"Input: list of canvi, letter"
	"returns primitive canvi list"
	coords = canviList2coords(composite)
	#shuffle(composite)
	parent_canvas = getAnyItem(composite)
	new_size =  parent_canvas.cell_size / LETTER_PATTERN_LENGTH
	return [Canvas(top_left,new_size,letter,letter_pos) for top_left in coords if inView(top_left,new_size)]


def inView(vector,cell_size):
	x = vector[0]
	y = vector[1]
	return x > -cell_size and y > -cell_size and x < MAXBOUND and y < MAXBOUND
	
def pushLevel(canvi_vec, letter_list, primitive_canvas):
	next_pos = getNextLetterPos(primitive_canvas.letter_pos, len(letter_list))
	next_letter = letter_list[next_pos]
	canvi_vec = upshift(canvi_vec)
	canvi_vec[0] = makeLevel(canvi_vec[1],next_letter,next_pos)
	return canvi_vec
	
def upshift(canvi_vec):
	k = len(canvi_vec.D)
	canvi_vec.D.add(k)
	for i in reversed(range(k)):
		canvi_vec[i+1] = canvi_vec[i]
	return canvi_vec
	
def popLevel(canvi_vec):
	k = len(canvi_vec.D)
	canvi_vec[k-1] = []
	canvi_vec.D.remove(k-1)
	return canvi_vec
	
def chooseCenter(canvi_vec):
	"Returns any canvas position from 2nd most composite level"
	k = len(canvi_vec.D)-2
	#top_level = updateBounds(canvi_vec[k])
	top_level = canvi_vec[k]
	"TODO: auto update when checking in_bounds"
	if len(top_level) > 0:
		for potential_center in top_level:
			if potential_center.in_bounds:
				if potential_center.checkInBounds():
					return potential_center
				else:
					potential_center.in_bounds = False
		
def choosePrimitive(canvi_vec):
	for canvas in canvi_vec[0]:
		if inView(canvas.top_left,canvas.cell_size):
			return canvas

def canviList2coords(C):
	"Input: list of canvi"
	"Returns list of coords"
	coords = []
	for c in C:
		if c.in_view:
			if inView(c.top_left,c.cell_size):
				if c.coords is None:
					c.canvas2Coords()
				for coord in c.coords:
					coords.append(coord)
			#else:
				#c.in_view = False
				#print(coord)
	return coords

#Call this for dilation
def canviVec2coords(C):
	"Input: a vector of lists of canvi"
	"Returns list of coords/vectors"
	coords = []
	#for each layer in hierarchy
	for c in C.D:
		for coord in canviList2coords(C[c]):
			coords.append(coord)
	return coords
	
def coords2points(C):
	pts = []
	for c in C:
		pts.append(vec2point(c))
	return pts
	
def canviVec2points(C):
	"Input: a vector of lists of canvi"
	"Returns a set of (x,y) points"
	return coords2points(canviVec2coords(C))
	
def canviList2points(C):
	return coords2points(canviList2coords(C))
		
	
def updateBounds(C):
	"Input: list 'C' of canvi"
	"Returns list with updated Canvi"
	for c in C:
		c.checkInBounds()
	return C
	
def vec2point(vector):
	return (vector[0],vector[1])
	
def dilateVectors(C, center, scale_factor, translate_rate):
	"Input: canvi_vec"
	"Returns canvi_vec with updated scaling and translation"
	#print(C.D)
	k = len(C.D)
	print(k)
	for level in reversed(range(k)):
		for canvas in C[level]:
			if canvas.in_view:
				if inView(canvas.top_left, canvas.cell_size):
					canvas.top_left = dilate(canvas.top_left, center, scale_factor)
					canvas.top_left = canvas.top_left + translate_rate
					canvas.cell_size = canvas.cell_size*scale_factor
				else:
					canvas.in_view = False
					#C[level].remove(canvas)
	return C
	

class Canvas():
	def __init__(self, top_left, cell_size, letter, letter_pos):
		self.top_left = top_left
		self.letter = letter
		self.letter_pos = letter_pos
		self.cell_size = cell_size
		self.in_bounds = True
		self.in_view = True
	
	def __getattr__(self,name): 
		"TODO: test that this lazy attribute setting works"
		if name is 'coords':
			self.canvas2Coords()
			return self.coords
		
	def canvas2Coords(self):
		"return list of coords from letter, displaced by top_left of this"
		"TODO: have dictionary of 'letter: coord' displacements"
		self.coords = []
		internal_size = self.cell_size/LETTER_PATTERN_LENGTH
		for (x,y) in LETTER_DICT[self.letter]:
			new_x = self.top_left[0] + (x*internal_size)
			new_y = self.top_left[1] + (y*internal_size)
			self.coords.append(Vec({0,1},{0:new_x,1:new_y}))
		return self.coords
		
	def checkInBounds(self):
		x = self.top_left[0]
		y = self.top_left[1]
		if x < MINBOUND or y < MINBOUND or x > MAXBOUND or y > MAXBOUND:
			self.in_bounds = False
		return self.in_bounds
		
class Center:
	#def __init__(self, top_left, cell_size, letter):
	#	super().__init__(self,top_left,cell_size,letter)
	#	self.calculateTranslateRate()
		
	def __init__(self, canvas,growth_rate):
		self.canvas = canvas
		self.calculateTranslateRate(growth_rate)
	
	def calculateTranslateRate(self,growth_rate):
		"returns amount to translate for the center"
		sizeDiff = self.canvas.cell_size
		#print(sizeDiff)
		dis = self.canvas.top_left[0]
		translate_rate =  (-1)* ((dis*growth_rate)/sizeDiff)
		self.translate_rate = Vec({0,1},{0:translate_rate,1:translate_rate})
		#print('translate_rate: ', self.translate_rate)

		
class Canvas_Level:
	def __init__(self, list_of_canvi,letter):
		self.canvi = list_of_canvi
		self.letter = letter
	
	@classmethod
	def fromCoordSet(coords,new_size):
		self.canvi = [Canvas(top_left,new_size,letter) for top_left in coords if inView(top_left,new_size)]
		
		