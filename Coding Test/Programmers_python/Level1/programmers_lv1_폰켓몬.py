def solution(nums):
    n = len(nums) // 2

    if len(set(nums)) >= n:
        answer = n
    else:
        answer = len(set(nums))
    return answer

nums = [3,3,3,2,2,4]
print(solution(nums))