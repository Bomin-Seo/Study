def winning(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    correct, unknown = 0, 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            unknown += 1
        elif lottos[i] in win_nums:
            correct += 1
        else:
            continue

    best = winning(correct + unknown)
    worst = winning(correct)
    answer = [best, worst]

    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos, win_nums))