import numpy as np

dx=[1,0,0,-1]
dy=[0,-1,1,0]
def Check_Can_Go(x,y,e,n,m):
    if(x<=0 or x>=n):
        return False
    if(y<=0 or y>=m):
        return False
    if(e[x][y]!=0): 
        return False
    return True
def TheWay(e,f,s,n,m):
    x,y=f
    t=np.full((n+1,m+1),0)
    while True:
        if((x,y)==s):
            t[x][y]=2
            return t
        t[x][y]=2
        #print(x,y)
        x,y=e[x][y]
def Breadth_First_Search(e,s,f,n,m):
    h=[]
    h.append((s,0))
    isVisit=np.full((n+1,m+1),0)
    theWay=np.full((n+1,m+1,2),0)
    while True:
        if len(h)==0: 
            return []
        x,z=h.pop(0)
        x,y=x
        if((x,y)==f):
            return TheWay(theWay,f,s,n,m)+e
        for i in range(0,4,1):
            u=dx[i]+x
            v=dy[i]+y
            t=z+1
            if(Check_Can_Go(u,v,e,n,m) and isVisit[u][v]==0):
                isVisit[u][v]=t
                h.append(((u,v),t))
                theWay[u][v]=[x,y]

