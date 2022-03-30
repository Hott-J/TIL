import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    temp=[]
    dq=[]
    for i in range(len(speeds)):
        temp.append(math.ceil((100-progresses[i])/speeds[i]))
    #print(temp)
    for t in temp:
        cnt=len(dq)
        while(True):
            if len(dq)==0:
                cnt=1
                dq.append(t)
                break
            else:
                if dq[-1]<t and max(dq)<t: # max(dq) < t 를 주의
                    for i in range(len(dq)):
                        dq.pop()
                    answer.append(cnt)
                else:
                    cnt+=1
                    dq.append(t)
                    break
    answer.append(cnt)
    return answer
