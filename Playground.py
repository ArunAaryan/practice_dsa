def increasing_sequence(arr):
    maxg = maxh = last = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > last:
            maxh += arr[i]
        else:
            maxh = arr[i]
        last = arr[i]
        maxg = max(maxg, maxh)
    return maxg
res = increasing_sequence([1,202,2,3,200,4,5])
print(res)
res = increasing_sequence([5,6,8,20])
print(res)

def find_maximum_profit(arr):
    buy = 0
    maxg = 0
    profit = 0
    for sell in range(1, len(arr)):
        if arr[sell] > arr[buy]:
            profit = arr[sell] - arr[buy]
        else:
            buy = sell
        maxg = max(profit, maxg)
    return maxg


# res = find_maximum_profit([10,18,26,31,4,53,69])
# print(res)

