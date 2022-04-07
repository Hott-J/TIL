n = int(input())
a=[]
for _ in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)
s=e=n//2
sum=0

for i in range(n):
    for j in range(s,e+1):
        sum+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(sum)