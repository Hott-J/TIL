n,m = map(int,input().split())
dduck = list(map(int,input().split()))

dduck.sort()

start = 0
end = max(dduck)
answer = 0

while start<=end:
    sum = 0
    mid = (start+end)//2
    for d in dduck:
        if d>mid:
            sum += d-mid
            #print(sum)
    if sum>m:
        start = mid +1
    else:
        answer = mid
        end = mid - 1
print(answer)
    