def merge(left_length, right_length, left, right, data):
    i, j, k = 0, 0, 0
    while i < left_length and j < right_length:
        # 분할된 두 개의 데이터에서 더 작은 값을 가지는 것부터 전체 데이터의 앞의 값으로 채웁니다.
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1
    if i >= left_length:
        # 분할된 2개의 데이터에서 왼쪽의 요소가 모두 비교가 끝났다면
        # 전체 데이터에 오른쪽의 요소를 차례로 첨가합니다.
        for a in range(j, right_length):
            data[k] = right[a]
            k += 1
    elif j >= right_length:
        # 분할된 2개의 데이터에서 오른쪽의 요소가 모두 비교가 끝났다면
        # 전체 데이터에 왼쪽의 요소를 차례로 첨가합니다.
        for b in range(i, left_length):
            data[k] = left[b]
            k += 1


def merge_sort(data_length, data):
    global size, max_space
    # 재귀적으로 호출될 때마다 새로 값을 할당하지 않기 위해서 전역변수로 설정합니다.

    left_length = int(data_length/2)
    right_length = data_length - left_length

    if data_length == 1:
        max_space = True
    # 절반의 데이터가 1개의 데이터만 가질 때까지 분할될 때는, 공간을 반납하기전
    # 병합정렬이 추가적으로 필요한 저장공간의 최대치일때입니다.
    # 데이터의 요소가 1개일 시점을 변곡점으로 삼아 추가적인 최대 공간 크기를 더 계산하지 않기 위해 지정합니다.

    if data_length > 1:
        left = data[:left_length]
        right = data[left_length:]
        if not max_space:
            size += (len(left) + len(right))
        merge_sort(left_length, left)
        merge_sort(right_length, right)
        # 1개의 요소를 가질 때까지 재귀적으로 호출하며 분할합니다.
        merge(left_length, right_length, left, right, data)
        # 1개의 요소까지 분할되었다면 차례로 크기를 비교하고, 합병하며 정렬합니다.

if __name__ == '__main__':
    size = 0
    max_space = False
    original_data = [8, 3, 15, 2, 9, 1, 5, 7, 4, 16, 10, 11, 12, 13, 6, 14]
    print("합병 정렬 전 데이터는 : ", original_data)
    merge_sort(len(original_data), original_data)
    print("합병 정렬 후 데이터는 : ", original_data)
    print("합병정렬 알고리즘 수행에 필요한 추가적인 공간의 크기는 : ", size)
