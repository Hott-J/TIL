def solution(arr):
    answer = []
    arr1=sorted(arr)
    arr.remove(arr1[0])
    if len(arr)==0:
        answer.append(-1)
    else:
        answer=arr
    return answer
