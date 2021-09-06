m = 1000
n = 4

def recur(m, n):
    if m < n:
        return 0
    if n == 0:
        return 1
    res = recur(m - 1, n) + recur(m //2 , n - 1)
    return res
def recurdp(m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for row in range(m + 1):
        for col in range(n + 1):
            if row == 0 or col == 0:
                dp[row][col] = 0
            elif row < col:
                pass
            elif col == 1:
                dp[row][col] = row
            else:
                dp[row][col] = dp[row - 1][col] + dp[row // 2][col - 1]
    return dp[m][n]
res = recur(m, n)
print(res)
res = recurdp(m, n)
print(res)