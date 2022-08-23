def solution(answers):
    score1, score2, score3 = 0, 0, 0
    answer = []
    for i in range(len(answers)):
        if answers[i] == i % 5 + 1:
            score1 += 1
        if i % 2 == 0:
            if answers[i] == 2:
                score2 += 1
        else:
            if i % 8 == 1 and answers[i] == 1:
                score2 += 1
            elif i % 8 == 3 and answers[i] == 3:
                score2 += 1
            elif i % 8 == 5 and answers[i] == 4:
                score2 += 1
            elif i % 8 == 7 and answers[i] == 5:
                score2 += 1
        if (i % 10 == 0 or i % 10 == 1) and answers[i] == 3:
            score3 += 1
        elif (i % 10 == 2 or i % 10 == 3) and answers[i] == 1:
            score3 += 1
        elif (i % 10 == 4 or i % 10 == 5) and answers[i] == 2:
            score3 += 1
        elif (i % 10 == 6 or i % 10 == 7) and answers[i] == 4:
            score3 += 1
        elif (i % 10 == 8 or i % 10 == 9) and answers[i] == 5:
            score3 += 1

    bestscore = max(score1, score2, score3)

    if bestscore == score1:
        answer.append(1)
    if bestscore == score2:
        answer.append(2)
    if bestscore == score3:
        answer.append(3)
    return answer

answers = [1,2,3,4,5]

print(solution(answers))