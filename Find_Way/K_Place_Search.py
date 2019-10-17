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
        if(c==0):
            t[c][x][y]=2
            return t
        t[c][x][y]=2
        if(x,y)in listPlace:
            e[x][y]=6
            #print(e)
        #print(t[c])
        #print(x,y)
        c=c-1
        x,y,z=theWay[x][y][z]
def K_Place_Search(e,n,m,listPlace,s,f):
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
                    #print("aa1")
                    d=setKthBit(d,j)
                    #print(j,d)
            if(Check_Can_Go(u,v,e,n,m) and isVisit[u][v][d]==0):
                #print(u,v,d)
                isVisit[u][v][d]=c
                h.append(((u,v),c,d))
                theWay[u][v][d]=[x,y,t]

if __name__ == "__main__":
    a=[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
,[1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0]
,[2,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0]
,[3,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0]
,[4,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0]
,[5,0,0,0,1,1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0]
,[6,0,0,0,1,0,0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0]
,[7,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
,[8,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
,[9,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
,[10,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
,[11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
,[12,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]
,[13,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
,[14,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
,[15,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
,[16,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]
,[17,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
,[18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    l=[(1,1)]
    t=K_Place_Search(a,18,22,l,(2,1),(16,19))
    #print(t[0])
    for i in t:print(i)
