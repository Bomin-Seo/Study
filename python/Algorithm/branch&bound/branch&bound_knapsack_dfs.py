def promising(i, weight, profit):
    global maxp
    if weight > W:
        return False
    else:
        j = i + 1
        bound = profit
        totweight = weight
        while (j < n) and (totweight + w[j] <= W):
            totweight = totweight + w[j]
            bound += p[j]
            j += 1
        k = j
        if k <= n-1:
            bound = bound + (W-totweight) * (p[k] // w[k])
        return bound > maxp

def kp(i, profit, weight):
    global bestset
    global maxp
    global num_nodes
    num_nodes += 1
    if (weight <= W) and (profit > maxp):
        maxp = profit
        bestset = include[:] # Deep copy

    if promising(i, weight, profit):
        include[i+1] = 1
        kp(i+1, profit + p[i+1], weight + w[i+1])
        include[i+1] = 0
        kp(i+1, profit, weight)