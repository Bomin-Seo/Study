#  1번 문제/
def promising(i, weight, total):
    return (weight + total >= W) and (weight == W or weight + w[i+1] <= W)
# return에 들어가있는 조건문과 같이 검사하여 weight의 합으로 W를 만들수 있는지에 대한 여부를 판단합니다.


def s_s(i, weight, total, include):
    global node
    if promising(i, weight, total):
        node += 2  # 유망하다고 판단되면 새로운 노드 2개를 만들어 유망성을 점검합니다.
        if weight == W:
            node -= 2
            # weight == W를 만족하면 해를 찾은 경우이지만 promising조건에 True를 반환하기 때문에
            # 추가되지 않은 node 2개를 차감합니다.
            print("W = ", W, "를 만족시키는 해 :", include)
            # W를 표현하기 위해 사용된 weight의 포함 여부를 출력합니다.
        else:
            # 다음 가중치를 포함시키거나 포함시키지 않고 함수를 재귀적으로 호출하며
            # weight의 요소의 합이 W를 만족시키는지 확인합니다.
            include[i+1] = 1
            s_s(i+1,weight+w[i+1], total - w[i+1], include)
            include[i+1] = 0
            s_s(i+1, weight, total - w[i+1], include)
# 1번 문제 끝

# 2번 문제
def color(i, vcolor):
    global node2
    # 유망하다고 판단되면 m개 만큼의 노드를 생성한 후 유망성 및 결과를 검증합니다.
    if promising2(i, vcolor):
        node2 += m
        if i == n - 1:
            node2 -= m
            print(vcolor)
            # 모든 노드를 검사한 후에는 추가적인 node가 필요없으므로
            # 추가된 node를 차감해줍니다.
        else:
            for c in range(1, m + 1):
                vcolor[i + 1] = c
                color(i + 1, vcolor)
        # n번 노드의 색깔의 교체해가며 유망성 및 결과를 확인합니다.


def promising2(i, vcolor):
    switch = True
    j = 0
    # 연결되어 있으면서 색깔이 같은 노드가 있는 경우를 유망하지 않다고 판단하며
    # 그 외의 경우는 유망하다고 판단하여 True/False값을 반환합니다.
    while j < i and switch:
        if W[i][j] and vcolor[i] == vcolor[j]:
            switch = False
        j += 1
    return switch

# 2번 문제 끝


if __name__ == '__main__':
    # 1번 실행 코드
    print("1번 문제")
    n = 5
    w = [1, 2, 3, 4, 15]
    W = 15
    node = 1
    print("items = ",w, "W = ", W)
    include = n * [0]
    total = 0
    for k in w:
        total += k
    s_s(-1, 0, total, include)
    print("총 노드의 수 : ", node)
    print()
    # 1번 실행 코드 끝

    # 2번 실행 코드
    print("2번 문제")
    n = 5
    W = [[0, 1, 1, 0, 1], [1, 0, 1, 1, 0], [1, 1, 0, 1, 0], [0, 1, 1, 0, 1], [1, 0, 0, 1, 0]]
    vcolor = n * [0]
    m = 3
    node2 = 0
    color(-1, vcolor)
    print("총 노드의 수 : ", node2)
    # 2번 실행코드 끝

