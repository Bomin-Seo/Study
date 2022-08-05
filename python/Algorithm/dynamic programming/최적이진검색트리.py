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