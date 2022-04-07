def solution(seoul):
    answer = ''
    cnt=0
    for s in seoul:
        if s=='Kim':
            break
        else:
            cnt=cnt+1
    answer+="김서방은 "+str(cnt)+"에 있다"
    return answer
