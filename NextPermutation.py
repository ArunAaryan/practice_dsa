class Solution:
    def nextPermutation(self, nums ):
        last = len(nums) - 2
        while (last >= 0 and nums[last + 1] <= nums[last]):
            last -= 1
        if last >= 0:
            last_greater = len(nums) - 1
            while nums[last_greater] <= nums[last]:
                last_greater -= 1
            nums[last], nums[last_greater] = nums[last_greater], nums[last]
        self.reverse(nums,last + 1)
        return nums
    def reverse(self,nums, i):
        s = i
        j = len(nums) - 1 
        while s < j:
            nums[s], nums[j] = nums[j], nums[s]
            s += 1
            j -= 1
s = Solution()
res = s.nextPermutation([3, 2, 1])
print(res)