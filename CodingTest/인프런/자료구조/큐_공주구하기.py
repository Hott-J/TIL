from collections import deque

d = deque()

n,k=map(int,input().split())

for i in range(n):
    d.append(i+1)

while d:
    for i in range(k):
        d.append(d.popleft())
    d.pop()
    if len(d)==1:
        print(d[0])
        d.pop()


