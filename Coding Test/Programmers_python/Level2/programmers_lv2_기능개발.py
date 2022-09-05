def solution(progresses, speeds):
    answer = []
    done = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            done.append((100 - progresses[i]) / speeds[i])
        else:
            done.append((100 - progresses[i]) // speeds[i] + 1)

    complete = 1
    for i in range(len(done)):
        if i == len(done) - 1:
            answer.append(complete)
        else:
            if done[i] == -1:
                continue

            for j in range(i+1, len(done)):
                if done[j] != -1 and done[i] >= done[j]:
                    complete += 1
                    done[j] = -1
                else:
                    answer.append(complete)
                    complete = 1
                    break

    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1,1,1,1,1,1]

print(solution(progresses, speeds))