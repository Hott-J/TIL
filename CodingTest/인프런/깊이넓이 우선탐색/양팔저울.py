def DFS(v,w):
    if v==k:
        if w<0:
            w=-w
        res.append(w)
    else:
        DFS(v+1,w+chu[v])
        DFS(v+1,w-chu[v])
        DFS(v+1,w)

k=int(input())
chu=[]
res=[]
chu.extend(list(map(int,input().split())))
DFS(0,0)

cnt=0
for x in set(res):
    cnt+=1

#print(set(res))
#print(cnt)
print(sum(chu)-cnt+1)