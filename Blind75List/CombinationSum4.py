class Solution:
    # dp solved similar to coin change problem but here find all possible combinations for change 
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[0] is set to 1 for base case
        dp = [1] + [0] * target
        for i in range(target + 1):
            for j in nums:
                if i - j >= 0:
                    dp[i] += dp[i - j]
        return dp[-1]
    def combinationSum4Optimized(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                # this optimization works for iterations of i where i < maxElement in nums
                if num  > i: break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
        return combs[target]