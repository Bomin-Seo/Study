import time
import random

def split(values, first, last):
    splitval = values[first]
    savefirst = first
    first += 1
    while True:
        onCollectSide = True
        while onCollectSide:
            if values[first] > splitval:
                onCollectSide = False
            else:
                first += 1
                onCollectSide = (first <= last)
        onCollectSide = (first <= last)
        while onCollectSide:
            if values[last] <= splitval:
                onCollectSide = False
            else:
                last -= 1
                onCollectSide = (first <= last)
        if first < last:
            temp = values[first]
            values[first] = values[last]
            values[last] = temp
            first += 1
            last -= 1
        if first <= last:
            continue
        break
    splitPoint = last
    temp1 = values[savefirst]
    values[savefirst] = values[splitPoint]
    values[splitPoint] = temp1
    return splitPoint


def quick_sort(values, first, last):
    if first < last:
        splitPoint = split(values, first, last)
        quick_sort(values, first, splitPoint - 1)
        quick_sort(values, splitPoint + 1, last)
    return values

num_list = []
num_list2 = []

for i in range(5000):
    num_list.append(random.randint(1, 1000))
for i in range(10000):
    num_list2.append(random.randint(1, 1000))

start = time.time()
quick_sort(num_list, 0, len(num_list) - 1)

print("quick sort time for n = 5000 : ", time.time() - start)

start = time.time()
quick_sort(num_list2, 0, len(num_list2) - 1)

print("quick sort time for n = 10000 : ", time.time() - start)