def solution(s):
    answer = ''
    s = s.lower()
    s.lstrip()

    if s[0].isalpha():
        answer += s[0].upper()
    elif s[0].isdigit():
        answer += s[0]

    for i in range(1, len(s)):
        if s[i-1] == " " and s[i].isalpha():
            answer += s[i].upper()
        else:
            answer += s[i]

    return answer

s = "3people unFollowed me"
print(solution(s))
