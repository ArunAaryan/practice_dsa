def smallestSubWithSum(a, n, x):
    cursum = 0
    left = right = 0
    minlen = n
    while right < n :
        while cursum <= x and right < n:
            cursum += a[right]
            right +=1
        while cursum > x and left < n:
            minlen = min(minlen, right - left )
            cursum -= a[left]
            left +=1
            
    return minlen
        

res = smallestSubWithSum([1,4,45,6,10,19], 6, 51)
print(res)
                


