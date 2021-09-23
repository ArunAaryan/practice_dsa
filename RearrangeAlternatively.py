def rearrange(nums):
    n = len(nums)
    nums.sort()
    i, j = 1, 1
    while j < n:
        if nums[j] > 0:
            break
        j += 1
    while nums[i] < 0 and j < n:
        nums[i], nums[j] = nums[j], nums[i]
        i += 2
        j += 1
    return nums
res = rearrange([-1,-2,-3,-4,1,2,3,4])
print(res)



            