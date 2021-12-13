
def selection_sort(values):
    endIndex = len(values) - 1
    current = 0
    while current < endIndex:
        minval = min(values[current:])
        minindex = values.index(minval, current)
        temp = values[current]
        values[current] = values[minindex]
        values[minindex] = temp
        current += 1


