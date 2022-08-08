
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
