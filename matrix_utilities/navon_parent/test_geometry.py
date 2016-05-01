from mat import Mat
import math
from image_mat_util import file2mat
from image_mat_util import mat2display
from geometry_lab import scale

positions,colors  = file2mat('board.png')
#scale_matrix = scale(10,10);
#positions= scale_matrix*positions;
#colors = scale_matrix*colors;
print('before display')
mat2display(positions,colors);
print('it occurred')