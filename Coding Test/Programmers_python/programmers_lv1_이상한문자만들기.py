def solution(s):
    answer = ''
    check = 0
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
            check = 0
        else:
            if check % 2 == 0:
                answer += s[i].upper()
                check += 1
            else:
                answer += s[i].lower()
                check += 1

    return answer