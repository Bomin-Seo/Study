from itertools import combinations

def solution(numbers):
    answer = []
    temp = list(combinations(numbers, 2))

    for i in temp:
        answer.append(sum(i))

    answer = list(set(answer))
    answer.sort()
    return answer

numbers = [2,1,3,4,1]
print(solution(numbers))