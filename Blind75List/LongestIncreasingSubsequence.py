# https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)
from bisect import bisect_left
class Solution:  # 68 ms, faster than 93.92%
    def lengthOfLIS(self, nums):
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)  # Find the index of the smallest number >= x
                sub[idx] = x  # Replace that number with x because we no longer compare with that element as it is not the last element
        return len(sub)



        