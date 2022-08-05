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