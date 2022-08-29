def solution(N, stages):
    answer = []
    fail = [0] * N
    arrive = [0] * N
    rate = []

    for i in range(len(stages)):
        if stages[i] == N + 1:
            for j in range(len(arrive)):
                arrive[j] += 1
        else:
            fail[stages[i] - 1] += 1
            for j in range(stages[i]):
                arrive[j] += 1

    for i in range(len(fail)):
        if arrive[i] == 0:
            rate.append(0)
        else:
            rate.append(fail[i] / arrive[i])

    k = 0
    while k != N:
        max_val = max(rate)
        for i in range(len(rate)):
            if rate[i] == max_val:
                answer.append(i + 1)
                rate[i] = -1
                break
        k += 1
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))