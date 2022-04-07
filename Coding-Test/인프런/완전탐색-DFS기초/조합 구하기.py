def DFS(v,s):
    if v==m:
        for i in range(m):
            print(res[i],end=' ')
        print()
    else:
        for i in range(s,n):
            res[v]=i+1
            DFS(v+1,i+1)

n,m = map(int,input().split())
chk=[0]*n
res=[0]*n
DFS(0,0)