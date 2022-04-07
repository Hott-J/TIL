from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    dq=deque()
    sum=0
    for tw in truck_weights:
        while(True):
            if len(dq)==0:
                dq.append(tw)
                sum+=tw
                answer+=1
                break
            elif len(dq)==bridge_length:
                sum-=dq.popleft()
            else:
                if sum+tw>weight:
                    answer+=1
                    dq.append(0)
                else:
                    answer+=1
                    sum+=tw
                    dq.append(tw)
                    break
    return answer+bridge_length
