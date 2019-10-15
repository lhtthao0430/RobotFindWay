import numpy as np 
import time
def drawLine(map, x1, y1, x2, y2):
	if x1 == x2 and y1 == y2:
		map[x1][y1]=1
		return map
	if abs(x1-x2) < 2 and abs(y1-y2) < 2:
		map[x1][y1]=1
		map[x1][y2]=1
		map[x2][y1]=1
		map[x2][y2]=1
		return map
	res = drawLine(map, x1, y1, (x1+x2)//2, (y1+y2)//2)
	res = drawLine(res, (x1+x2)//2, (y1+y2)//2, x2, y2)
	return res

def textToMap(fileName):
	input = open("input.txt", "r")
	m, n = input.readline().split(",")
	m = int(m)
	n = int(n)
	sx, sy, gx, gy = input.readline().split(",")
	sx = int(sx)
	sy = int(sy)
	gx = int(gx)
	gy = int(gy)
	t = input.readline()
	t = int(t)
	map = np.full((m+1, n+1), 0)
	for i in range (0, t):
		temp = input.readline().split(",")
		for j in range(0, len(temp), 2):
			map = drawLine(map, int(temp[j-2]), int(temp[j-1]), int(temp[j]), int(temp[j+1]))
	return m, n, map, sx, sy, gx, gy