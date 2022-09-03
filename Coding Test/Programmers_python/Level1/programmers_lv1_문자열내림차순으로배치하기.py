def solution(s):
    answer = ''
    upper_ch = ''
    temp = sorted(s, reverse=True)

    for i in temp:
        if i.islower():
            answer += i
        else:
            upper_ch += i

    answer += upper_ch
    return answer

s = "Zbcdefg"
print(solution(s))