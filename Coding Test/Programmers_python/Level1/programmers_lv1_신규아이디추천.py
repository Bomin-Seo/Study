def solution(new_id):
    possible = [45, 46, 95]
    for i in range(97, 123):
        possible.append(i)

    for i in range(48, 58):
        possible.append(i)
    answer = ""
    new_id = new_id.lower()
    for i in new_id:
        if ord(i) not in possible:
            continue
        else:
            answer += i


    new_id = answer

    answer = "" + new_id[0]

    for i in range(1, len(new_id)):
        if new_id[i] == '.':
            if new_id[i-1] == '.':
                continue
            else:
                answer += new_id[i]
        else:
            answer += new_id[i]

    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[len(answer) - 1] == '.':
        answer = answer[:-1]

    if len(answer) == 0:
        answer = 'a'

    if len(answer) > 15:
        answer = answer[:15]
        if answer[14] == '.':
            answer = answer[:14]

    if len(answer) < 3:
        while len(answer) != 3:
            answer += answer[-1]

    return answer

new_id = "abcdefghijklmn.p"

print(solution(new_id))
