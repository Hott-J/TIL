from collections import deque

N = int(input())
arr = [list(map(int,input().split()))for _ in range(N)]
dQ = deque()
dx = [1,-1,0,0]
dy = [0,0,-1,1]
cnt = 0
temp = 0
res = []
ans = []
res1 = 0

for s in range(100):
    chk = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]>s and chk[i][j]==0:
                chk[i][j]=1
                temp = 1
                dQ.append((i,j))
                while dQ:
                    now = dQ.popleft()
                    for k in range(4):
                        xx = now[0]+dx[k]
                        yy = now[1]+dy[k]
                        if 0<=xx<N and 0<=yy<N and arr[xx][yy]>s and chk[xx][yy]==0:
                            dQ.append((xx,yy))
                            chk[xx][yy]=1
                            #temp +=1
                #res.append(temp)
                cnt+=1
    res1=max(res1,cnt)
    if cnt==0:
        break
print(res1)
#print(ans)