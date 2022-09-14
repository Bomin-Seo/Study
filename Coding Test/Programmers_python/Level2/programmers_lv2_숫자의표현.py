def solution(n):
    answer = 1
    if n == 1 or n == 2:
        return answer

    for i in range(1, (n//2) + 2):
        temp = 0
        for j in range(i, (n//2) + 2):
            temp += j
            if temp == n:
                answer += 1
                break
            elif temp > n:
                break
    return answer

n = 15
print(solution(n))