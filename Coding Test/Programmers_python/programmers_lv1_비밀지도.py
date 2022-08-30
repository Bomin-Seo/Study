def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    for i in range(len(arr1)):
        arr1_bin.append(format(arr1[i], 'b').zfill(n))
        arr2_bin.append(format(arr2[i], 'b').zfill(n))

    for i in range(n):
        temp = ''
        for j in range(n):
            if arr1_bin[i][j] == '1' or arr2_bin[i][j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))
