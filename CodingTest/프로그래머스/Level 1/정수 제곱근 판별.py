import math

def solution(n):
    answer = 0
    if n%math.sqrt(n)==0:
        answer=(math.sqrt(n)+1)**2
    else:
        answer=-1
    return answer
