class Solution:
    def largest_sum_contiguos_sub_array(self, nums):
        maxh = maxg = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i] + maxh:
                maxh = nums[i] 
            else:
                maxh = nums[i] + maxh
            if maxg < maxh:
                maxg = maxh
        return maxg
        
c = Solution()
res = c.largest_sum_contiguos_sub_array([-1, -2, 3, 4, 5, -2, 6])
print(res)