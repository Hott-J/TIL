from bisect import bisect_left, bisect_right

# 재귀
def binary_search_recursion(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if array[mid]==target:
        return mid
    elif array[mid]<target:
        return binary_search_recursion(array,target, mid+1,end)
    elif array[mid]>target:
        return binary_search_recursion(array,target,start,mid-1)

# 반복문
def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            start = mid + 1
        elif array[mid]>target:
            end = mid - 1
    return None

# bisect 라이브러리
a = [1,2,4,4,8]
x = 4
print(bisect_right(a,x))
print(bisect_left(a,x))


