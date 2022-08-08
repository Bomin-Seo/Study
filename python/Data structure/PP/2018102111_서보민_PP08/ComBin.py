def combinations(group, members):
    if members == 1:
        return group
    elif members == group:
        return 1
    else:
        return (combinations(group - 1, members - 1) + combinations(group - 1, members))

