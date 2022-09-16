def solution(n):
    answer = 0
    bin_n = bin(n)
    count = str(bin_n).count('1')
    while True:
        next = n + 1
        bin_next = bin(next)
        if count == str(bin_next).count('1'):
            answer = next
            break
        n += 1
    return answer

s = 78
print(solution(s))