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