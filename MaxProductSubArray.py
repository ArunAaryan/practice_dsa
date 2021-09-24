def maxProduct(arr, n):
    max_val = min_val = max_g =  arr[0]
    for i in range(1, n):
        if arr[i] < 0:
            max_val, min_val = min_val, max_val
        max_val = max(max_val * arr[i], arr[i])
        min_val = min(min_val * arr[i], arr[i])
        max_g = max(max_g, max_val)
    return max_g

res = maxProduct([6, -3, -10, 0, 2], 5)
print(res)
