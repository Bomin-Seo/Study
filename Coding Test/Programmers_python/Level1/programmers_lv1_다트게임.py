def solution(dartResult):
    answer = 0
    n = 0
    score_list = []
    score = ''
    for i in dartResult:
        if i.isdigit():
            score += i
            n += 1
        elif i == 'S' or i == 'D' or i == 'T':
            score = int(score)
            if i == 'S':
                score_list.append(score)
                score = ''
            elif i == 'D':
                score_list.append(score ** 2)
                score = ''
            else:
                score_list.append(score ** 3)
                score = ''
        else:
            if i == '*':
                if n == 1:
                    score_list[0] *= 2
                else:
                    score_list[n - 1] *= 2
                    score_list[n - 2] *= 2
            else:
                score_list[n - 1] *= (-1)

    answer = sum(score_list)
    return answer

dartResult = "1D2S#10S"
print(solution(dartResult))