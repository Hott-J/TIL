def solution(s):
    answer = True
    s=s.upper()
    pcnt=0
    ycnt=0
    for c in s:
        if c=="P":pcnt+=1
        if c=="Y":ycnt+=1
    if pcnt==ycnt:answer=True
    else:answer=False
    return answer
