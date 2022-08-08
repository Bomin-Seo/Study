'''
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
'''

n = int(input())
'''
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

ans = 1 # 전부 2 x 1 인 경우

n = int(input())

q = n//2
for i in range(1, q + 1):
    ans += factorial(n-i) / (factorial(i) * factorial(n-2*i))

print(int(ans % 10007))
'''

ans = [1, 2]
for i in range(999):
    ans.append(ans[i] + ans[i + 1])

print(ans[n - 1] % 10007)




