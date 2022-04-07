from collections import deque

dQ = deque()
N = int(input())
arr = [list(map(int,input().split()))for _ in range(N)]
dx=[1,-1,0,0,1,1,-1,-1]
dy=[0,0,1,-1,-1,1,1,-1]
cnt=0
answer = []

for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            arr[i][j]=0
            dQ.append((i,j))
            cnt = 1
            while dQ:
                now = dQ.popleft()
                for k in range(8):
                    xx = now[0]+dx[k]
                    yy = now[1]+dy[k]
                    if 0<=xx<N and 0<=yy<N and arr[xx][yy]==1:
                        arr[xx][yy]=0
                        cnt+=1
                        dQ.append((xx,yy))
            answer.append(cnt)

print(len(answer))
print(answer)
