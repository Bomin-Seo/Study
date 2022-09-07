def solution(numbers):
    answer = ''
    if set(numbers) == {0}:
        return "0"

    numbers = list(map(str, numbers))
    numbers.sort(key= lambda x:x*4, reverse=True)

    for i in numbers:
        answer += i
    return answer


numbers = [1, 11, 110, 1110]

print(solution(numbers))