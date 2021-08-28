class Solution:
    def reverse_an_array(self, arr):
        i, j = 0, len(arr) - 1
        while i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr
c = Solution()
res = c.reverse_an_array([1,2,3,4,5,6])
print(res)