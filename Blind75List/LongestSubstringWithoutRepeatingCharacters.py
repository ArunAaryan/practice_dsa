class Solution:
    def lengthOfLongestSubstring(self, s) : # solve using sliding window
        maxl = windowStart = 0 
        seen = {}
        for idx, char in enumerate(s):
            if char in seen and windowStart <= seen[char]:
                windowStart = seen[char] + 1
            else:
                maxl = max(maxl, idx - windowStart + 1)
            seen[char] = idx
        return maxl
      

s = Solution()
res = s.lengthOfLongestSubstring('dvdf')
print(res)




        