def solution(price, money, count):
    answer = 0
    n = 0
    while count != 0:
        n += 1
        money -= price * n
        count -= 1

    if money < 0:
        answer = (-1) * money
    return answer

price, money, count = 3, 20, 4
print(solution(price, money, count))