from bisect import bisect_left,bisect_right

n,x = map(int,input().split())
arr = list(map(int,input().split()))

right_index = bisect_right(arr,x)
left_index = bisect_left(arr,x)

if right_index - left_index > 0 :
    print(right_index - left_index)
else:
    print(-1)