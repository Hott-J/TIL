def DFS(v):
    if v==m:
        for i in range(v):
            #print(chk[i],end=' ')
            print(res[i],end=' ')
        print()
    else:
        for i in range(n):
            if chk[i]==0:
                chk[i]=1
                res[v]=i+1
                DFS(v+1)
                chk[i]=0

n,m=map(int,input().split())
chk=[0]*n
res=[0]*n
DFS(0)
