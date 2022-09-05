def solution(record):
    answer = []
    dic = {}
    for i in record:
        if i[0] == 'E' or i[0] == 'C':
            act, uid, nickname = map(str, i.split())
            dic[uid] = nickname

    for i in record:
        if i[0] == 'E':
            act, uid, nickname = map(str, i.split())
            temp = dic[uid] + "님이 들어왔습니다."
            answer.append(temp)
        elif i[0] == "L":
            act, uid = map(str, i.split())
            temp = dic[uid] + "님이 나갔습니다."
            answer.append(temp)

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))