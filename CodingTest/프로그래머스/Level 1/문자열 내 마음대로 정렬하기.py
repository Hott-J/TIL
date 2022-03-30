def solution(strings, n):
    answer = []
    arr=[]
    strings.sort()
    answer=sorted(strings,key=lambda x:x[n])
    return answer
