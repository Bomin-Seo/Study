def solution(priorities, location):
    answer = 0
    while True:
        if priorities[0] == max(priorities):
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            del priorities[0]
        else:
            temp = priorities.pop(0)
            priorities.append(temp)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer

priorities = [1, 1, 9, 1, 1, 1]
locaton = 0
print(solution(priorities, locaton))