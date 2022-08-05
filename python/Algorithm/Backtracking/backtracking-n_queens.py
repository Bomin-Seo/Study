def promising(i, col):
    global node  # 재귀적으로 호출될 때마다 새로 할당되는 것을 막기 위해 전역변수로 선언합니다.
    node += 1  # 유망한지에 대한 여부를 검사할 때 마다 node의 개수가 늘어납니다.
    k = 0
    switch = True
    # i번째 여왕이 위치와 같은 열 혹은 대각선에 다른 여왕이 위치하면 false를 반환합니다.
    while k < i and switch:
        if col[i] == col[k] or abs(col[i] - col[k]) == i-k:
            switch = False
        k += 1
    return switch

def queens(n, i, col):
    global ans  # 재귀적으로 호출될 때마다 새로 할당되는 것을 막기 위해 전역변수로 선언합니다.
    if promising(i, col):
        if i == n - 1:
            ans += 1
        else:
            for j in range(n):
                col[i+1] = j
                queens(n, i+1, col)
    return ans, node