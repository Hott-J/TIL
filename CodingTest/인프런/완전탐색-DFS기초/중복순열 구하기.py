def DFS(v):
    global cnt
    if v==m:
        cnt+=1
        for i in range(m):
            print(res[i],end=' ')
        print()
    else:
        for i in range(1,n+1):
            res[v]=i
            DFS(v+1)
    
n,m=map(int,input().split())
res=[0]*m
cnt=0
DFS(0)
print(cnt)
