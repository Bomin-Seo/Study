def solution(brown, yellow):
    answer = []

    temp = (brown - 4) // 2
    width, height = 0, 0
    for i in range(1, temp):
        if i * (temp - i) == yellow:
            if i >= temp - i:
                width, height = i, temp - i
                break

    width += 2
    height += 2

    answer.append(width)
    answer.append(height)
    return answer

brown = 8
yellow = 1
print(solution(brown, yellow))