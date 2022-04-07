n = int(input())
a=[]
dx=[0,0,-1,1]
dy=[1,-1,0,0]

for _ in range(n):
    temp = list(map(int,input().split()))
    temp.insert(0,0)
    temp.append(0)
    a.append(temp)
a.insert(0,[0]*(n+2))
a.append([0]*(n+2))
cnt=0

for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j]>a[i+dx[z]][j+dy[z]] for z in range(4)):
            cnt+=1

print(cnt)
        