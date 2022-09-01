def solution(a, b):
    answer = ''
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_count = 0
    for i in range(a - 1):
        day_count += days[i]

    day_count += b

    answer += day[(day_count + 5) % 7 - 1]
    return answer