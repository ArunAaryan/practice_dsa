class Solution:
    def find_max_min(self, nums):
        if not nums:
            return 0
        maximum = minimum = nums[0]
        for num in nums:
            if num > maximum:
                maximum = num
            elif num < minimum:
                minimum = num
        return (maximum, minimum)

c = Solution()
res = c.find_max_min([10, 9, 1, -1, 20])
print(res)