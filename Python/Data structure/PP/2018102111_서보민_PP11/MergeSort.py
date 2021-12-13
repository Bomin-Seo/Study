def merge_sort(values, first, last):
    if first < last:
        mid = int((first+last)/2)
        merge_sort(values, first, mid)
        merge_sort(values, mid + 1, last)
        merge(values, first, mid, mid+1, last)

def merge(values, leftFirst, leftLast, rightFirst, rightLast):
    index = leftFirst
    savefirst = leftFirst
    temp = [0] * len(values)
    while leftFirst <= leftLast and rightFirst <= rightLast:
        if values[leftFirst] < values[rightFirst]:
            temp[index] = values[leftFirst]
            leftFirst += 1
        else:
            temp[index] = values[rightFirst]
            rightFirst += 1
        index += 1
    while leftFirst <= leftLast:
        temp[index] = values[leftFirst]
        leftFirst += 1
        index += 1

    while rightFirst <= rightLast:
        temp[index] = values[rightFirst]
        rightFirst += 1
        index += 1

    while savefirst <= rightLast:
        values[savefirst] = temp[savefirst]
        savefirst += 1



