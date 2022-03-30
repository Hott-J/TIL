n = int(input())
scared_arr = list(map(int,input().split()))

scared_arr.sort()

cnt =0 
res = 0

for s in scared_arr:
    cnt += 1
    if s>cnt:
        pass
    else:
        res += 1
        cnt = 0

print(res)