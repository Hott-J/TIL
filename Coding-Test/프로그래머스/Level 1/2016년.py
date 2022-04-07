def solution(a, b):
    day=["FRI","SAT","SUN","MON","TUE","WED","THU"]
    answer = ''
    if a==1:
        date=b-1
        answer=day[date%7]
    elif a==2:
        date=31+b-1
        answer=day[date%7]
    elif a==3:
        date=31+29+b-1
        answer=day[date%7]
    elif a==4:
        date=31+29+31+b-1
        answer=day[date%7]
    elif a==5:
        date=31+29+31+30+b-1
        answer=day[date%7]
    elif a==6:
        date=31+29+31+30+31+b-1
        answer=day[date%7]
    elif a==7:
        date=31+29+31+30+31+30+b-1
        answer=day[date%7]
    elif a==8:
        date=31+29+31+30+31+30+31+b-1
        answer=day[date%7]
    elif a==9:
        date=31+29+31+30+31+30+31+31+b-1
        answer=day[date%7]
    elif a==10:
        date=31+29+31+30+31+30+31+31+30+b-1
        answer=day[date%7]
    elif a==11:
        date=31+29+31+30+31+30+31+31+30+31+b-1
        answer=day[date%7]
    elif a==12:
        date=31+29+31+30+31+30+31+31+30+31+30+b-1
        answer=day[date%7]
    return answer
