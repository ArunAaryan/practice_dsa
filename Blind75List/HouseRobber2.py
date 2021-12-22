def rob(nums):
    def robhelper(l, r):
        rob = notrob = 0
        for i in range(l, r):
            notrob, rob = rob, max(notrob + nums[i], rob)
        return rob
    n = len(nums)
    ans = max(robhelper(0, n - 1), robhelper(1, n))
    return ans


res = rob([1, 2])
print(res)
