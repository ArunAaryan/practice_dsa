class Solution:
    def countInversions(self, arr):
        res = []
        al = []
        for i in range(len(arr)):
            for j in range(i + 1,len(arr)):
                if arr[i] > arr[j]:
                    res.append( (arr[i], arr[j]))
                al.append((arr[i], arr[j]))
        print(al)
        return res, len(res)

    def countInversionMergeSort(self, arr):
        n = len(arr)
        temp = [0] * n 
        return self.mergeSort(arr, temp, 0, n - 1)
    def mergeSort(self, arr,  temp, left, right):
        count = 0
        if left < right:
            mid = (left + right) // 2
            count += self.mergeSort(arr, temp, left, mid)
            count += self.mergeSort(arr, temp, mid + 1, right)
            count += self.merge(arr,temp,  left, mid, right)
        return count
    def merge(self, arr, temp, left, mid, right):
        count = 0
        i, j, k = left, mid + 1, left
        while i <= mid and j<= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
                k += 1
            else:
                temp[k] = arr[j]
                count += (mid - i) + 1 
                j += 1
                k += 1
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        for i in range(left, right + 1):
            arr[i] = temp[i]
        return count
            




c = Solution()
# res = c.countInversions([1, 20, 6, 4, 5])
res = c.countInversionMergeSort([1, 20, 6, 4, 5])
print(res)