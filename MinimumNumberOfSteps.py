class Solution:
    def minimum_jumps(self, nums):
        steps = 0
        cur_far, cur_end = 0, 0
        for i in range(len(nums) - 1):
            cur_far = max(cur_far, i + nums[i])
            if i == cur_end:
                steps += 1
                cur_end = cur_far
        return steps
c = Solution()
res = c.minimum_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])
print(res)