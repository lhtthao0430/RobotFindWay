import numpy as np
dx=[1,0,0,-1,0,0]
dy=[0,-1,1,0,0,0]
dz=[0,0,0,0,1,-1]
def Check_Can_Go(x,y,z,e,n,m,k):
    #if(z!=1): print(e[x][y][z])
    if(x<=0 or x>=n):
        return False
    if(y<=0 or y>=m):
        return False
    if(z<=0 or z>=k):
        return False
    if(e[x][y][z]!=0): 
        return False
    #if(z!=1): print(e[x][y][z])
    return True
def TheWay(e,f,s,n,m,k):
    x,y,z=f
    t=np.full((n+1,m+1,k+1),0)
    while True:
        if((x,y,z)==s):
            t[x][y][z]=2
            return t
        t[x][y][z]=2
        #print(x,y)
        x,y,z=e[x][y][z]
def ThreeD_Search(e,s,f,n,m,k):
    h=[]
    h.append((s,0))
    isVisit=np.full((n+1,m+1,k+1),0)
    theWay=np.full((n+1,m+1,k+1,3),0)
    while True:
        if len(h)==0: 
            return "Can't find the way"
        x,c=h.pop(0)
        #print(x)
        x,y,z=x
        if((x,y,z)==f):
            return TheWay(theWay,f,s,n,m,k)+e
        for i in range(0,6,1):
            u=dx[i]+x
            v=dy[i]+y
            t=dz[i]+z
            #if(t!=1): print(t)
            cost=c+1
            if(Check_Can_Go(u,v,t,e,n,m,k) and isVisit[u][v][t]==0):
                isVisit[u][v][t]=cost
                h.append(((u,v,t),cost))
                theWay[u][v][t]=[x,y,z]
if __name__ == "__main__":
    a=np.full((20,19,21),0)
    t=ThreeD_Search(a,(1,1,1),(1,3,4),19,18,20)
    print(t)