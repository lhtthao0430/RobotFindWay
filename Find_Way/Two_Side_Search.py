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
    t=np.full((n,m),0)
    while True:
        if((x,y)==s):
            t[x][y]=1
            return t
        t[x][y]=1
        #print(x,y)
        x,y=e[x][y]
def Two_Side_Search(e,s,f,n,m):
    h=[]
    h.append((s,1))
    h.append((f,2))
    isVisit=np.full((n+1,m+1),0)
    isVisit[s]=1
    isVisit[f]=2
    theWay=np.full((n+1,m+1,2),0)
    while True:
        if len(h)==0: 
            return "Can't find the way"
        x,z=h.pop(0)
        x,y=x
        for i in range(0,4,1):
            u=dx[i]+x
            v=dy[i]+y
            t=z
            if(Check_Can_Go(u,v,e,n,m)and isVisit[u][v]!=0 and isVisit[x][y]!=isVisit[u][v]):
                res=np.full((n,m),0)
                #print(isVisit[u][v])
                #print(isVisit[x][y])
                if(isVisit[x][y]==1):
                    #print(TheWay(theWay,(x,y),s,n,m))
                    #print(TheWay(theWay,(u,v),f,n,m))
                    res=TheWay(theWay,(x,y),s,n,m)+TheWay(theWay,(u,v),f,n,m)
                if(isVisit[x][y]==2):
                    #print(TheWay(theWay,(x,y),f,n,m))
                    #print(TheWay(theWay,(u,v),s,n,m))
                    res=TheWay(theWay,(x,y),f,n,m)+TheWay(theWay,(u,v),s,n,m)
                return res
            if(Check_Can_Go(u,v,e,n,m) and isVisit[u][v]==0):
                isVisit[u][v]=t
                #print(t)
                h.append(((u,v),t))
                theWay[u][v]=[x,y]


if __name__ == "__main__":
   a=np.full((18+1,19+1),0)
   t=Two_Side_Search(a,(1,1),(10,10),18,19)
   print(t)