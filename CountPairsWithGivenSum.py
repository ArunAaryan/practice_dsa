def countPairsWithGivenSum(nums, k):
    elements = {}
    count = 0
    for num in nums:
        if k - num in elements:
            count += elements[k - num]
        if num in elements:
            elements[num] += 1
        else:
            elements[num] = 1
    return count



res = countPairsWithGivenSum([1,5,7,1],6)
print(res)