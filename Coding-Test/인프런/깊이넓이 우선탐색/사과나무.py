from collections import deque

n = int(input())
arr=[[0]*n for _ in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().split()))
#arr=[list(map(int, input().split())) for _ in range(n)]
chk=[[0]*n for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,-1,1]
chk[n//2][n//2]=1
dQ=deque()
dQ.append((n//2,n//2))
cnt=0
apple=arr[n//2][n//2]

while True:
    #now = dQ.popleft()
    if cnt==n//2:
        break
    s=len(dQ)
    for i in range(s):
        now = dQ.popleft()
        for j in range(4):
            x=now[0]+dx[j]
            y=now[1]+dy[j]
            if chk[x][y]==0:
                apple+=arr[x][y]
                #print(arr[x][y],end=' ')
                chk[x][y]=1
                dQ.append((x,y))
    cnt+=1

print(apple)

