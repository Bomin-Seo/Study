import time
import random

def insertion_sort(values):
    numvalues = len(values)
    count = 0
    while count < numvalues:
        finished = False
        current = count
        moretosearch = current != 0
        while moretosearch and not finished:
            if values[current] < values[current - 1]:
                values[current], values[current - 1] = values[current - 1], values[current]
                current -= 1
                moretosearch = current != 0
            else:
                finished = True
        count += 1

ans_list = []
ans_list2 = []

for i in range(5000):
    ans_list.append(random.randint(1, 1000))
for i in range(10000):
    ans_list2.append(random.randint(1, 1000))

start = time.time()
insertion_sort(ans_list)

print("insertion sort time for n = 5000 : ", time.time() - start)

start = time.time()
insertion_sort(ans_list2)

print("insertion sort time for n = 10000 : ", time.time() - start)