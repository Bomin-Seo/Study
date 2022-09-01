def solution(s, n):
    answer = ''
    for i in s:
        if ord(i) in range(65, 91):
            i = chr((ord(i) + n - 65) % 26 + 65)
            answer += i
        elif ord(i) in range(97, 123):
            i = chr((ord(i) + n - 97) % 26 + 97)
            answer += i
        else:
            answer += i
    return answer

s = "z"
n = 1
print(solution(s, n))