def solution(n, words):
    answer = []
    temp = []
    person, round = 1, 1
    for i in range(len(words)):
        if i == 0:
            temp.append(words[i])
            person += 1
        else:
            if words[i][0] != words[i-1][-1] or len(words[i]) == 1 or words[i] in temp:
                answer.append(person)
                answer.append(round)
                break
            elif i == len(words) - 1:
                return [0, 0]
            else:
                if person % n == 0:
                    person = 0
                    round += 1
                temp.append(words[i])
                person += 1

    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))