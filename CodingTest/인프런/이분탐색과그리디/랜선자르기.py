k,n=map(int,input().split())
a=[]
t=[]
for i in range(k):
    a.append(input())

a=sorted(a)

def count(len):
    cnt=0
    for i in a:
        cnt+=int(i)//len
    return cnt

s=0
e=int(max(a))

for i in range(s,e):
    mid=(s+e)//2
    if count(mid)<n:
        e=mid-1
    elif count(mid)>n:
        s=mid+1
    else:
        print(mid)
        break