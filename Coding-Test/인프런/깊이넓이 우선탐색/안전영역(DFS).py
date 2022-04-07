import sys
sys.setrecursionlimit(10**6) # 이렇게 해야 에러 안뜸, python3로 채점할 것

N = int(input())
arr = [list(map(int,input().split()))for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
res = 0

def DFS(x,y,s):
    chk[x][y]=1
    for k in range(4):
        xx = x+dx[k]
        yy = y+dy[k]
        if 0<=xx<N and 0<=yy<N and chk[xx][yy]==0 and arr[xx][yy]>s:
            DFS(xx,yy,s)

for s in range(100):
    chk = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if chk[i][j]==0 and arr[i][j]>s:
                cnt+=1
                DFS(i,j,s)
    res = max(res,cnt) 
    if  cnt == 0:
        break

print(res)
