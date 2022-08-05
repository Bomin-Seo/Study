import random
import matplotlib.pyplot as plt
import math

# 1번 문제 ----------------------------------------------------------------------
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

# 2번 문제 ----------------------------------------------------------------------
def prod(num1, num2):
    threshold = 2
    n = max(len(str(num1)), len(str(num2)))
    if num1 == 0 or num2 == 0:  # 두 수 중에 0의 값이 있다면 바로 0을 반환합니다
        return 0
    elif n <= threshold:
        # n이 threshold값이 2보다 작을 경우, 즉 num1, num2가 2자리수 이하 일때는
        # 일반적인 계산방식을 이용하여 값을 반환합니다.
        return num1 * num2
    else:
        m = math.floor(n/2)
        x = num1 // 10**m
        y = num1 % 10**m
        w = num2 // 10**m
        z = num2 % 10**m
        # 큰 수인 num1과 num2를 num1 =  x * (10**m) + y 의 방식으로 자릿수를 기준으로 반으로 나눕니다
        r = prod(x + y, w + z)
        p = prod(x, w)
        q = prod(y, z)
        # 큰 수를 2개로 나눈 것을 기반으로 재귀적으로 호출하며
        # 곱셈 공식인 (ax + b)(cx + d) = acx2 + (ad + bc)x + bd의 꼴로 값을 반환합니다.
        return p * 10**(2*m) + (r - p - q) * 10**m + q

if __name__ == "__main__":
    #  1번 실행 코드 ------------------------------------
    data_size = [100, 200, 300, 400]
    aver_compare = []
    for n in data_size:
        compare_count = 0
        randint_list = []
        compare = []
        for j in range(100):
            for i in range(n):
                elem = random.randint(0, n)
                randint_list.append(elem)
            quicksort(randint_list, 0, n)
            compare.append(compare_count)
        aver_comp = sum(compare)/100
        aver_compare.append(aver_comp)

    for i in range(4):
        print("Data size : ", data_size[i])
        print("Average number of comparisons : ", aver_compare[i])
        print()
    plt.xlabel('Data size(n)')
    plt.ylabel("Average number of comparisons")
    plt.plot(data_size, aver_compare, marker="o")
    plt.show()

    # 1번 실행 코드 끝 -----------------------------------
    # 2번 실행 코드 --------------------------------------
    a = 1234567812345678
    b = 2345678923456789
    print("큰 정수 곱셈 알고리즘 결과 : ", prod(a, b))
    print("일반적인 곱셉 결과 : ", a*b)
    # 2번 실행 코드 끝-------------------------------------

