class Solution:
    def sort_colors(self, nums):
        one = zero = 0
        two = len(nums) - 1
        while one <= two:
            if nums[one] == 0:
                nums[one], nums[zero] = nums[zero], nums[one]
                zero += 1
                one += 1
            elif nums[one] == 2:
                nums[two], nums[one] = nums[one], nums[two]  
                two -= 1
            else:
                one += 1
        return nums
c = Solution()
res = c.sort_colors([2,2,1,1,0,1,2,0,1])
print(res)