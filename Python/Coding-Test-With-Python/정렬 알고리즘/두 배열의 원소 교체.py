n,k = map(int,input().split())
arr_A = list(map(int,input().split()))
arr_B = list(map(int,input().split()))

arr_A.sort()
arr_B.sort(reverse=True)

for i in range(k):
    if arr_A[i]<arr_B[i]:
        arr_A[i],arr_B[i] = arr_B[i],arr_A[i]
    else:
        break

print(sum(arr_A))