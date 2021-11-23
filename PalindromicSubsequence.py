class Solution():
    def countPalindromes(self, s):
        self. s = s
        self.dp = [[-1] * len(s) for _ in range(len(s))]
        res =  self._count(0, len(s) - 1)
        print(self.dp)
        return res
    
    def _count(self, i, j):
        if i > j:
            return 0
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        if i == j:
            self.dp[i][j] =1
            return 1 
        elif self.s[i] == self.s[j]:
            self.dp[i][j] =  (self._count(i + 1, j) + self._count(i , j - 1) + 1)
            return self.dp[i][j]
        else:
            self.dp[i][j] =  (self._count(i + 1, j) + self._count(i, j - 1) - self._count(i + 1, j - 1))
            return self.dp[i][j]
s = Solution()
res = s.countPalindromes('aabc')
print(res)