def commonElementsInMatrix(arr):
    if len(arr) == 1:
        return arr
    common = {}
    for i in range(len(arr[0])):
        common[arr[0][i]] = 1

    for row in range(1, len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] in common:
                common[arr[row][col]] += 1
    res = []
    for key in common:
        if common[key] >= len(arr):
            res.append(key)
    return(res)

arr = [[1, 2, 1, 4, 8], [3, 7, 8, 5, 1], [8, 7, 7, 3, 1], [8, 1, 2, 7, 9]]
res = commonElementsInMatrix(arr)
print(res)
