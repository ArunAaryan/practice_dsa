class Solution:
    def minimum_jumps(self, nums, n):
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] == 0:
            return -1
        max_reach = nums[0]
        rem_steps = nums[0]
        jumps = 1
        for i in range(1, n):
            if i == n - 1:
                return jumps
            max_reach = max(max_reach, i + nums[i])
            rem_steps -= 1
            if rem_steps == 0:
                jumps += 1
                if i == max_reach:
                    return - 1
            step = max_reach - i
        return -1



c = Solution()
res = c.minimum_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 12)
print(res)