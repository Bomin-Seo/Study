from itertools import combinations

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    possible = list(combinations(nums, 3))
    for i in possible:
        num = i[0] + i[1] + i[2]
        if is_prime_number(num):
            answer += 1
    return answer

nums = [1,2,7, 6,4]
print(solution(nums))