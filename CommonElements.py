def commonElements(x, y, z):
    if not x or not y or not z:
        return []
    first = second = third = 0
    # current_greatest = max(x[first], y[second], z[third])
    res = []
    while first < len(x) and second < len(y) and third < len(z):
        current_greatest = max(x[first], y[second], z[third])
        if x[first] < current_greatest:
            first += 1
        if y[second] < current_greatest:
            second += 1
        if z[third] < current_greatest:
            third += 1
        if x[first] == y[second] and y[second] == z[third]:
            if res:
                if res[-1] != x[first] :
                    res.append(x[first])
            else:
                res.append(x[first])
            first += 1
            second += 1
            third += 1
    return res

def commonElementsGFGApproach(x, y, z):
    first = second = third = 0
    res = []
    while first < len(x) and second < len(y) and third < len(z):
        if x[first] == y[second] == z[third]:
            res.append(x[first])
            first += 1
            second += 1
            third += 1
        elif x[first] < y[second]:
            first += 1
        elif y[second] < z[third]:
            second += 1
        else:
            third += 1
    return res


res = commonElementsGFGApproach([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]) 
print(res)