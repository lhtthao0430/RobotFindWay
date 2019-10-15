import numpy as np
from Find_Way import Breadth_First_Search as BFS
import draw2Dmap
import draw3Dmap
import InputHandle

m, n, map, sx, sy, gx, gy = InputHandle.textToMap('input.txt')
#print(map)
map = BFS.Breadth_Fist_Search(map,(sx,sy),(gx,gy),m, n)
#draw2Dmap.draw2Dmap(n, m, map)
draw3Dmap.draw3Dmap(m, n, map)