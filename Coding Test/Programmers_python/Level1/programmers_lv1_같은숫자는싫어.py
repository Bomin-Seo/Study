def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        else:
            if arr[i] == arr[i-1]:
                continue
            else:
                answer.append(arr[i])

    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))