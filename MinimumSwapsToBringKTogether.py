def minSwapToBringElements(arr, k):
    right = 0
    for i in arr:
        if i <= k:
            right += 1
    greater = 0
    for i in range(right):
        if arr[i] > k:
            greater += 1
    left = 0
    ans = greater
    while right < len(arr):
        if arr[left] > k:
            greater -= 1
        if arr[right] > k:
            greater += 1
        ans = min(ans, greater)
        left += 1
        right += 1
    return ans 







res = minSwapToBringElements([5, 3, 6, 1, 3, 2, 9], 3)
print(res)
