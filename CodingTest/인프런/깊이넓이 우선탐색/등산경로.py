from collections import deque

N=int(input())
dQ=deque()
arr = [list(map(int,input().split()))for _ in range(N)]
chk = [[0]*N for _ in range(N)]
s=9999999
e=-999999
dx=[1,-1,0,0]
dy=[0,0,-1,1]

def DFS(x,y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<N and 0<=yy<N and chk[xx][yy]==0 and arr[xx][yy]>arr[x][y]:
                chk[xx][yy]=1
                DFS(xx,yy)
                chk[xx][yy]=0

for i in range(N):
    for j in range(N):
        s=min(s,arr[i][j])
        e=max(e,arr[i][j])

for i in range(N):
    for j in range(N):
        if arr[i][j]==s:
            sx=i
            sy=j
        if arr[i][j]==e:
            ex=i
            ey=j
chk[sx][sy]=1
cnt=0
DFS(sx,sy)
print(cnt)