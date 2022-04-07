from collections import deque

n=int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dis = [[0]*(n) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

dQ=deque()

arr[0][0]=1
dQ.append((0,0))

while dQ:
    now = dQ.popleft()
    print(now[0],now[1])
    for i in range(4):
        x=now[0]+dx[i]
        y=now[1]+dy[i]
        if 0<=x<=n-1 and 0<=y<=n-1 and arr[x][y]==0:
            arr[x][y]=1
            dQ.append((x,y))
            dis[x][y]=dis[now[0]][now[1]]+1
if dis[n-1][n-1]==0:
    print(-1)
else:
    print(dis[n-1][n-1])
