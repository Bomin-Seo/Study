class Node2:
    def __init__(self, level, weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include

    def __lt__(self, other):
        return self.bound < other.bound

def kp_Best_FS():
    global maxProfit2
    global bestset2
    # root node를 생성하고 priority queue에 삽입합니다.
    pq = queue.PriorityQueue()
    temp = n * [0]
    v = Node2(0, 0, 0, 0, temp)
    v.bound = compBound(v)
    pq.put(v)

    while not pq.empty():
        v = pq.get()
        if v.bound < maxProfit2:  # 마디가 유망한지 확인합니다.
            # level의 수와 인덱스가 대응하는 요소를 넣은 경우를 가정하여 계산합니다.
            u = Node2(v.level + 1, v.weight + weight[v.level], v.profit + profit[v.level], 0, temp)
            u.include = v.include[:]
            u.include[v.level] = 1
            u.bound = compBound(u)
            if u.weight <= W and u.profit > maxProfit2:
                maxProfit2 = - u.profit  # bound와의 비교 연산을 위하여 부호를 바꾸어 할당합니다.
                bestset2 = u.include[:]
            if u.bound < maxProfit2:
                pq.put(u)

            # level의 수와 인덱스가 대응하는 요소를 넣지 않은 경우를 가정하여 계산합니다.
            u = Node(v.level + 1, v.weight, v.profit, 0, temp)
            u.include = v.include[:]
            u.bound = compBound(u)

            if u.bound < maxProfit2:
                pq.put(u)

    maxProfit2 *= -1  # minheap계산을 위해 bound값을 계산할 때 부호를 바꾸었기 때문에 결과 출력을 위해 다시 부호를 바꿉니다.


def compBound(u):  # bound를 계산합니다.
    if u.weight >= W:
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while j < n and totweight + weight[j] <= W:
            totweight += weight[j]
            result += profit[j]
            j += 1
        k = j
        if k < n:
            result += (W-totweight) * (profit[k] // weight[k])
        return -result  # minheap이므로 부호를 바꾸어서 처리합니다.
