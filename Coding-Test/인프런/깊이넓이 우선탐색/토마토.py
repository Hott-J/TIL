from collections import deque

dQ = deque()
M,N = map(int,input().split())
arr = [list(map(int,input().split()))for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
answer = 0

for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            dQ.append((i,j,0))
while dQ:
    now = dQ.popleft()
    for k in range(4):
        xx = now[0]+dx[k]
        yy = now[1]+dy[k]
        day = now[2]+1
        if 0<=xx<N and 0<=yy<M and arr[xx][yy]==0:
            arr[xx][yy]=1
            answer = day
            dQ.append((xx,yy,day))

flag = 1

for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            flag = 0
if flag==1:
    print(answer)
else:
    print(-1)