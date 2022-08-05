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