def solution(x):
    answer = True
    temp = 0
    for i in str(x):
        temp += int(i)

    if x % temp != 0:
        answer = False
    return answer