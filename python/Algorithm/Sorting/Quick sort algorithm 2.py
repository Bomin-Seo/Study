def partition(data, low, high, pivotpoint):
    global compare_count  # 재귀로 호출될 때 값을 새로 할당하지 않기 위해 전역 변수로 선언
    pivotitem = data[low]  # pivotitem으로 첫번째 항목을 고릅니다
    j = low  # low값을 유지하기 위해 새로운 변수 j에 low값을 할당합니다.
    for i in range(low + 1, high):
        if data[i] < pivotitem:
            j += 1
            # data[i]가 pivotitem보다 작을때만 j를 증가시킴으로써,
            # j는 pivotitem보다 작은 그룹의 제일 오른쪽 요소의 index를 나타냅니다
            data[i], data[j] = data[j], data[i]
            compare_count += 1
    pivotpoint[0] = j
    # pivotpoint를 pivotitem보다 작은 그룹의 가장 오른쪽 index로 지정합니다.
    data[low], data[pivotpoint[0]] = data[pivotpoint[0]], data[low]
    # data의 첫번째 요소와 pivotitem보다 작은 값을 서로 바꿈으로써
    # pivotitem 왼쪽에는 작은 값이, 오른쪽에는 같거나 큰 값이 분류됩니다.


def quicksort(data, low, high):
    pivotpoint = [0]
    if high > low:  # 적어도 데이터의 개수가 2개 이상일 경우, quick sort 수행
        partition(data, low, high, pivotpoint)
        # Pivot item을 기준으로 작은 값을 왼쪽으로, 같거나 큰 값을 오른쪽으로 분류합니다
        quicksort(data, low, pivotpoint[0] - 1)
        # pivotitem보다 작은 값을 가지는 데이터를 다시 quicksort를 수행합니다.
        quicksort(data, pivotpoint[0] + 1, high)
        # pivotitem보다 큰 값을 가지는 데이터를 다시 quicksort를 수행합니다.