def solution(id_list, report, k):
    answer = []
    report = set(report)
    dic = {}
    dic2 = {}
    block = []

    for i in id_list:
        dic[i] = 0
        dic2[i] = 0

    for i in report:
        a, b = map(str, i.split())
        dic[b] += 1

    for i in range(len(dic)):
        if dic[id_list[i]] >= k:
            block.append(id_list[i])

    for i in report:
        a, b = map(str, i.split())
        if b in block:
            dic2[a] += 1

    for i in dic2.values():
        answer.append(i)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))