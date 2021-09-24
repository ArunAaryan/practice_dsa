def morethanNbyK(nums, k):
    more = len(nums) / k
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    res = [] 
    for key in freq:
        if freq[key] > more:
            res.append(key)
    return res
res = morethanNbyK([1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1 ], 4)
print(res)
