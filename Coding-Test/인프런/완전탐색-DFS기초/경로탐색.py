def DFS(v):
    global cnt
    if v==n:
        cnt+=1
        for x in path:
            print(x,end=' ')
        print()
    else:
        for i in range(1,n+1):
            if arr[v][i]==1 and chk[i]==0:
                chk[i]=1
                path.append(i)
                DFS(i) # 도착지점이므로, i로 한다. v+1은 도착지점이 아니라 깊이가 도착지점 
                chk[i]=0
                path.pop()

n,m=map(int,input().split())

arr = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())
    arr[x][y]=1

cnt=0
chk=[0]*(n+1)
path=[]
path.append(1)
chk[1]=1
DFS(1)

