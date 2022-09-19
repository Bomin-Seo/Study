def right(s):
    temp = []
    if s[0] == '}' or s[0] == ']' or s[0] == ')':
        return False
    if s.count('(') != s.count(')') or s.count('{') != s.count('}') or s.count('[') != s.count(']'):
        return False
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            temp.append(s[i])
        else:
            if s[i] == ')':
                if len(temp) == 0:
                    return False
                elif temp[-1] == '(':
                    temp.pop()
                else:
                    return False
            elif s[i] == '}':
                if len(temp) == 0:
                    return False
                elif temp[-1] == '{':
                    temp.pop()
                else:
                    return False
            else:
                if len(temp) == 0:
                    return False
                elif temp[-1] == '[':
                    temp.pop()
                else:
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