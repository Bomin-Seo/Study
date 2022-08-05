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