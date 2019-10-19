import numpy as np
from Find_Way import Breadth_First_Search
from Find_Way import Depth_First_Search
from Find_Way import K_Place_Search
from Find_Way import Moving_Search
from Find_Way import Two_Side_Search
import draw2Dmap
import draw3Dmap
import InputHandle
import copy

m, n, map, sx, sy, gx, gy = InputHandle.textToMap('1.txt')
print(map)
#map = BFS.Breadth_Fist_Search(map,(sx,sy),(gx,gy),m, n)
#draw2Dmap.draw2Dmap(n, m, map)
#draw3Dmap.draw3Dmap(m, n, map)
maps = Breadth_First_Search.Breadth_First_Search(map,(sx,sy),(gx,gy), m, n)
#maps = Moving_Search.Moving_Search(map, (sx, sy), (gx,gy),m, n)
#maps = K_Place_Search.K_Place_Search(map, (sx,sy), (gx,gy), m, n, [(1,1), (1,15), (10,2), (15,15)])
# for map in maps:
#    map[gx][gy] = 4
draw3Dmap.draw3DMap(m, n, maps)

