import heapq as hq

a=[]

while True:
    n=int(input())
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a))
    if n==-1:
        break
    else:
        hq.heappush(a,n)