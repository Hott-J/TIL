def solution(s):
    answer = True
    if len(s)==4 or len(s)==6:
        for c in s:
            if c=="0":answer=True
            elif c=='1':answer=True
            elif c=='2':answer=True
            elif c=='3':answer=True
            elif c=='4':answer=True
            elif c=="5":answer=True
            elif c=="6":answer=True
            elif c=="7":answer=True
            elif c=="8":answer=True
            elif c=="9":answer=True
            else:
                answer=False
                break
            print(c)
    else:answer=False
    return answer
