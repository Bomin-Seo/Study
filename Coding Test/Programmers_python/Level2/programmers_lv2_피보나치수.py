def solution(n):
    answer = 0
    fibo = [0, 1]
    i = 2
    while i < n + 1:
        temp = fibo[i - 2] + fibo[i - 1]
        fibo.append(temp)
        i += 1

    answer = fibo[-1] % 1234567
    return answer