def solution(n):
    answer = ''
    n = sorted(str(n), reverse=True)
    for i in n:
        answer += i

    return int(answer)

n = 118372
print(solution(n))