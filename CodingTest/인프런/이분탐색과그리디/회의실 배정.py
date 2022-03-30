n = int(input())
t=[]
a=[]
for i in range(n):
    t=list(map(int,input().split()))
    a.append(t)
a.sort(key=lambda x:x[1])

e=0
cnt=0

for i,j in a:
    if  i>=e:
        e=j
        cnt+=1

print(cnt) 