class Solution:
    def decodeWays(self, s):  # O(n) space solution for decode ways, as the current value
        # only depends on the prev, prevprev value , we can store them.
        oneprev, twoprev = 0, 1
        n = len(s)
        if s[n - 1] != '0':
            oneprev = 1
        for i in range(n - 2, -1, -1):
            if s[i] != '0':
                cur = oneprev
                if s[i] == '1' or s[i] == '2' and s[i + 1] < '7':
                    cur += twoprev
            twoprev = oneprev
            oneprev = cur
        return oneprev

    def numDecodings(self, s: str) -> int:  # O(n) time and space solution.
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        if s[n-1] != "0":
            dp[n-1] = dp[n]
        for i in range(n-2, -1, -1):
            if s[i] != "0":
                dp[i] = dp[i + 1]
                if s[i] == "1" or s[i] == "2" and s[i+1] < "7":
                    dp[i] += dp[i + 2]
        return dp[0]

    def decodeWaysMemo(self, s):
        dp = [0] * len(s)

        def numWays(s, p):
            n = len(s)
            if p == n:
                return 1
            # print(p)
            if dp[p]:
                return dp[p]

            if s[p] == '0':
                return 0
            res = numWays(s, p + 1)
            dp[p] = res
            if (p < n - 1 and (s[p] == '1' or s[p] == '2' and s[p + 1] < '7')):
                res += numWays(s, p + 2)
                dp[p] = res
            return res
        if len(s) == 0:
            return 0
        else:
            return numWays(s, 0)


c = Solution()
res = c.decodeWaysMemo('11106')
print(res)
