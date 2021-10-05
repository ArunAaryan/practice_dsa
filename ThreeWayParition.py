def threeWayPartition_(arr, a, b): # only works if the elements are present in the array
    n = len(arr) 
    first = second = 0
    while arr[first] != a:
        first += 1
    while arr[second] != b:
        second += 1
    val = 0
    while val < n:
        if arr[val] < a and val > first:
            arr[val], arr[first] = arr[first] , arr[val]
        if arr[val] < b and val > second:
            arr[val], arr[second] = arr[second] , arr[val]
        val += 1    
    return arr

def threeWayPartition(arr, a, b):
    left , right = 0, len(arr) - 1
    val = 0
    while val <= right:
        if arr[val] < a:
            arr[val], arr[left] = arr[left], arr[val]
            left += 1
            val += 1
        elif arr[val] > b:
            arr[val], arr[right] = arr[right], arr[val]
            right -= 1
        else:
            val += 1 
    return arr

        

# res = threeWayPartition([1,0,3,2,4], 1, 3)
res = threeWayPartition([1, 2, 3, 3, 4], 1, 3)
# res = threeWayPartition([1,0,3,2,4], 1, 3)
# res = threeWayPartition([1,0,3,2,4], 1, 3)
print(res)

