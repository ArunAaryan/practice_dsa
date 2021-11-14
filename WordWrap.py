def solveWordWrap(nums, k):
    n = len(nums)
    dp = [0] * n
    dp[n - 1] = 0
    for i in range(n - 2, -1 ,-1):
        dp[i] = float('inf')
        curl = -1
        for j in range(i, n):
            curl += nums[j] + 1
            if curl > k:
                break
            if j == n - 1: #last word
                cost = 0
            else:
                rem = k - curl
                cost = rem * rem + dp[j + 1]
            if cost < dp[i]:
                dp[i] = cost
    print(dp)
    return dp[0]
res = solveWordWrap([3,2,2,5],6)
print(res)




        
