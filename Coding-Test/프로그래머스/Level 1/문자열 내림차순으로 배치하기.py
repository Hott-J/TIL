def solution(s):
    answer = ''
    temp=sorted(s)
    temp.reverse()
    for str in temp:
        answer+=str
    return answer
