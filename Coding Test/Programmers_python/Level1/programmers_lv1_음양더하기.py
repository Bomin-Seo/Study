def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] is True:
            answer += int(absolutes[i])
        else:
            answer -= int(absolutes[i])
    return answer

absolutes = [4,7,12]
signs = [True, False, True]
print(solution(absolutes, signs))