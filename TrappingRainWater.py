def trappingRainWater(arr):
    low , high = 0, len(arr) - 1
    left_max = right_max = 0
    water = 0
    while low <= high:
        if arr[low] < arr[high]:
            if arr[low] > left_max:
                left_max = arr[low]
            else:
                water += left_max - arr[low]
            low += 1
        else:
            if arr[high] > right_max:
                right_max = arr[high]
            else:
                water += right_max - arr[high]
            high -= 1
    return water


def maxWater(arr, n): # review the code
    # indices to traverse the array
    left = 0
    right = n-1
 
    # To store Left max and right max
    # for two pointers left and right
    l_max = 0
    r_max = 0
 
    # To store the total amount
    # of rain water trapped
    result = 0
    while (left <= right):
         
        # We need check for minimum of left
        # and right max for each element
        if r_max <= l_max:
             
            # Add the difference between
            #current value and right max at index r
            result += max(0, r_max-arr[right])
             
            # Update right max
            r_max = max(r_max, arr[right])
             
            # Update right pointer
            right -= 1
        else:
             
            # Add the difference between
            # current value and left max at index l
            result += max(0, l_max-arr[left])
             
            # Update left max
            l_max = max(l_max, arr[left])
             
            # Update left pointer
            left += 1
    return result
 
    
res = trappingRainWater([7,4,0,9])
res = trappingRainWater([8, 8, 2, 4, 5, 5, 1])
print(res)




