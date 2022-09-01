def solution(s):
    answer = True
    a, b = 0, 0

    if s[0] == ')' or s[len(s) - 1] == '(':
        return False
    elif s.count("(") != (len(s) / 2):
        return False
    else:
        for i in range(len(s)):
            if s[i] == '(':
                a += 1
            else:
                b += 1
                if a < b:
                    return False

    return True