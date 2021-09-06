def rotate( arr, n):
    last = arr[n - 1]
    for i in range(n-1, -1, -1):
        arr[i] = arr[i - 1]
    arr[0] = last
    

    arr[0] = last 
    print(arr)
rotate([1,2,3,4,5], 5)


