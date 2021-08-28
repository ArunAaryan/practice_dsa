class Solution:
    def cyclic_rotate_right(self, nums):
        last = nums[len(nums) - 1]
        for i in range(len(nums) - 1, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = last
        return nums
    def cyclic_rotate_left(self, nums):
        first = nums[0]
        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1]
        nums[len(nums) - 1] = first
        return nums
c = Solution()
res = c.cyclic_rotate_right([1,2,3,4])
res1 = c.cyclic_rotate_left([1,2,3,4])
print(res)
print(res1)