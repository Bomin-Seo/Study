def solution(sizes):
    width_l = []
    vertical_l = []
    for i in sizes:
        width_l.append(i[0])
        vertical_l.append(i[1])
    review = []
    if max(width_l) > max(vertical_l):
        width = max(width_l)
        for i in range(len(sizes)):
            if sizes[i][0] < sizes[i][1]:
                review.append(sizes[i][0])
            else:
                review.append(sizes[i][1])
        vertical = max(review)
    else:
        vertical = max(vertical_l)
        for i in range(len(sizes)):
            if sizes[i][0] < sizes[i][1]:
                review.append(sizes[i][0])
            else:
                review.append(sizes[i][1])
        width = max(review)

    answer = width * vertical
    return answer

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))