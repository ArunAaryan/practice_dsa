def rotateMatrix(arr):
    res = []
    r = len(arr) 
    c = len(arr[0]) 
    for col in range(c - 1, -1, -1):
        a = []
        for row in range(r - 1, -1, -1):
            a.append(arr[row][col])
        res.append(a)
    print(res[::-1])
             

rotateMatrix([[1,2,3],[4,5,6],[7,8,9]])






