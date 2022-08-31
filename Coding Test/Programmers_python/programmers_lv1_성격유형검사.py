def solution(survey, choices):
    answer = ''
    types_dic = {'R':0 ,'T':0, 'C': 0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(survey)):
        if choices[i] in range(1, 4):
            types_dic[survey[i][0]] += (4 - choices[i])
        else:
            types_dic[survey[i][1]] += (choices[i] - 4)

    for i in range(0, 8, 2):
        if types_dic[list(types_dic.keys())[i]] >= types_dic[list(types_dic.keys())[i+1]]:
            answer += list(types_dic.keys())[i]
        else:
            answer += list(types_dic.keys())[i+1]
    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))