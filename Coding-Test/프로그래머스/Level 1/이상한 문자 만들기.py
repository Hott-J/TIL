def solution(s):
    answer = ''
    cnt=0
    for st in s:
        if st==" ":
            cnt=0
            answer+=" "
        else:
            cnt+=1
            if cnt%2==0:
                answer+=st.lower()
            else:
                answer+=st.upper()
    return answer
