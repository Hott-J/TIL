from collections import deque

arr=[]
dQ = deque()
M,N,H = map(int,input().split())
arr = [[list(map(int,input().split()))for _ in range(N)]for _ in range(H)]
#print(arr)
dx = [1,-1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]
answer = 0

for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j]==1:
                dQ.append((k,i,j,0))
while dQ:
    now = dQ.popleft()
    for k in range(6):
        zz = now[0]+dz[k]
        xx = now[1]+dx[k]
        yy = now[2]+dy[k]
        #zz = now[2]+dz[k]
        day = now[3]+1
        if 0<=xx<N and 0<=yy<M and 0<=zz<H and arr[zz][xx][yy]==0:
            arr[zz][xx][yy]=1
            answer = day
            dQ.append((zz,xx,yy,day))

flag = 1

for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j]==0:
                flag = 0
if flag==1:
    print(answer)
else:
    print(-1)