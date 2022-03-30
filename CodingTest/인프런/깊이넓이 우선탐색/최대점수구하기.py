def DFS(v,sum,t):
    global res
    if t>m:
        return
    if v==n:
        if res<sum:
            res=sum
    else:
        DFS(v+1,sum+score[v],t+time[v])
        DFS(v+1,sum,t)

n,m = map(int,input().split())
time=[]
score=[]
res=-2149000000

for i in range(n):
    a,b=map(int,input().split())
    score.append(a)
    time.append(b)
DFS(0,0,0)

print(res)