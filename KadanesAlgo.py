def maxSubArraySum(self,arr,N):
    max_g = max_here = arr[0]
    for i in range(1, N):
        max_here = max(max_here + arr[i], arr[i])
        max_g = max(max_g, max_here)
    return max_g

