def subArraySumZero(nums):
    is_present = set()
    sum = 0
    for num in nums:
        sum += num
        if sum == 0 or sum in is_present:
            return True
        is_present.add(sum)
    return False
res = subArraySumZero([3, -1, -1, -1, 6])
print(res)
