def solution(phone_number):
    answer = ""
    for i in range(len(phone_number)):
        if i>=len(phone_number)-4:
            answer+=phone_number[i]
        else:
            answer+="*"
    return answer
