#  1번 문제
inf = 1000

def dijkstra(n, w, f):
    NoC = 0
    touch = [0] * n  # 각 노드로 가는 최단거리는 0번 노드에서 시작합니다.
    length = [0] * n
    for i in range(1, n):
        length[i] = w[0][i]  # 초기 상황에서 최단길이는 0번 노드에서 각 노드로의 길이입니다.
    for i in range(1, n):
        min = inf
        for j in range(1, n):
            if 0 <= length[j] < min:
                min = length[j]
                # length 중 작은 값을 min에 할당합니다.
                # 이미 최단거리가 계산된 node에 대한 거리 값은 -1로 설정되어 있기 때문에
                # 조건문에서 고려되지 않습니다.
                vnear = j
                # 최단거리를 가지는 node 번호를 vnear에 할당합니다.
        f.add((touch[vnear], vnear))
        # 0번 노드에서 각 노드로 가는 최단 경로 중 마지막 노드와 해당 노드의 이음선을
        # f에 추가합니다.

        # Y에 node가 추가됨에 따라 최단 경로의 길이가 수정될 수 있습니다.
        # 0번 노드에서 각 노드로 가는 길이와 Y에 속한 노드를 거쳐 가는 경로 중
        # 더 짧은 거리로 Length를 update합니다.
        for k in range(1, n):
            if length[vnear] + w[vnear][k] < length[k]:
                length[k] = length[vnear] + w[vnear][k]
                touch[k] = vnear
        length[vnear] = -1

        # vnear와 연결된 0번 노드를 제외한 노드의 수를 셉니다.
        for m in range(1, n):
            if m != vnear and w[vnear][m] != inf:
                NoC += 1
    return f, NoC
# 1번 문제 끝

# 2번 문제
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
# 2번 문제 끝


if __name__ == '__main__':
    # 1번 실행 코드
    w = [[0, 15, 4, 11, 5], [inf, 0, inf, 1, inf], [inf, 4, 0, 2, inf], [inf, inf, inf, 0, inf], [inf, 3, inf, 1, 0]]
    n = 5
    f = set()
    result_f, result_NoC = dijkstra(n, w, f)
    print(result_f)
    print(result_NoC)
    # 1번 실행 코드 끝

    # 2번 실행 코드
    ans = 0
    node = 0
    n = 7
    col = n * [0]
    total, node_count = queens(n, -1, col)
    print("해의 총 개수 : ", total)
    print("생성된 상태공간트리 노드 수 : ", node)
    # 2번 실행코드 끝

