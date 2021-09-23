def merge(intervals):
    if not intervals:
        return []
    res = [intervals[0]]
    intervals.sort(key = lambda x : x[0])
    for interval in intervals[1:]:
        if interval[0] <= res[-1][1] :
            res[-1][1] = max(res[-1][1], interval[1])
        else:
            res.append(interval)
    return res
res = merge([[0, 4], [1, 4]])
print(res)
    
    
    
    