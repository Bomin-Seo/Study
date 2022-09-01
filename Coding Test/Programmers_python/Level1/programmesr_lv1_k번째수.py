def solution(array, commands):
    answer = []
    temp = []
    for i in commands:
        for j in range(i[0] - 1, i[1]):
            temp.append(array[j])
        temp = sorted(temp)
        answer.append(temp[i[2] - 1])
        temp = []
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))