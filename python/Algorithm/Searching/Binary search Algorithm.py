import random

class data:
    def __init__(self, n=0):
        self.n = n
        self.elem = self.make_data(self.n)
        self.compare_count = 0

    def make_data(self, n):
    # data(n)으로 객체가 생성되면 1~n까지의 임의의 수를 n개 생성하고 비내림차순으로 정렬합니다
        elem = []
        for i in range(n):
            elem.append(random.randint(1, n))
        elem = sorted(elem)
        return elem

    def location(self, item, low, high):
        # low가 high값보다 커진 경우, 마지막으로 비교한 후
        # index값으로 'not found'의 의미로 -1을 반환하며
        # 데이터 수에 대한 비교 회수를 측정하기 위하여 self.compare_count값을 반환합니다.
        if low >= high:
            self.compare_count += 1
            return -1, self.compare_count
        else:
            mid = int((low + high) / 2)
            if item == self.elem[mid]:
            # 찾고자 하는 값을 데이터 내에서 찾은 경우 비교횟수를 증가한 후
            # 찾고자 하는 값의 데이터 내의 index번호와 비교 횟수를 반환합니다.
                self.compare_count += 1
                return mid, self.compare_count
            elif item < self.elem[mid]:
            # 찾고자 하는 값이 데이터의 중앙값보다 작을 경우, 데이터의 앞 절반으로 범위를 축소합니다
                self.compare_count += 1
                return self.location(item, low, mid - 1)
            else:
            # 찾고자 하는 값이 데이터의 중앙값보다 클 경우, 데이터의 뒤 절반으로 범위를 축소합니다
                self.compare_count += 1
                return self.location(item, mid + 1, high)

    def binsearch(self, x):
        index, compare = self.location(x, 0, self.n)
        return index, compare

if __name__ == '__main__':
    aver = 0
    for i in range(1000):
        x = data(128)
        ranint = random.randint(1, 128)
        index, compare = x.binsearch(ranint)
        aver += compare
    print("데이터의 개수가 128개일 때 평균적으로 : ", aver/1000,"번 비교를 수행합니다")

    aver = 0
    for i in range(1000):
        x = data(256)
        ranint = random.randint(1, 256)
        index, compare = x.binsearch(ranint)
        aver += compare
    print("데이터의 개수가 256개일 때 평균적으로 : ", aver/1000,"번 비교를 수행합니다")

    aver = 0
    for i in range(1000):
        x = data(512)
        ranint = random.randint(1, 512)
        index, compare = x.binsearch(ranint)
        aver += compare
    print("데이터의 개수가 512개일 때 평균적으로 : ", aver/1000,"번 비교를 수행합니다")


    print("이분 검색시 데이터의 개수가 2배 증가할 때 마다 평균 비교 회수가 약 1회 증가합니다")
    print()
