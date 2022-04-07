def DFS(v,pay):
    global res
    if v>n:
        return
    if v==n:
        if res<pay:
            res=pay
    else:
        DFS(v+t[v],pay+p[v])
        DFS(v+1,pay)

n = int(input())
t=[]
p=[]
for i in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)

res = -2149000000
DFS(0,0)
print(res)