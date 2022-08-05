# 1번 ------------------------------

def printmatrixf(mat):
    # 행렬의 형태로 출력을 위한 함수
    row = len(mat[0])
    col = len(mat)
    for i in range(col):
        for j in range(row):
            print(f'{mat[i][j]:>3.2f}', end=' ')
        print()


def printmatrix(mat):
    row = len(mat[0])
    col = len(mat)
    for i in range(col):
        for j in range(row):
            print(f'{mat[i][j]:>3}', end=' ')
        print()


class Node:
    def __init__(self, data):
        self.data = data
        # node의 data를 저장합니다
        self.l_child = None
        # node의 왼쪽 자식을 지칭합니다.
        self.r_child = None
        # node의 오른쪽 자식을 지칭합니다.


def tree(key, r, i, j):
    k = r[i][j]
    if k == 0:
        return None
    else:
        p = Node(key[k])
        p.l_child = tree(key, r, i, k - 1)
        p.r_child = tree(key, r, k+1, j)
        # 루트로 삼은 K보다 작은 것은 왼쪽 자식, 큰 것은 오른쪽 자식을 지칭하며
        # 재귀적으로 호출하며 트리구조를 형성합니다.
        return p


def optsearchtree(n, p, a, r):
    for diagonal in range(1, n):
        # 오른쪽 아래로 향하는 대각선이며 주대각선 바로 위의 대각선은 p_i를 의미하며
        # diagonal은 p_i를 나타내는 대각선 위를 지칭합니다.
        for i in range(1, n - diagonal + 1):
            temp = []
            sum_prob = 0
            j = i + diagonal
            for k in range(i, j+1):
                temp.append(a[i][k-1] + a[k+1][j])
                sum_prob += p[k]
            r[i][j] = temp.index(min(temp)) + i
            a[i][j] = min(temp) + sum_prob
            # 가장 적은 값을 도출하는 요소를 a에 저장하며
            # 루트로 삼았을 때 가장 적은 값을 도출하는 루트의 값을 r에 저장합니다.
            # 행이 증가할수록 하삼각행렬의 요소도 증가하므로 i를 더해줍니다.


def print_inOrder(root):
    if not root:
        return None
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)
    # 왼쪽 자식 -> 부모 -> 오른쪽 자식 순으로 출력합니다

def print_preOrder(root):
    if not root:
        return None
    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)
    # 부모 -> 왼쪽 자식 -> 오른쪽 자식

# 1번 ------------------------------

# 2번 ------------------------------
def dna_alignment(a, b):
    m = len(a)  # 행의 개수로 사용될 변수의 값을 할당합니다.
    n = len(b)  # 열의 개수로 사용될 변수의 값을 할당합니다.
    table = [[0 for _ in range(0,n+1)] for _ in range(m+1)]
    minindex = [[(0,0) for _ in range(n+1)] for _ in range(m+1)]
    # table, minindex의 2차원 배열에 (m+1) * (n+1)의 영행렬의 생성합니다.

    for j in range(n-1, -1, -1):
        table[m][j] = table[m][j+1] + 2

    for i in range(m-1, -1, -1):
        table[i][n] = table[i+1][n] + 2
    # 가장 우측하단의 0의 원소로부터 위, 왼쪽으로 갈때마다 2가 증가한 값을 더합니다
    # dna의 길이가 맞지 않을 때 틈을 넣음으로써 2의 penalty값을 갖는 것을 의미합니다.

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            penalty = 0
            if a[i] != b[j]:
                penalty = 1
            table[i][j] = min(table[i+1][j+1] + penalty, table[i+1][j] + 2, table[i][j+1] + 2)
            # 가장 끝부터 비교하여 a 또는 b에 틈이 있는 경우, 또는 불일치, 일치되는 경우를 가정하고,
            # 그 중에서 가장 penalty가 적은 값을 table의 요소로 저장합니다.

            if table[i][j] == table[i + 1][j + 1] + penalty:  # 불일치
                minindex[i][j] = (i + 1, j + 1)
            elif table[i][j] == table[i + 1][j] + 2:  # 틈
                minindex[i][j] = (i + 1, j)
            else:
                minindex[i][j] = (i, j + 1)
            # minindex의 (i,j)요소에는 오른쪽, 아래, 대각선 아래 방향의 3가지 방향에서의
            # 최소값과 일치하는 (x,y) 값을 할당함으로써 어떤 경우가 최적화를 이루는 방식인지 지칭합니다.

    printmatrix(table)
    print()

    x, y = 0, 0
    while x < m and y < n:
        tx, ty = x, y
        print(minindex[x][y])
        (x, y) = minindex[x][y]
        if x == tx + 1 and y == ty + 1:  # 일치 또는 불일치의 경우
            print(a[tx], " ", b[ty])
        elif x == tx and y == ty + 1:  # a의 data에 틈이 발생한 경우
            print(" - ", " ", b[ty])
        else:  # b의 data에 틈이 발생한 경우
            print(a[tx], " ", " -")

# 2번 ------------------------------


if __name__ == '__main__':
    # 1번 ------------------------------
    print("data 1 :")
    p = [0, 1/15, 2/15, 3/15, 4/15, 5/15]
    key = [" ", 'A', 'B', 'C', 'D', 'E']
    n = len(p) - 1
    a = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    r = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

    for i in range(1, n+1):
        a[i][i-1] = 0
        a[i][i] = p[i]
        # a[i][i] 는 자기 자신을 검색하는 경우이므로 p[i]의 값을 할당합니다.
        r[i][i] = i
        # r[i][i]는 노드가 하나인 경우이므로 i값을 할당합니다.
        r[i][i-1] = 0
    a[n+1][n] = 0
    r[n + 1][n] = 0
    optsearchtree(n, p, a, r)

    printmatrixf(a)
    print()
    printmatrix(r)
    print()

    root = tree(key, r, 1, n)
    print("Inorder :")
    print_inOrder(root)
    print()
    print("Preorder :")
    print_preOrder(root)
    print()
    # data 2  ---------------------------------------
    print("data 2 :")
    p = [0, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]
    key = [" ", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    n = len(p) - 1
    a = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    r = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

    for i in range(1, n + 1):
        a[i][i - 1] = 0
        a[i][i] = p[i]
        r[i][i] = i
        r[i][i - 1] = 0
    a[n + 1][n] = 0
    r[n + 1][n] = 0
    optsearchtree(n, p, a, r)

    printmatrixf(a)
    print()
    printmatrix(r)
    print()

    root = tree(key, r, 1, n)
    print("Inorder :")
    print_inOrder(root)
    print()
    print("Preorder :")
    print_preOrder(root)
    print()

    # 1번 ------------------------------

    # 2번 ------------------------------
    a = ['G', 'A', 'C', 'T', 'T', 'A', 'C', 'C']
    b = ['C', 'A', 'C', 'G', 'T', 'C', 'C', 'A', 'C', 'C']
    dna_alignment(a, b)




