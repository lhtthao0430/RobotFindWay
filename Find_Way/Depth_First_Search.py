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
def dfs(e,x,y,n,m,isVisit,TheWay):
    for i in range(0,4,1):
        u=x+dx[i]
        v=y+dy[i]
        if(Check_Can_Go(u,v,e,n,m) and isVisit[u][v]>isVisit[x][y]+1):
            isVisit[u][v]=isVisit[x][y]+1
            TheWay[u][v]=[x,y]
            dfs(e,u,v,n,m,isVisit,TheWay)
def Depth_Fist_Search(e,s,f,n,m):
    isVisit=np.full((n+1,m+1),np.inf)
    theWay=np.full((n+1,m+1,2),0)
    x,y=s
    isVisit[x][y]=0
   
    dfs(e,x,y,n,m,isVisit,theWay)
    x,y=f
    if(isVisit[x][y]==np.inf):
        return "Can't find the way"
    return TheWay(theWay,f,s,n,m)
if __name__ == "__main__":
   a=np.full((18+1,19+1),0)
   t=Depth_Fist_Search(a,(1,1),(10,10),18,19)
   print(t)