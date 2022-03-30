n = int(input())
a=[]
for _ in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)
m = int(input())

for _ in range(m):
    s,d,r = map(int,input().split())

    if d==0:
        for _ in range(r):
            a[s-1].append(a[s-1].pop(0))
    else:
        for _ in range(r):
            a[s-1].insert(0,a[s-1].pop())

s=0
e=n-1
sum=0
for i in range(n):
    for j in range(s,e+1):
        sum+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(sum)