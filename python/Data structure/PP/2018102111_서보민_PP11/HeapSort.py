
def reheap_down(elements, root, bottom):
    leftchild = root * 2 + 1
    rightchild = root * 2 + 2
    if leftchild <= bottom:
        if leftchild == bottom:
            maxchild = leftchild
        else:
            if elements[leftchild] <= elements[rightchild]:
                maxchild = rightchild
            else:
                maxchild = leftchild
        if elements[root] < elements[maxchild]:
            temp = elements[root]
            elements[root] = elements[maxchild]
            elements[maxchild] = temp
            reheap_down(elements, maxchild, bottom)

def heap_sort(values, numValues):
    index = int(numValues/2) - 1
    while index >= 0:
        reheap_down(values, index, numValues - 1)
        index -= 1

    index = numValues - 1
    while index >= 1:
        temp = values[0]
        values[0] = values[index]
        values[index] = temp
        reheap_down(values, 0, index - 1)
        index -= 1

