def bubble_sort(values):
    current = 0
    index = len(values) - 1
    while current < len(values) - 1:
        while index > current:
            if values[index] < values[index - 1]:
                temp = values[index]
                values[index] = values[index - 1]
                values[index - 1] = temp
            index -= 1
        index = len(values) - 1
        current += 1



