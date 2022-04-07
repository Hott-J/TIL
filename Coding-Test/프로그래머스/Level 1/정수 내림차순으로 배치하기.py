def solution(n):
    answer = ""
    s=str(n)
    s1=sorted(s,reverse=True)
    for n in s1:
        answer+=n
    answer=int(answer)
    return answer
