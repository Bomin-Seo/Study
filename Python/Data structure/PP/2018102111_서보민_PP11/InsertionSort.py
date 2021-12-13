def insertion_sort(values):
    numvalues = len(values)
    count = 0
    while count < numvalues:
        finished = False
        current = count
        moretosearch = current != 0
        while moretosearch and not finished:
            if values[current] < values[current - 1]:
                temp = values[current]
                values[current] = values[current - 1]
                values[current - 1] = temp
                current -= 1
                moretosearch = current != 0
            else:
                finished = True
        count += 1