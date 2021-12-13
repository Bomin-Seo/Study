
def short_bubble(values, numValues):
    current = 0
    sort = False
    while current < numValues - 1 and not sort:
        bubble_up(values, current, numValues - 1, sort)
        current += 1

def bubble_up(values, startIndex, endIndex, sort):
    sort = True
    index = endIndex
    while index > startIndex:
        if values[index] < values[index - 1]:
            temp = values[index]
            values[index] = values[index - 1]
            values[index - 1] = temp
            sort = False
        index -= 1
    return sort
