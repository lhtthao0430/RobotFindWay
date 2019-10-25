import numpy as np
from Find_Way import K_Place_Search
import draw2Dmap
import draw3Dmap
import InputHandle
import copy
import timeit

if __name__ == "__main__":
    m, n, map, sx, sy, gx, gy, k = InputHandle.textToMap('map1.txt')
    start = timeit.default_timer()
    res = K_Place_Search.K_Place_Search(
        map, (sx, sy), (gx, gy), m, n, k)
    stop = timeit.default_timer()
    if len(res) != 0:
        cost =  len(res)
        res[:, sx, sy] = 3
        res[:, gx, gy] = 4
        res[:, 0, :] = 1
        res[:, :, 0] = 1
        res[:, m, :] = 1
        res[:, :, n] = 1
        print(cost)
        draw3Dmap.draw3DMapList(m+1, n+1, res, "KPS with map1", stop-start)
    else:
        map[sx, sy] = 3
        map[gx, gy] = 4
        map[0, :] = 1
        map[:, 0] = 1
        map[m, :] = 1
        map[:, n] = 1
        for i in k:
            map[i[0], i[1]] = 6
        draw3Dmap.draw3DMap(m+1, n+1, map, res, "KPS with map1", stop-start)
    m, n, map, sx, sy, gx, gy, k = InputHandle.textToMap('map2.txt')
    start = timeit.default_timer()
    res = K_Place_Search.K_Place_Search(
        map, (sx, sy), (gx, gy), m, n, k)
    stop = timeit.default_timer()
    print('map1, time: ', stop - start)
    if len(res) != 0:
        cost =  len(res)
        res[:, sx, sy] = 3
        res[:, gx, gy] = 4
        res[:, 0, :] = 1
        res[:, :, 0] = 1
        res[:, m, :] = 1
        res[:, :, n] = 1
        print(cost)
        draw3Dmap.draw3DMapList(m+1, n+1, res, "KPS with map2", stop-start)
    else:
        map[sx, sy] = 3
        map[gx, gy] = 4
        map[0, :] = 1
        map[:, 0] = 1
        map[m, :] = 1
        map[:, n] = 1
        for i in k:
            map[i[0], i[1]] = 6
        draw3Dmap.draw3DMap(m+1, n+1, map, res, "KPS with map2", stop-start)
    m, n, map, sx, sy, gx, gy, k = InputHandle.textToMap('map3.txt')
    start = timeit.default_timer()
    res = K_Place_Search.K_Place_Search(
        map, (sx, sy), (gx, gy), m, n, k)
    stop = timeit.default_timer()
    if len(res) != 0:
        cost =  len(res)
        res[:, sx, sy] = 3
        res[:, gx, gy] = 4
        res[:, 0, :] = 1
        res[:, :, 0] = 1
        res[:, m, :] = 1
        res[:, :, n] = 1
        print(cost)
        draw3Dmap.draw3DMapList(m+1, n+1, res, "KPS with map3", stop-start)
    else:
        map[sx, sy] = 3
        map[gx, gy] = 4
        map[0, :] = 1
        map[:, 0] = 1
        map[m, :] = 1
        map[:, n] = 1
        for i in k:
            map[i[0], i[1]] = 6
        draw3Dmap.draw3DMap(m+1, n+1, map, res, "KPS with map3", stop-start)
    pass
