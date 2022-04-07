from collections import deque

d=[]
n,m = map(int,input().split())
n=list(map(int,str(n)))

for x in n:
    while d and m>0 and d[-1]<x:
        d.pop()
        m-=1
    d.append(x)
if m!=0:
    d=d[:-m]
print(d)
res=''.join(map(str,d))
print(res)