import heapq
class Solution:
    def find_Kth_max_min(self, nums, k):
        heapq._heapify_max(nums)
        while k :
            element = heapq._heappop_max(nums)
            k -= 1
        return element 
c = Solution()
res = c.find_Kth_max_min([1,2,3,4,5], 2)
print(res)