class Solution:     
    def longest_increasing_subsequence(self, arr):
        n = len(arr)
        cache = [1] *  n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if arr[i] < arr[j]:
                    cache[i] = max(cache[i], 1 + cache[j])
        return max(cache)
c = Solution()
res = c.longest_increasing_subsequence([1,6,3,4,5])
print(res)