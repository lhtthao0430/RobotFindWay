import numpy as np
dx=[1,0,0,-1]
dy=[0,-1,1,0]
def setKthBit(n,k): 
    return ((1 << k) | n) 

def Check_Can_Go(x,y,e,n,m):
    if(x<=0 or x>=n):
        return False
    if(y<=0 or y>=m):
        return False
    if(e[x][y]!=0): 
        return False
    return True
def TheWay(theWay,f,s,n,m,k,c,e,listPlace):
    x,y=f
    z=k
    #print(k)
    t=np.full((c+1,n+1,m+1),0)
    while True:
        t[c]=e
        if((x,y)==s):
            t[c][x][y]=2
            return t
        t[c][x][y]=2
        if(x,y)in listPlace:
            e[x][y]=6
        #print(t[c])
        #print(x,y)
        c=c-1
        x,y,z=theWay[x][y][z]
def K_Place_Search(e, s,f,n,m,listPlace):
    placeCount=len(listPlace)
    k=int(pow(2,placeCount))-1
    #print(k)
    h=[]
    h.append((s,0,0))
    isVisit=np.full((n+1,m+1,k+1),0)
    theWay=np.full((n+1,m+1,k+1,3),0)
    while True:
        if len(h)==0: 
            return "Can't find the way"
        x,z,t=h.pop(0)
        x,y=x
        if((x,y)==f and t==k):
            return TheWay(theWay,f,s,n,m,k,z,e,listPlace)
            #return "Find the way"
        for i in range(0,4,1):
            u=dx[i]+x
            v=dy[i]+y
            c=z+1
            d=t
            for j in range(0,placeCount,1):
                #print(listPlace[j])
                if(listPlace[j]==(u,v)):
                    d=setKthBit(d,j)
                    #print(j,d)
            if(Check_Can_Go(u,v,e,n,m) and isVisit[u][v][d]==0):
                #print(u,v,d)
                isVisit[u][v][d]=c
                h.append(((u,v),c,d))
                theWay[u][v][d]=[x,y,t]

