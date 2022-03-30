def solution(arr):
    answer = 0
    for num in arr:
        answer+=num
    answer=answer/len(arr)
    return answer
