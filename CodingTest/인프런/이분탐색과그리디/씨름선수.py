n = int(input())
t=[]
a=[]
cnt=0
for i in range(n):
    t=list(map(int,input().split()))
    a.append(t)
a.sort(key=lambda x:x[1])

for i in range(n):
    if all (a[i][0]>a[j][0] for j in range(i+1,n)):
        print(a[i])
        cnt+=1

print(cnt)