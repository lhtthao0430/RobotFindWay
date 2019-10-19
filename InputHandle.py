import numpy as np 
import time
from skimage.draw import line

def textToMap(fileName):
	input = open(fileName, "r")
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
			rr, cc = line(int(temp[j-2]), int(temp[j-1]), int(temp[j]), int(temp[j+1]))
			map[rr, cc] = 1
	return m, n, map, sx, sy, gx, gy
