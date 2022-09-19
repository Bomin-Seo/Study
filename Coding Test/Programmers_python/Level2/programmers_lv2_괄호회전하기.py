def right(s):
    a1, a2, b1, b2, c1, c2 = 0, 0, 0, 0, 0, 0
    if s[0] == '}' or s[0] == "]" or s[0] == ')':
        return False

    if s.count('{') != s.count('}') or s.count('[') != s.count(']') or s.count('(') != s.count(')'):
        return False

    for i in range(len(s)):
        match s[i]:
            case '(':
                a1 += 1
            case ')':
                a2 += 1
            case '{':
                b1 += 1
            case '}':
                b2 += 1
            case '[':
                c1 += 1
            case ']':
                c2 += 1

        if a2 > a1 or b2 > b1 or c2 > c1:
            return False

    return True

def solution(s):
    answer = 0
    for i in range(1, len(s) + 1):
        temp = s[i:] + s[:i]

        if right(temp):
            answer += 1

    return answer

s = "}]()[{"
print(solution(s))