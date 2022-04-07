n,m=map(int,input().split())

a=[]

a=list(map(int,input().split()))

s=0
e=len(a)
a=sorted(a)

for i in range(s,e):
    mid=(s+e)//2
    if a[mid]<m:
        s=mid+1

    elif a[mid]>m:
        e=mid-1

    else:
        print(mid+1)
        break    

