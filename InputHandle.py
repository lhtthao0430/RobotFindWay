import numpy as np 
import time
from skimage.draw import polygon

def textToMap(fileName):
	input = open(fileName, "r")
	m, n = input.readline().split(",")
	m = int(m)
	n = int(n)
	t = input.readline().split(",")
	k=[]
	if len(t)==4:
		sx = int(t[0])
		sy = int(t[1])
		gx = int(t[2])
		gy = int(t[3])
	elif len(t) > 4:
		sx = int(t[0])
		sy = int(t[1])
		gx = int(t[2])
		gy = int(t[3])
		for i in range(4,len(t),2):
			k.append((int(t[i]),int(t[i+1])))
	t = input.readline()
	t = int(t)
	map = np.full((m+1, n+1), 0)
	for i in range (0, t):
		temp = input.readline().split(",")
		r=[]
		for j in range(0, len(temp), 2):
			r.append(int(temp[j]))
		c=[]
		for j in range(1, len(temp), 2):
			c.append(int(temp[j]))
		r=np.array(r)
		c=np.array(c)
		rr, cc = polygon(r,c)
		map[rr, cc] = i % 4 + 11
		
	return m, n, map, sx, sy, gx, gy, k
