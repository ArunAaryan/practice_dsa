import sys
def solveWordWrap(arr, n, k):
    dp = [0] * n
    dp[n - 1] = 0
    for i in range(n - 2, -1, -1):
        currlen = -1
        dp[i] = sys.maxsize
        for j in range(i, n):
            currlen += (arr[j] + 1)
            if (currlen > k):
                break
            if (j == n - 1):
                cost = 0
            else:
                cost = ((k - currlen) * 
                        (k - currlen) + dp[j + 1])
            if (cost < dp[i]):
                dp[i] = cost
    print(dp)
# Driver Code
if __name__ == "__main__":
    
    arr = [3,2,2 ]
    n = len(arr)
    M = 4
    solveWordWrap(arr, n, M)

# This code is contributed by ita_c
