def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer+=int(a[i])*int(b[i])
    return answer
