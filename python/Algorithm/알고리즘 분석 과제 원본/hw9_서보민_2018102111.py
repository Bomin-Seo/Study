class Heap(object):
    n = 0

    def __init__(self, data):
        self.data = data
        self.n = len(self.data) - 1

    def addElt(self, elt):
        # 요소를 하나 추가하고 heap 형태를 유지하는 함수입니다.
        self.data.append(elt)
        self.n += 1
        self.siftup(self.n)

    def siftup(self, i):
        # 자식 노드가 부모노드보다 크다면 key값을 상호 교환하고
        # i를 i//2로 바꾸어 root까지 진행합니다.
        while i >= 2:
            if self.data[i] > self.data[i//2]:
                temp = self.data[i//2]
                self.data[i//2] = self.data[i]
                self.data[i] = temp
            i = i//2

    def siftdown(self, i):
        siftkey = self.data[i]
        parent = i
        spotfound = False
        while 2 * parent <= self.n and spotfound == False:
            # 자식 노드를 가지고 있는 경우에만 반복문 동작
            if 2 * parent < self.n and self.data[2 * parent] < self.data[2 * parent + 1]:
                # 자식 노드가 2개이면서 오른쪽 자식의 key가 더 큰 경우
                largerchild = 2 * parent + 1
            else:
                # 자식 노드가 1개이거나 왼쪽 자식의 key가 더 큰 경우
                largerchild = 2 * parent
            if siftkey < self.data[largerchild]:
                self.data[parent] = self.data[largerchild]
                parent = largerchild
            else:
                spotfound = True
        self.data[parent] = siftkey

    def makeheap1(self):
        # data를 aliasing 후 self.data를 비우고 요소를 하나씩 추가하며
        # siftup을 통하여 heap의 형태를 유지합니다.
        temp_arr = self.data[:]
        self.data = [0]
        self.n = len(self.data) - 1
        for i in range(1, len(temp_arr)):
            self.data.append(temp_arr[i])
            self.n = len(self.data) - 1
            self.siftup(i)

    def makeheap2(self):
        # self.data길이의 2로 나눈 몫은 항상 자식 노드를 가지는 마지막 node index를 지칭합니다
        # 요소가 모두 추가된 후이므로 자식 노드를 가지는 마지막 노드를 siftdown을 통해
        # sub heap이 heap의 형태를 갖추게 하며 index를 하나씩 줄여가며
        # root node까지 진행합니다.
        for i in range(len(self.data)//2, 0, -1):
            self.siftdown(i)

    def root(self):
        # root의 key값을 저장한 뒤 맨 마지막 배열의 위치와 교환하고
        # 맨 마지막 요소를 삭제합니다
        # 그리고 다시 heap의 형태를 갖춘 후 root의 key값을 반환합니다.
        keyout = self.data[1]
        self.data[1] = self.data[self.n]
        del self.data[self.n]
        self.n -= 1
        if self.n > 0:
            self.siftdown(1)
        return keyout

    def removekeys(self):
        # root의 key를 temp_arr에 저장하고 root값을 제거한 후
        # 다시 heap의 형태로 만들고 root 값이 없을 때 까지 진행합니다.
        temp_arr = []
        for i in range(self.n, 0, -1):
            temp_arr.append(self.root())
        return temp_arr


def heapsort1(a):
    a = Heap(a)
    a.makeheap1()
    ans = a.removekeys()
    return ans


def heapsort2(a):
    a = Heap(a)
    a.makeheap2()
    ans = a.removekeys()
    return ans


if __name__ == '__main__':
    a = [0, 11, 14, 2, 7, 6, 3, 9, 5]
    b = Heap(a)
    b.makeheap1()
    print("방법 1의 makeheap 후 data : ", b.data)
    s = heapsort1(a)
    print("heap sort 후의 data : ", s)
    print()

    c = Heap(a)
    c.makeheap2()
    print("방법 2의 makeheap 후 data : ", c.data)
    c.addElt(50)
    print("방법 2의 50 추가 후 data : ", c.data)
    s2 = heapsort2(a)
    print("heap sort 후의 data : ", s2)



