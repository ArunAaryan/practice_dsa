def spiralTraverse(matrix,r, c):
    left = top = 0
    bottom = r - 1
    right = c - 1
    res = []
    while left <= right and top <= bottom:
        for lr in range(left, right + 1):
            res.append(matrix[top][lr])
        top += 1
        for ud in range(top, bottom + 1):
            res.append(matrix[ud][right])
        right -= 1
        if left > right or top > bottom:
            break
        for rl in range(right, left - 1, - 1):
            res.append(matrix[bottom][rl])
        bottom -= 1
        for bu in range(bottom, top - 1, -1):
            res.append(matrix[bu][left])
        left += 1
    return res



    
