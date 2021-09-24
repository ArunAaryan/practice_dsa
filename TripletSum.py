def tripletSum(nums, sum):
    n = len(nums)
    for i in range(n):
        s = set()
        req = sum - nums[i] 
        for j in range(i + 1, n):
            if req - nums[j] in s:
                return (nums[i], nums[j], req - nums[j])
            s.add(nums[j])
    return False

res = tripletSum([1, 4, 45, 6, 10, 8], 22)
print(res)

