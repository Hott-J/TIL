from collections import deque

s,e=map(int,input().split())
m=10000

chk=[0]*(m+1)
dis=[0]*(m+1)

chk[s]=1
dQ=deque()
dQ.append(s)

while True:
    now=dQ.popleft()
    if now==m:
        break
    for next in (now-1,now+1,now+5):
        if 0<next<=m:
            if chk[next]==0:
                dQ.append(next)
                chk[next]=1
                dis[next]=dis[now]+1

print(dis[e])       
