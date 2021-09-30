def chocolateDistribution(arr, m):
    arr.sort()
    min_res = arr[len(arr) - 1] - arr[0]
    for i in range(0, len(arr) - m + 1):
        min_res = min(min_res, arr[i + m - 1] - arr[i])
    return min_res



res = chocolateDistribution([3, 4, 1, 9, 56, 7, 9, 12], 5)
print(res)
