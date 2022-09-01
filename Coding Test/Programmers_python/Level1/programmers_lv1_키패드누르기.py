def solution(numbers, hand):
    answer = ''
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    left = dic['*']
    right = dic['#']

    for i in numbers:
        current = dic[i]
        if i in [1, 4, 7]:
            answer += 'L'
            left = current
        elif i in [3, 6, 9]:
            answer += 'R'
            right = current
        else:
            left_leng = abs(current[0] - left[0]) + abs(current[1] - left[1])
            right_leng = abs(current[0] - right[0]) + abs(current[1] - right[1])
            if left_leng < right_leng:
                answer += 'L'
                left = current
            elif left_leng > right_leng:
                answer += 'R'
                right = current
            else:
                if hand == 'right':
                    answer += 'R'
                    right = current
                else:
                    answer += 'L'
                    left = current
    return answer