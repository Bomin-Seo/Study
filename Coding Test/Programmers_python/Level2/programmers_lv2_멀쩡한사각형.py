import math

def solution(w, h):
    answer = w * h - (w + h - 1)
    gcd = math.gcd(w, h)
    if w == 1 or h == 1:
        return answer
    elif w == h:
        answer += (h - 1)
    else:
        a = [i for i in range(w//gcd, w, w//gcd)]
        answer += len(a)
    return answer

print(solution(8, 12))