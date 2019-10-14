import numpy as np
dx=[1,0,0,-1,0]
dy=[0,-1,1,0,0]
def Check_Can_Go(x,y,e,n,m):
    if(x<=0 or x>=n):
        return False
    if(y<=0 or y>=m):
        return False
    if(e[x][y]!=0): 
        return False
    return True
def Moving(e,n,m):
    e1=np.full((n+1,m+1),0)
    #print(e)
    for i in range(0,n,1):
        for j in range(0,m,1):
            e1[i][j+1]=e[i][j]
    #print(e1)
    return e1
def TheWay(theWay,f,s,n,m,e,e1,c):
    x,y=f
    t=np.full((c+1,n+1,m+1),0)
    while True:
        if((x,y)==s):
            #print(c)
            if(c%2==0):
                t[c]=e
            else: 
                t[c]=e1    
            t[c][x][y]=-1
            #print(t[0])
            return t
        if(c%2==0):
           t[c]=e
        else: 
            t[c]=e1    
        t[c][x][y]=-1
        #print(t[c])
        c=c-1
        #print(x,y)
        x,y=theWay[x][y]
     
def Moving_Search(e,s,f,n,m):
    #print(e)
    e1=Moving(e,n,m)
    #print(e)
    #print(e1)
    h=[]
    h.append((s,0))
    isVisit=np.full((n+1,m+1),0)
    theWay=np.full((n+1,m+1,2),0)
    while True:
        if len(h)==0: 
            return "Can't find the way"
        x,z=h.pop(0)
        x,y=x
        if((x,y)==f):
            return TheWay(theWay,f,s,n,m,e,e1,z)
        for i in range(0,5,1):
            u=dx[i]+x
            v=dy[i]+y
            t=z+1
            check=0
            if(t%2==0):
                check=Check_Can_Go(u,v,e,n,m)
            else: 
                check=Check_Can_Go(u,v,e1,n,m)
            if(check==1 and isVisit[u][v]==0):
                isVisit[u][v]=t
                h.append(((u,v),t))
                theWay[u][v]=[x,y]    
if __name__ == "__main__":
   a=np.full((4+1,4+1),0)
   a[3][2]=1
   #print(a)
   t=Moving_Search(a,(1,1),(3,3),4,4)
   print(t)