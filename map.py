import numpy as np
from Find_Way import Breadth_First_Search as BFS

input = open("input.txt", "r")

m, n = input.readline().split(",")
m = int(m)
n = int(n)
s1, s2, g1, g2 = input.readline().split(",")
s1 = int(s1)
s2 = int(s2)
g1 = int(g1)
g2 = int(g2)

polygonNum = input.readline()
polygonList = []
list = []
for i in polygonNum:
    polygon = input.readline().split(",")
    polygonList.append(polygon)

for i in range (0, len(polygonList)):
    for j in range(0, len(polygonList[i])): 
        polygonList[i][j] = int(polygonList[i][j]) 

print(polygonList)
input.close()

map = np.full((n+1, m+1),0)
i = 0
while i < len(polygonList):
    j = 0
    while j <= len(polygonList[i]) - 4:
        print((polygonList[i][j], polygonList[i][j + 1]), (polygonList[i][j + 2], polygonList[i][j + 3]))
        print((n - polygonList[i][j], polygonList[i][j + 1]), (n - polygonList[i][j + 2], polygonList[i][j + 3]))
        map = BFS.Breadth_Fist_Search(map, (n - polygonList[i][j], polygonList[i][j + 1]), (n - polygonList[i][j + 2], polygonList[i][j + 3]), n, m)
        print(map)
        j += 2
    map = BFS.Breadth_Fist_Search(map, (polygonList[i][0], n-polygonList[i][1]), (polygonList[i][len(polygonList[i]) - 1], n-polygonList[i][len(polygonList[i]) - 2]), n, m)
    i += 1
print(map)