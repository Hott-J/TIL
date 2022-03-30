def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if ord(s[i])+n>ord('z'):
            answer+=chr(ord('a')+n-ord('z')+ord(s[i])-1)
        elif s[i]==' ':
            answer+=' '
        elif ord(s[i])+n>ord('Z') and ord(s[i])<ord('a'):
            answer+=chr(ord('A')+n-ord('Z')+ord(s[i])-1)
        else:
            answer+=chr(ord(s[i])+n)
    return answer
