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
import timeit

if __name__ == "__main__":
    m, n, map, sx, sy, gx, gy, k = InputHandle.textToMap('map1.txt')
    start = timeit.default_timer()
    res = Breadth_First_Search.Breadth_First_Search(
        map, (sx, sy), (gx, gy), m, n)
    stop = timeit.default_timer()
    print('map1, BFS, time: ', stop - start)
    if len(res) != 0:
        map = res
    map[sx][sy] = 3
    map[gx][gy] = 4
    map[0, :] = 1
    map[:, 0] = 1
    map[m, :] = 1
    map[:, n] = 1
    draw3Dmap.draw3DMap(m+1, n+1, map, res)
    m, n, map, sx, sy, gx, gy, k = InputHandle.textToMap('map1.txt')
    start = timeit.default_timer()
    res = Depth_First_Search.Depth_First_Search(
        map, (sx, sy), (gx, gy), m, n)
    stop = timeit.default_timer()
    print('map1, DFS, time: ', stop - start)
    if len(res) != 0:
        map = res
    map[sx][sy] = 3
    map[gx][gy] = 4
    map[0, :] = 1
    map[:, 0] = 1
    map[m, :] = 1
    map[:, n] = 1
    draw3Dmap.draw3DMap(m+1, n+1, map, res)
    m, n, map, sx, sy, gx, gy, k = InputHandle.textToMap('map1.txt')
    start = timeit.default_timer()
    res = Two_Side_Search.Two_Side_Search(
        map, (sx, sy), (gx, gy), m, n)
    stop = timeit.default_timer()
    print('map1, TSS, time: ', stop - start)
    if len(res) != 0:
        map = res
    map[sx][sy] = 3
    map[gx][gy] = 4
    map[0, :] = 1
    map[:, 0] = 1
    map[m, :] = 1
    map[:, n] = 1
    draw3Dmap.draw3DMap(m+1, n+1, map, res)        
    m, n, map, sx, sy, gx, gy, k = InputHandle.textToMap('map2.txt')
    start = timeit.default_timer()
    res = Breadth_First_Search.Breadth_First_Search(
        map, (sx, sy), (gx, gy), m, n)
    stop = timeit.default_timer()
    print('map2, BFS, time: ', stop - start)
    if len(res) != 0:
        map = res
    map[sx][sy] = 3
    map[gx][gy] = 4
    map[0, :] = 1
    map[:, 0] = 1
    map[m, :] = 1
    map[:, n] = 1
    draw3Dmap.draw3DMap(m+1, n+1, map, res)
    start = timeit.default_timer()
    res = Depth_First_Search.Depth_First_Search(
        map, (sx, sy), (gx, gy), m, n)
    stop = timeit.default_timer()
    print('map2, DFS, time: ', stop - start)
    if len(res) != 0:
        map = res
    map[sx][sy] = 3
    map[gx][gy] = 4
    map[0, :] = 1
    map[:, 0] = 1
    map[m, :] = 1
    map[:, n] = 1
    draw3Dmap.draw3DMap(m+1, n+1, map, res)
    start = timeit.default_timer()
    res = Two_Side_Search.Two_Side_Search(
        map, (sx, sy), (gx, gy), m, n)
    stop = timeit.default_timer()
    print('map2, TSS, time: ', stop - start)
    if len(res) != 0:
        map = res
    map[sx][sy] = 3
    map[gx][gy] = 4
    map[0, :] = 1
    map[:, 0] = 1
    map[m, :] = 1
    map[:, n] = 1
    draw3Dmap.draw3DMap(m+1, n+1, map, res)        
    m, n, map, sx, sy, gx, gy, k = InputHandle.textToMap('map3.txt')
    start = timeit.default_timer()
    res = Breadth_First_Search.Breadth_First_Search(
        map, (sx, sy), (gx, gy), m, n)
    stop = timeit.default_timer()
    print('map3, BFS, time: ', stop - start)
    if len(res) != 0:
        map = res
    map[sx][sy] = 3
    map[gx][gy] = 4
    map[0, :] = 1
    map[:, 0] = 1
    map[m, :] = 1
    map[:, n] = 1
    draw3Dmap.draw3DMap(m+1, n+1, map, res)
    start = timeit.default_timer()
    res = Depth_First_Search.Depth_First_Search(
        map, (sx, sy), (gx, gy), m, n)
    stop = timeit.default_timer()
    print('map3, DFS, time: ', stop - start)
    if len(res) != 0:
        map = res
    map[sx][sy] = 3
    map[gx][gy] = 4
    map[0, :] = 1
    map[:, 0] = 1
    map[m, :] = 1
    map[:, n] = 1
    draw3Dmap.draw3DMap(m+1, n+1, map, res)
    start = timeit.default_timer()
    res = Two_Side_Search.Two_Side_Search(
        map, (sx, sy), (gx, gy), m, n)
    stop = timeit.default_timer()
    print('map3, TSS, time: ', stop - start)
    if len(res) != 0:
        map = res
    map[sx][sy] = 3
    map[gx][gy] = 4
    map[0, :] = 1
    map[:, 0] = 1
    map[m, :] = 1
    map[:, n] = 1
    draw3Dmap.draw3DMap(m+1, n+1, map, res)        
    pass
