tmp_list = [0]

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
    tmp_list[0] = last
    splitPoint = tmp_list[0]
    temp1 = values[savefirst]
    values[savefirst] = values[splitPoint]
    values[splitPoint] = temp1

def quick_sort(values, first, last):
    if first < last:
        split(values, first, last)
        splitPoint = tmp_list[0]
        quick_sort(values, first, splitPoint - 1)
        quick_sort(values, splitPoint + 1, last)
    return values
