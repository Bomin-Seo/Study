def solution(s):
    answer = True
    p_num, y_num = 0, 0
    for i in s:
        if i == 'p' or i == 'P':
            p_num += 1
        elif i == 'y' or i == 'Y':
            y_num += 1

    if p_num != y_num:
        return False

    return True